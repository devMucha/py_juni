"""
py_juni/juni.py
-----------------
Główna klasa aplikacji - asystent systemowy Juni.

Na ten moment odpowiada za pętlę nasłuchu mikrofonu i prostą
interpretację rozpoznanych komend. Docelowo to tutaj będzie
spinana logika "intencji" (np. otwórz aplikację, sprawdź pogodę itd.).
"""

from py_juni.config import config
from py_juni.listener import MicrophoneListener
from py_juni.logger import get_logger

logger = get_logger("core")

# Komendy kończące działanie asystenta.
EXIT_COMMANDS = {"koniec", "wyłącz się", "zamknij się", "stop"}


class Juni:
    """Reprezentuje uruchomioną instancję asystenta Juni."""

    def __init__(self):
        self._config = config
        self._running = False

    def run(self) -> None:
        """Uruchamia główną pętlę nasłuchu i obsługi komend głosowych."""
        self._running = True
        logger.info(
            "Juni gotowy do pracy. Mów do mikrofonu (powiedz '%s' aby zakończyć).",
            "/".join(EXIT_COMMANDS),
        )

        with MicrophoneListener(self._config) as listener:
            while self._running:
                text = listener.listen_once()
                if text is None:
                    continue

                self._handle_command(text)

    def stop(self) -> None:
        self._running = False

    def _handle_command(self, text: str) -> None:
        """Bardzo prosta interpretacja rozpoznanego tekstu."""
        if text in EXIT_COMMANDS:
            logger.info("Otrzymano komendę zakończenia pracy.")
            self.stop()
            return

        # TODO: tutaj docelowo trafi router intencji / komend Juni.
        logger.info("Komenda do obsłużenia: '%s' (logika jeszcze nie zaimplementowana).", text)