import logging
import sys

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    # formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s")
    formatter = logging.Formatter("%(levelname)s:%(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def this_func():
    # https://dhznsdl.tistory.com/30
    return sys._getframe(1).f_code.co_name