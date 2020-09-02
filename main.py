# test
import sys
import os
import tushare as ts
sys.path.append(os.path.join(os.getcwd(), 'DataProcess'))
sys.path.append(os.path.join(os.getcwd(), 'AutoTools'))
sys.path.append(os.path.join(os.getcwd(), 'DataInput'))

from dailyStock import get_daily_stock
import matplotlib.pyplot as plt
import datetime
from config import STOCKS

from dailyAnalysis import t


df = get_daily_stock(ts_code = STOCKS[0])


def savePic(data):
    df = data.copy()
    df['trade_date'] = df['trade_date'].apply(lambda x: datetime.datetime.strptime(x,'%Y%m%d'))
    plt.plot(df.close, 'r-')
    plt.savefig('p.jpg')

