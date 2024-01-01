# 표준
import logging
# 서드파티
import pandas as _pd
# 커스텀
from client import *
from util import get_logger, this_func

MARKETCAP='https://crix-api-cdn.upbit.com/v1/crix/marketcap?currency=KRW'
TRADABLE='https://s3.ap-northeast-2.amazonaws.com/crix-production/crix_master'

_logger = get_logger('downbit')
_logger.setLevel(logging.INFO)

def get_marketcap_from_upbit():
    _logger.info(this_func())
    response = get_api(MARKETCAP)
    json = response.json() 
    cols =  ('koreanName', 'symbol', 'marketCap', 'accTradePrice24h')
    df : _pd.DataFrame = _pd.DataFrame(json).loc[:, cols]
    _logger.debug(f'marketcap_size : {len(df)}')
    _logger.debug(df)
    return df

def get_observable_symbol(marketcap: _pd.DataFrame):
    _logger.info(this_func())
    alt = marketcap.query('symbol != "BTC" and symbol != "ETH"')
    alt_marketcap = alt.marketCap.mean()
    alt_accTradePrice24h = alt.accTradePrice24h.mean()
    expr = f'marketCap > {alt_marketcap} and accTradePrice24h > {alt_accTradePrice24h}'
    df = marketcap.query(expr).set_index('symbol')
    _logger.debug(f'observable_size : {len(df)}')
    _logger.debug(df)
    return df

def get_tradable_from_upbit():
    _logger.info(this_func())
    response = get_api(TRADABLE)
    json = response.json() 
    cols =  ('koreanName', 'baseCurrencyCode')
    expr = 'pair.str.contains("KRW") and marketState == "ACTIVE" and exchange == "UPBIT"'
    df : _pd.DataFrame = _pd.DataFrame(json)\
        .query(expr).loc[:, cols].set_index('baseCurrencyCode')
    _logger.debug(f'tradable_size : {len(df)}')
    _logger.debug(df)
    return df

def get_filtered_symbol():
    _logger.info(this_func())
    marketcap = get_marketcap_from_upbit()
    observable = get_observable_symbol(marketcap)
    tradable = get_tradable_from_upbit()
    df = observable.join(tradable, lsuffix='_x', rsuffix='_y', how='inner')
    _logger.info(f'filterd_size : {len(df)}')
    symbol = df.index.to_list()
    _logger.debug(symbol)
    return symbol