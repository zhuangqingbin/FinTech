import tushare as ts
import pandas as pd
from utils import reduce_mem_usage
from utils import Time

def get_ipo(start_date):
    """
    :param start_date: str, 开始日期
    :return: 指定日期范围内的上市股票
        ts_code       股票代码
        sub_code      申购代码
        name          名称
        ipo_date      上网发行日期
        issue_date    上市日期
        amount        发行总量（万股）
        market_amount 上网发行总量（万股）
        price         发行价格
        pe            市盈率
        limit_amount  个人申购上限（万股）
        funds         募集资金（亿元）
        ballot        中签率
    """
    pro = ts.pro_api()
    ipo_data = pro.new_share(start_date = start_date)
    return ipo_data[ipo_data.issue_date < Time.now()]