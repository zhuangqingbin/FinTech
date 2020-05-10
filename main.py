# test
import sys
import os
import tushare as ts
sys.path.append(os.path.join(os.getcwd(), 'DataProcess'))
sys.path.append(os.path.join(os.getcwd(), 'AutoTools'))
sys.path.append(os.path.join(os.getcwd(), 'DataInput'))

from AutoEmail import LimitUp
from utils import parse_data
from utils import Time


pro = ts.pro_api()


dfSH = pro.hsgt_top10(trade_date='20200508', market_type='1',
        fields = ['name', 'rank', 'amount', 'net_amount', 'buy', 'sell'])
dfSH = dfSH.sort_values('rank').drop(['rank'], axis = 1).\
        reset_index(drop = True)

dfSZ = pro.hsgt_top10(trade_date='20200508', market_type='3',
        fields = ['name', 'rank', 'amount', 'net_amount', 'buy', 'sell'])
dfSZ = dfSZ.sort_values('rank').drop(['rank'], axis = 1).\
        reset_index(drop = True)

today = Time.now()
msg = parse_data(dfSH, '沪股通{}月{}日前十大成交详细数据'.\
                 format(int('05'), int('08')))
msg += '<br><br>'
msg += parse_data(dfSZ, '深股通{}月{}日前十大成交详细数据'.\
                 format(int('05'), int('08')))

socket = LimitUp()
socket.send(msg)
