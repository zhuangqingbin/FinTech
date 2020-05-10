# coding = utf-8
# /usr/bin/env python

# Author: Jimmy
# Date: 2020-05-08 17:03

import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..', 'DataInput'))
from dailyStock import get_daily_stock

df = get_daily_stock(date='20200508')
print(df)