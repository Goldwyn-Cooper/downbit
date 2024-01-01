import logging as _logging
import sys as _sys
from datetime import datetime as _dt
from dateutil.relativedelta import relativedelta as _rd

def get_logger(logger_name):
    logger = _logging.getLogger(logger_name)
    # formatter = _logging.Formatter("%(asctime)s %(levelname)s:%(message)s")
    formatter = _logging.Formatter("%(levelname)s:%(message)s")
    handler = _logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def this_func():
    # https://dhznsdl.tistory.com/30
    return _sys._getframe(1).f_code.co_name

def get_day(fmt, prev_count:int=0) -> str:
    td = (_dt.utcnow() + _rd(hours=9)).date() - _rd(days=prev_count)
    return td.strftime(fmt)