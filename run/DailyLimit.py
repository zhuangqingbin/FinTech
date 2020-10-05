# coding = utf-8
# /usr/bin/env python

# Author: Jimmy
# Date: 2020-08-29 22:30
import multiprocessing
import sys
import os
import tushare as ts
sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append(os.path.join(os.getcwd(), '..', 'DataProcess'))
sys.path.append(os.path.join(os.getcwd(), '..', 'AutoTools'))
sys.path.append(os.path.join(os.getcwd(), '..', 'DataInput'))
import pickle
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# plt.rcParams["font.family"] = 'Arial Unicode MS'
plt.rcParams["font.sans-serif"] = 'SimHei'

import datetime
from DataInput import get_daily_stock
from AutoEmail import TextEmail
from utils import timer
from utils import Time

today = Time.ex_now()
pro = ts.pro_api()
limit_up = pro.limit_list(trade_date = today, limit_type = 'U')
limit_down = pro.limit_list(trade_date = today, limit_type = 'D')

content_html = '''
    <style>
        th {
           background-color:#1565C0;
           color: #E1F5FE;
           border-bottom-width: 0;
           padding: 5px 10px;
           font-size: 16px;
           font-family:Georgia;
           font-weight: bold;
           width:200px;
        }
        td {
           color: #000;
           font-family:Times;
           font-size: 13px;
           border-width: 1px;
           border-style: dashed;
           border-color:#FAFAFA;
           width:120px;
           height:35px;
        }
    </style>
    '''

def get_table_html(data, title):
    def valuFormat(x, type):
        if type == 'percent':
            return '{:.2f}%'.format(x)
        elif type == 'int':
            return '{}'.format(int(x))
        elif type == 'float':
            return '{:.2f}'.format(x)
        elif type == 'E':
            return '{:.2E}'.format(x)
        else:
            return ''

    def addHref(row):
        href_format = "<a href = 'http://quote.eastmoney.com/%s.html'>%s</a>"
        if row['ts_code'].endswith('SH'):
            code = 'sh' + row['ts_code'].split('.')[0]
        else:
            code = 'sz' + row['ts_code'].split('.')[0]
        return href_format % (code, row['name'])

    table_html = '''<font size="4em"><b>%s</b></font>''' % title
    table_html += '''
        <table>
               <tr style="background:#2196F3; color:white; align:center;font-size:1.25em">
                <th style="width:50px; align:center">证券</th>
                <th style="width:100px">振幅</th>
                <th style="width:100px">封单金额</th>
                <th style="width:100px">打开次数</th>
                <th style="width:100px">强度</th>
               </tr>'''
    for index, row in data.iterrows():
        color = '#E1F5FE' if index % 2 == 0 else '#FAFAFA'
        row_html = '''<tr style="background:%s; color:black; align:center;">''' % (color)
        si = '''<td>%s</td>
                <td align="right">%s</td>
                <td align="center">%s</td>
                <td align="center">%s</td>
                <td align="center">%s</td>
            ''' % (addHref(row), valuFormat(row['amp'],'percent'), valuFormat(row['fd_amount'],'E'),
                   valuFormat(row['open_times'],'int'), valuFormat(row['strth'],'float'))
        row_html += si
        row_html += '''</tr>'''
        table_html += row_html.strip()
    table_html += '</table>'
    return table_html

content_html += get_table_html(limit_up, '{}月{}日涨停股票'.\
                        format(int(today[4:6]), int(today[-2:])))
content_html += get_table_html(limit_down, '{}月{}日跌停股票'.\
                        format(int(today[4:6]), int(today[-2:])))

# 发送邮件
socket = TextEmail('{}月{}日涨跌停股票汇总'.\
                    format(int(today[4:6]), int(today[-2:])))
socket.send(content_html)