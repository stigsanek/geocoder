import logging
import os
import sys
from datetime import datetime as dt
from logging.handlers import RotatingFileHandler


class Logger:
    __FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

    def __init__(self, name):
        self.__logger = logging.getLogger(name)

    def get_logger(self):
        self.__logger.setLevel(logging.DEBUG)
        self.__logger.addHandler(self.__get_console_handler())
        self.__logger.addHandler(self.__get_file_handler())
        self.__logger.propagate = False
        return self.__logger

    def __get_console_handler(self):
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(self.__get_format())
        return handler

    def __get_file_handler(self):
        handler = RotatingFileHandler(self.__create_file_name(), encoding='utf-8')
        handler.setFormatter(self.__get_format())
        return handler

    def __create_file_name(self):
        abs_path = os.path.dirname(os.path.abspath(__file__))
        prefix = os.path.join(abs_path, '..', 'logs', 'log-')
        return prefix + dt.now().strftime('%Y-%m-%d') + '.log'

    def __get_format(self):
        return logging.Formatter(self.__FORMAT)


logger = Logger(__name__).get_logger()
