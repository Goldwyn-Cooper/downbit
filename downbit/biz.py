# 표준
import logging as _logging
from time import sleep as _sleep
# 서드파티
import pandas as _pd
# 커스텀
from .client import get_api as _get_api
from .util import this_func as _this_func
from .util import get_logger as _get_logger

MARKETCAP='https://crix-api-cdn.upbit.com/v1/crix/marketcap?currency=KRW'
TRADABLE='https://s3.ap-northeast-2.amazonaws.com/crix-production/crix_master'
# CANDLE_DAYS='https://api.upbit.com/v1/candles/days'
CANDLE_HOURS='https://api.upbit.com/v1/candles/minutes/60'

_logger = _get_logger('downbit')
_logger.setLevel(_logging.INFO)

def get_marketcap_from_upbit():
    _logger.info(_this_func())
    response = _get_api(MARKETCAP) 
    cols = ('koreanName', 'symbol', 'marketCap', 'accTradePrice24h')
    df : _pd.DataFrame = _pd.DataFrame(response.json()).loc[:, cols]
    _logger.debug(f'marketcap_size : {len(df)}')
    _logger.debug(df)
    return df

def get_observable_symbol(marketcap: _pd.DataFrame):
    _logger.info(_this_func())
    alt = marketcap.query('symbol != "BTC" and symbol != "ETH"')
    expr = f'marketCap > {alt.marketCap.mean()}\
             and accTradePrice24h > {alt.accTradePrice24h.mean()}'
    df = marketcap.query(expr).set_index('symbol')
    _logger.debug(f'observable_size : {len(df)}')
    _logger.debug(df)
    return df

def get_tradable_from_upbit():
    _logger.info(_this_func())
    response = _get_api(TRADABLE)
    expr = 'pair.str.contains("KRW") and marketState == "ACTIVE" and exchange == "UPBIT"'
    df : _pd.DataFrame = _pd.DataFrame(response.json())\
        .query(expr).loc[:, ('koreanName', 'baseCurrencyCode')]
    _logger.debug(f'tradable_size : {len(df)}')
    _logger.debug(df)
    return df.set_index('baseCurrencyCode')

def get_filtered_symbol():
    _logger.info(_this_func())
    marketcap = get_marketcap_from_upbit()
    observable = get_observable_symbol(marketcap)
    tradable = get_tradable_from_upbit()
    df = observable.join(tradable, lsuffix='_x', rsuffix='_y', how='inner')
    _logger.debug(f'filterd_size : {len(df)}')
    _logger.debug(df)
    return df.index.to_list()

def get_hour_candle(symbol:str, count:int=200, sleep:float=0.04):
    _logger.info(_this_func())
    headers = dict(accept='application/json')
    params = dict(market=f'KRW-{symbol}', count=count)
    # response = _get_api(CANDLE_DAYS, params=params, headers=headers)
    response = _get_api(CANDLE_HOURS, params=params, headers=headers)
    df = _pd.DataFrame(response.json())
    df['candle_date_time_kst'] = _pd.to_datetime(df['candle_date_time_kst'])
    cols = ('high_price', 'low_price', 'trade_price')
    df = df.set_index('candle_date_time_kst').loc[:, cols]
    df.index.set_names('dt', inplace=True)
    df.columns = ['high', 'low', 'close']
    _sleep(sleep)
    _logger.debug(f'{symbol}_price_size : {len(df)}')
    _logger.debug(df)
    return df