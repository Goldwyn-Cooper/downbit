# 표준
from unittest import TestCase
import logging
# 커스텀
from .biz import *
from .util import this_func

class MyTests(TestCase):
    def setUp(self):
        logger = logging.getLogger("downbit")
        logger.setLevel(logging.DEBUG)

    def test_get_observable_symbol(self):
        print(f'[{this_func()}]')
        marketcap = get_marketcap_from_upbit()
        self.assertTrue(len(get_observable_symbol(marketcap)))

    def test_get_marketcap_from_upbit(self):
        print(f'[{this_func()}]')
        self.assertTrue(len(get_marketcap_from_upbit()))

    def test_get_filtered_symbol(self):
        print(f'[{this_func()}]')
        self.assertTrue(get_filtered_symbol())
    
    def test_get_day_candle(self):
        print(f'[{this_func()}]')
        self.assertEqual(len(get_hour_candle('BTC', 200)), 200)
        
# python -m unittest downbit/test.py