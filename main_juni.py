"""
main_juni.py
------------
Punkt wejścia aplikacji Juni - asystenta systemowego.

Uruchomienie:
    python main_juni.py
"""

import sys

from py_juni.juni import Juni
from py_juni.logger import get_logger

logger = get_logger(__name__)


def main() -> int:
    logger.info("Uruchamiam asystenta Juni...")

    try:
        assistant = Juni()
        assistant.run()
    except KeyboardInterrupt:
        logger.info("Przerwano przez użytkownika (Ctrl+C). Zamykam Juni.")
    except Exception:
        logger.exception("Wystąpił nieoczekiwany błąd krytyczny aplikacji.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())