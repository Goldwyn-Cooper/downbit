# 표준
from unittest import TestCase, main
# 커스텀
from biz import *

class MyTests(TestCase):

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
        
if __name__ == '__main__':
    logger = logging.getLogger("downbit")
    # logger.setLevel(logging.DEBUG)
    main()