import tushare as ts
import pandas as pd
from utils import reduce_mem_usage

def get_ex_moneyflow(**kwargs):
    """
    :param trade_date: str, 交易日期 (二选一)
    :param start_date: str, 开始日期 (二选一)
    :param end_date: str, 结束日期
    :return: 指定日期范围内的上市股票
        ts_code       股票代码
        ggt_ss        港股通（上海）
        ggt_sz        港股通（深圳）
        hgt           沪股通（百万元）
        sgt           深股通（百万元）
        north_money   北向资金（百万元）= hgt + sgt
        south_money   南向资金（百万元）= ggt_ss + ggt_sz
    """
    pro = ts.pro_api()
    return pro.moneyflow_hsgt(**kwargs)


def get_moneyflow(trade_date = None, ts_code = None, **kwargs):
    """
    :param trade_date: str，选择当天所有正常交易的股票日内数据，与ts_code二选其一
    :param ts_code: str, 股票代码，选择指定股票日内数据，与date二选其一
    :param kwargs: 传入 moneyflow 的参数，当ts_date非空有效
    :return: 股票交易数据
    1、仅有trade_date参数，返回当天所有股票数据
    2、仅有ts_code参数，返回指定股票数据
        ts_code                股票代码
        trade_date             交易日期
        小单：5万以下 中单：5万～20万 大单：20万～100万 特大单：成交额>=100万
        buy_**_vol             *单买入量（手）
        buy_**_amount          *单买入金额（万元）
        sell_**_vol            *单卖出量（手）
        sell_**_amount         *单卖出金额（万元）
        net_mf_vol             净流入量（手）
        net_mf_amount          净流入额（万元）
    """
    pro = ts.pro_api()
    if ts_code:
        stock_moneyflow = pro.moneyflow(ts_code = ts_code, **kwargs)
        if not kwargs and len(stock_moneyflow) == 4000:
            furtheset_date = stock_moneyflow.trade_date.values[-1]
            stock_moneyflowfurther = pro.moneyflow(ts_code = ts_code, end_date = furtheset_date)
            stock_moneyflow = pd.concat([stock_moneyflow, stock_moneyflowfurther]).\
                                drop_duplicates().reset_index(drop=True)
    if trade_date:
        stock_moneyflow = pro.moneyflow(trade_date = trade_date)
    return stock_moneyflow
