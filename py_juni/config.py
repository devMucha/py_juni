"""
py_juni/config.py
------------------
Centralna konfiguracja asystenta Juni.

Trzymanie ustawień w jednym miejscu ułatwia ich późniejsze
przeniesienie np. do pliku .yaml / .env, gdy aplikacja się rozrośnie.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class JuniConfig:
    # Nazwa "wake worda" / słowa aktywującego (na przyszłość, na razie
    # nasłuch działa w trybie ciągłym po komendzie startu).
    wake_word: str = "juni"

    # Język rozpoznawania mowy (kod dla biblioteki speech_recognition / Google).
    language: str = "pl-PL"

    # Próg ciszy / czułość mikrofonu - czas (s) ciszy kończący jedną wypowiedź.
    pause_threshold: float = 0.8

    # Maksymalny czas (s) oczekiwania na rozpoczęcie mowy zanim nastąpi timeout.
    listen_timeout: float = 5.0

    # Maksymalna długość pojedynczej wypowiedzi (s).
    phrase_time_limit: float = 10.0

    # Czy przy starcie automatycznie kalibrować poziom szumu otoczenia.
    calibrate_on_start: bool = True

    # Poziom logowania: DEBUG, INFO, WARNING, ERROR.
    log_level: str = "INFO"


# Pojedyncza, globalna instancja konfiguracji używana w całej aplikacji.
config = JuniConfig()