import pickle
import os
from utils import Time
import tushare as ts
RECORD_FILE = os.path.join(os.getcwd(), '..', 'DataStore', 'record.pkl')


hot_money = {
    'zhao': ['中国银河证券股份有限公司绍兴证券营业部', '华泰证券股份有限公司浙江分公司',
             '中国银河证券股份有限公司北京阜成路证券营业部'],
    'good': ['银泰证券有限责任公司上海嘉善路证券营业部', '长江证券股份有限公司上海世纪大道证券营业部',
             '海通证券股份有限公司上虞市民大道证券营业部']
             }


df = pro.top_inst(trade_date='20190815')
df_zhao = df[df.exalter.isin(hot_money['zhao'])]

def dump_record():
    """
    :return: 存储本次获取数据的日期信息、之后15天的开市日期
            存放于DataStore中
    """
    record_info_dict = {}
    record_info_dict['now'] = Time.now()

    pro = ts.pro_api()
    record_info_dict['open'] = list(pro.trade_cal(exchange='', start_date=Time.now(),
                  end_date=Time.delta(15), is_open='1').cal_date)

    with open(RECORD_FILE, 'wb') as fw:
        pickle.dump(record_info_dict, fw)

def load_record():
    """
    :return: 读取DataStore中的record信息，返回上一次存储的信息
    """
    if not os.path.exists(RECORD_FILE):
        raise FileNotFoundError("%s not found." % RECORD_FILE)
    with open(RECORD_FILE, 'rb') as fr:
        record_info_dict = pickle.load(fr)
    return

