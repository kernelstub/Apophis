import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime


class Logger:
    _configured: bool = False

    @staticmethod
    def _ensure(file_name: str, path: str) -> logging.Logger:
        if not Logger._configured:
            os.makedirs(path, exist_ok=True)
            logger = logging.getLogger("Apophis")
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s Apophis | %(levelname)s | %(message)s", datefmt="%H:%M:%S")
            fh = RotatingFileHandler(os.path.join(path, file_name), maxBytes=262144, backupCount=3)
            fh.setFormatter(formatter)
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            logger.addHandler(fh)
            logger.addHandler(ch)
            Logger._configured = True
        return logging.getLogger("Apophis")

    @staticmethod
    def log(status: str, file_name: str = "logs.vs", path: str = "./logs/") -> None:
        logger = Logger._ensure(file_name, path)
        logger.info(status)

    @staticmethod
    def error(status: str, file_name: str = "logs.vs", path: str = "./logs/") -> None:
        logger = Logger._ensure(file_name, path)
        logger.error(status)
