from datetime import timedelta, datetime
import time
from contextlib import contextmanager
import numpy as np
import tushare as ts

import pandas as pd
import tushare as ts
import pickle
import os
TOCKEN = "64ce1845b91d06f579525db6e53d497b1c513174331f5509320f4bd5"



class Time:
    @staticmethod
    def delta(diff, hour = False):
        target = datetime.now() + timedelta(diff)
        if hour:
            return target.strftime("%Y%m%d %H:%M:%S")
        else:
            return target.strftime("%Y%m%d")

    @staticmethod
    def now(detail = False):
        if detail:
            return datetime.now().strftime("%Y%m%d %H:%M:%S")
        else:
            return datetime.now().strftime("%Y%m%d")

    @staticmethod
    def ex_now(detail = False):
        ts.set_token(TOCKEN)
        pro = ts.pro_api()
        df = pro.trade_cal(exchange = '', start_date = Time.delta(-7),
                           end_date = Time.now())
        for i in range(len(df)):
            if df.iloc[-i]['is_open'] == 1:
                result =  df.iloc[-i]['cal_date']
                break
        if detail:
            return datetime.strptime(result,"%Y%m%d").\
                        strftime("%Y%m%d %H:%M:%S")
        else:
            return result


@contextmanager
def timer(title):
    '''
    Examples
    --------
    >>> with timer("Program name"):
            time.sleep(3)
    '''
    start_time = time.time()
    print('{:-^50}'.format(' ' + title + ' '))
    yield
    elapsed_time = time.time() - start_time
    print('{:-^50}'.format(' {:.0f}s elapsed '.format(elapsed_time)))


def reduce_mem_usage(data, verbose=True):
    start_mem = data.memory_usage().sum() / 1024 ** 2
    if verbose:
        print('Memory usage of dataframe: {:.2f} MB'.format(start_mem))

    for col in data.columns:
        col_type = data[col].dtype

        if str(col_type)[:3] == 'int':
            c_min = data[col].min()
            c_max = data[col].max()
            if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                data[col] = data[col].astype(np.int8)
            elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                data[col] = data[col].astype(np.int16)
            elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                data[col] = data[col].astype(np.int32)
            elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                data[col] = data[col].astype(np.int64)

        elif str(col_type)[:5] == 'float':
            c_min = data[col].min()
            c_max = data[col].max()
            if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                data[col] = data[col].astype(np.float16)
            elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                data[col] = data[col].astype(np.float32)
            else:
                data[col] = data[col].astype(np.float64)

        else:
            pass

    end_mem = data.memory_usage().sum() / 1024 ** 2
    if verbose:
        print('Memory usage after optimization: {:.2f} MB'.format(end_mem))
        print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return data



def parse_row(row, header, color = None):
    result = '<tr>'
    if header:
        normal_format = '<th> {} </th>'
    else:
        normal_format = '<th><p style="color:%s;"> {} </p></th>' % color
    i = 0
    while i < len(row):
        if type(row[i]) == str:
            result += normal_format.format(row[i])
        else:
            result += normal_format.format('{:.2e}'.format(row[i]))
        i += 1
    result += '</tr>'
    return result

def parse_data(data, title):
    result = '<div>'
    result += '<table border="1">'
    result += '<caption><font size = "5" color = "red" > {} </font></caption>'.format(title)

    result += parse_row(data.columns, header=True)
    for index, value in data.iterrows():
        color = 'red' if value[2] > 0 else 'green'
        result += parse_row(value, header=False,
                            color=color)

    result += '</table>\n</div>'
    return result