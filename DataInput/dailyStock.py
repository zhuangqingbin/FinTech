import tushare as ts
import pandas as pd
from utils import reduce_mem_usage, TOCKEN

def get_daily_stock(ts_code = None, date = None, **kwargs):
    """
    :param date: str，选择当天所有正常交易的股票日内数据，与ts_code二选其一
    :param ts_code: str, 股票代码，选择指定股票日内数据，与date二选其一
    :param kwargs: 传入 daily 和 daily_basic 的参数，当ts_date非空有效
    :return: 股票交易数据
    1、仅有date参数，返回当天所有股票数据
    2、仅有ts_code参数，返回指定股票数据
        ts_code       股票代码
        trade_date    交易日期
        open          开盘价
        high          最高价
        low           最低价
        close         收盘价
        pre_close     昨收价
        change        涨跌额
        pct_chg       涨跌幅 （未复权
        vol           成交量 （手）
        amount        成交额 （千元）
        turnover_rate 换手率（%）
        turnover_rate_f     	换手率（自由流通股）
        volume_ratio            量比
        pe                      市盈率（总市值/净利润）
        pe_ttm                  市盈率（TTM）
        pb                      市净率（总市值/净资产）
        ps                      市销率
        ps_ttm                  市销率（TTM）
        total_share             总股本 （万股）
        float_share             流通股本 （万股）
        free_share              自由流通股本 （万）
        total_mv                总市值 （万元）
        circ_mv                 流通市值（万元）
    """
    try:
        pro = ts.pro_api()
    except:
        ts.set_token(TOCKEN)
        pro = ts.pro_api()
    if ts_code:
        if not (ts_code.endswith('SZ') or ts_code.endswith('SH')):
            if ts_code.startswith('0') or ts_code.startswith('3'):
                ts_code = ts_code + '.SZ'
            if ts_code.startswith('6'):
                ts_code = ts_code + '.SH'

        daily_stock = pro.daily(ts_code = ts_code, **kwargs)
        daily_stock_basic = pro.daily_basic(ts_code = ts_code, **kwargs)
        if not kwargs:
            if len(daily_stock) == 5000:
                daily_stock_furtheset_date = daily_stock.trade_date.values[-1]
                daily_stock_further = pro.daily(ts_code = ts_code,
                                                end_date = daily_stock_furtheset_date)
                daily_stock = pd.concat([daily_stock, daily_stock_further]). \
                                         drop_duplicates().reset_index(drop=True)
            if len(daily_stock_basic) == 4000:
                daily_stock_basic_furtheset_date = daily_stock_basic.trade_date.values[-1]
                daily_stock_basic_further = pro.daily_basic(ts_code = ts_code,
                                                            end_date = daily_stock_basic_furtheset_date)
                daily_stock_basic = pd.concat([daily_stock_basic, daily_stock_basic_further]).\
                                               drop_duplicates().reset_index(drop=True)
    if date:
        daily_stock = pro.daily(trade_date = date)
        daily_stock_basic = pro.daily_basic(trade_date = date)
    return daily_stock.merge(daily_stock_basic, how = 'left', on = ['ts_code', 'trade_date', 'close']).\
                    pipe(reduce_mem_usage, verbose = False)







