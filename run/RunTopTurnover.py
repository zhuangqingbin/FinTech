# coding = utf-8
# /usr/bin/env python

# Author: Jimmy
# Date: 2020-06-18 11:58

import sys
import os
import tushare as ts
sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append(os.path.join(os.getcwd(), '..', 'DataProcess'))
sys.path.append(os.path.join(os.getcwd(), '..', 'AutoTools'))
sys.path.append(os.path.join(os.getcwd(), '..', 'DataInput'))

from AutoEmail import TextEmail
from utils import parse_data
from utils import Time



today = Time.ex_now()
pro = ts.pro_api()

dfSH = pro.hsgt_top10(trade_date = today, market_type='1',
        fields = ['name', 'rank', 'amount', 'net_amount', 'buy', 'sell'])
dfSH = dfSH.sort_values('rank').drop(['rank'], axis = 1).\
        reset_index(drop = True)

dfSZ = pro.hsgt_top10(trade_date = today, market_type='3',
        fields = ['name', 'rank', 'amount', 'net_amount', 'buy', 'sell'])
dfSZ = dfSZ.sort_values('rank').drop(['rank'], axis = 1).\
        reset_index(drop = True)


msg = parse_data(dfSH, '沪股通{}月{}日前十大成交详细数据'.\
                 format(int(today[4:6]), int(today[-2:])))
msg += '<br><br>'
msg += parse_data(dfSZ, '深股通{}月{}日前十大成交详细数据'.\
                 format(int(today[4:6]), int(today[-2:])))


# 发送邮件
socket = TextEmail('沪深股通前十大成交详细数据')
socket.send(msg)




