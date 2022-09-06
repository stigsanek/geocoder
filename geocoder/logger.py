import logging
import sys
from datetime import datetime as dt
from logging.handlers import RotatingFileHandler
from pathlib import Path

from geocoder.config import LOGS_DIR


class Logger:
    """Logger"""
    __FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

    def __init__(self, name):
        self.__logger = logging.getLogger(name)

    def get_logger(self):
        """Returns logger object"""
        self.__logger.setLevel(logging.DEBUG)
        self.__logger.addHandler(self.__get_console_handler())
        self.__logger.addHandler(self.__get_file_handler())
        self.__logger.propagate = False
        return self.__logger

    def __get_console_handler(self):
        """Returns console handler"""
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(self.__get_format())
        return handler

    def __get_file_handler(self):
        """Returns file handler"""
        handler = RotatingFileHandler(self.__get_log_path(), encoding='utf-8')
        handler.setFormatter(self.__get_format())
        return handler

    def __get_log_path(self):
        """Creates file name for logging"""
        Path.mkdir(LOGS_DIR, parents=True, exist_ok=True)
        file_name = f"{dt.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        return str(LOGS_DIR / file_name)

    def __get_format(self):
        """Returns format"""
        return logging.Formatter(self.__FORMAT)


logger = Logger(__name__).get_logger()
