# coding = utf-8
# /usr/bin/env python

# Author: Jimmy
# Date: 2020-08-29 22:30
import multiprocessing
import sys
import os
import tushare as ts
sys.path.append(os.path.join(os.getcwd(), '..', 'DataProcess'))
sys.path.append(os.path.join(os.getcwd(), '..', 'AutoTools'))
sys.path.append(os.path.join(os.getcwd(), '..', 'DataInput'))
import pickle
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = 'Arial Unicode MS'

import datetime
from DataInput import get_daily_stock
from AutoEmail import ImageEmail
from utils import timer


pro = ts.pro_api()
all_stocks = pro.stock_basic(exchange = '', list_status = 'L')[['ts_code']]
all_stocks = all_stocks.ts_code.apply(lambda x: x.split('.')[0])

def judge_low_pe(ts_code):
    df = get_daily_stock(ts_code = ts_code)[["trade_date", "pe"]]
    return df.pe[0] < np.percentile(df.pe, 10)

with timer("获取低PE股票"):
    STOCKS = []
    for ts_code in all_stocks:
        if judge_low_pe(ts_code):
            STOCKS.append(ts_code)

# 健康股票存储文件夹
STOCKS_DIR = os.path.join(os.getcwd(), '..',
                            'DataStore', 'low_pe_stocks')
if not os.path.exists(STOCKS_DIR):
    os.makedirs(STOCKS_DIR)
with open(os.path.join(os.getcwd(),'..','DataStore','stock_map.pkl'),'rb') as f:
    stock_map = pickle.load(f)

def savePic(stock):
    df = get_daily_stock(ts_code = stock)
    df = df.head(100)
    df['trade_date'] = df['trade_date'].apply(lambda x: datetime.datetime.strptime(x,'%Y%m%d'))
    df = df.set_index('trade_date')
    plt.plot(df.close, 'r-')
    plt.title(stock_map[stock], fontsize = 30)
    plt.axis('off')
    plt.savefig(os.path.join(STOCKS_DIR, stock + '.jpg'), bbox_inches='tight')
    plt.close('all')


with timer("可视化过程"):
    p = multiprocessing.Pool(processes = 2)
    for stock in STOCKS:
        p.apply_async(savePic, args = (stock,))
    p.close()
    p.join()


#发送邮件
socket = ImageEmail('低估值股票')
socket.send(STOCKS_DIR, STOCKS)