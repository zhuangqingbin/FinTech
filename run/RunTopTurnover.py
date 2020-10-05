# coding = utf-8
# /usr/bin/env python

# Author: Jimmy
# Date: 2020-06-18 11:58

import sys
import os
import tushare as ts
import numpy as np
sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append(os.path.join(os.getcwd(), '..', 'DataProcess'))
sys.path.append(os.path.join(os.getcwd(), '..', 'AutoTools'))
sys.path.append(os.path.join(os.getcwd(), '..', 'DataInput'))

from AutoEmail import TextEmail
from utils import parse_data
from utils import Time
import pickle



today = Time.ex_now()

pro = ts.pro_api()
with open(os.path.join(os.getcwd(),'..','DataStore','stock_map.pkl'),'rb') as f:
    stock_map = pickle.load(f)


dfSH = pro.hsgt_top10(trade_date = today, market_type='1',
        fields = 'ts_code,name,rank,amount,net_amount,buy,sell')
dfSH = dfSH.sort_values('rank').drop(['rank'], axis = 1).\
        reset_index(drop = True)

dfSZ = pro.hsgt_top10(trade_date = today, market_type='3',
        fields = 'ts_code,name,rank,amount,net_amount,buy,sell')
dfSZ = dfSZ.sort_values('rank').drop(['rank'], axis = 1).\
        reset_index(drop = True)

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
    def colorMap(x):
        a = np.double(x)
        if a > 0:
            c = 'red'
        elif a < 0:
            c = 'green'
        else:
            c = 'black'
        s = '<font color="%s">%s</font>' % (c, a)
        return s

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
                <th style="width:100px">交易量</th>
                <th style="width:100px">净交易额</th>
                <th style="width:100px">买量</th>
                <th style="width:100px">卖量</th>
               </tr>'''
    for index, row in data.iterrows():
        color = '#E1F5FE' if index % 2 == 0 else '#FAFAFA'
        row_html = '''<tr style="background:%s; color:black; align:center;">''' % (color)
        si = '''<td>%s</td>
                <td align="right">%s</td>
                <td align="center">%s</td>
                <td align="center">%s</td>
                <td align="center">%s</td>
            ''' % (addHref(row), colorMap(row['amount']), colorMap(row['net_amount']),
                   colorMap(row['buy']), colorMap(row['sell']))
        row_html += si
        row_html += '''</tr>'''
        table_html += row_html.strip()
    table_html += '</table>'
    return table_html

content_html += get_table_html(dfSH, '沪股通{}月{}日前十大成交详细数据'.\
                        format(int(today[4:6]), int(today[-2:])))
content_html += get_table_html(dfSZ, '深股通{}月{}日前十大成交详细数据'.\
                        format(int(today[4:6]), int(today[-2:])))

# 发送邮件
socket = TextEmail('沪深股通前十大成交详细数据')
socket.send(content_html)




