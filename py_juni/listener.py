"""
py_juni/listener.py
--------------------
Odpowiada wyłącznie za przechwytywanie dźwięku z mikrofonu
i zamianę go na tekst (Speech-to-Text).

Wykorzystuje bibliotekę `speech_recognition`, która pod spodem
korzysta z silnika rozpoznawania mowy Google (wymaga internetu).
Można ją łatwo podmienić na silnik offline (np. Vosk, Whisper).
"""

from typing import Optional

import speech_recognition as sr

from py_juni.config import JuniConfig
from py_juni.logger import get_logger

logger = get_logger("listener")


class MicrophoneListener:
    """Nasłuchuje mikrofonu i zwraca rozpoznany tekst."""

    def __init__(self, config: JuniConfig):
        self._config = config
        self._recognizer = sr.Recognizer()
        self._recognizer.pause_threshold = config.pause_threshold
        self._microphone: Optional[sr.Microphone] = None

    def __enter__(self) -> "MicrophoneListener":
        self._microphone = sr.Microphone()
        self._microphone.__enter__()

        if self._config.calibrate_on_start:
            logger.info("Kalibruję poziom szumu otoczenia (1 sekunda ciszy)...")
            self._recognizer.adjust_for_ambient_noise(self._microphone, duration=1)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._microphone is not None:
            self._microphone.__exit__(exc_type, exc_val, exc_tb)

    def listen_once(self) -> Optional[str]:
        """
        Nasłuchuje jednej wypowiedzi i próbuje zamienić ją na tekst.

        Zwraca:
            str  - rozpoznany tekst (małymi literami)
            None - gdy nie udało się nic rozpoznać / wystąpił timeout
        """
        if self._microphone is None:
            raise RuntimeError(
                "MicrophoneListener musi być używany w bloku 'with'."
            )

        logger.debug("Nasłuchuję...")
        try:
            audio = self._recognizer.listen(
                self._microphone,
                timeout=self._config.listen_timeout,
                phrase_time_limit=self._config.phrase_time_limit,
            )
        except sr.WaitTimeoutError:
            logger.debug("Brak mowy w zadanym czasie (timeout).")
            return None

        try:
            text = self._recognizer.recognize_google(
                audio, language=self._config.language
            )
            logger.info("Rozpoznano: %s", text)
            return text.lower()
        except sr.UnknownValueError:
            logger.debug("Nie udało się zrozumieć mowy.")
            return None
        except sr.RequestError as exc:
            logger.error("Błąd usługi rozpoznawania mowy: %s", exc)
            return None