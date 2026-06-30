"""
py_juni/logger.py
------------------
Wspólna konfiguracja logowania dla całej aplikacji.
"""

import logging
import sys

from py_juni.config import config

_CONFIGURED = False


def _configure_root_logger() -> None:
    global _CONFIGURED
    if _CONFIGURED:
        return

    root = logging.getLogger("juni")
    root.setLevel(config.log_level)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    handler.setFormatter(formatter)
    root.addHandler(handler)

    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """Zwraca logger podrzędny w hierarchii 'juni.<name>'."""
    _configure_root_logger()
    return logging.getLogger(f"juni.{name}")