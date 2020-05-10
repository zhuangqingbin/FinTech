import tushare as ts
import pandas as pd
from utils import reduce_mem_usage

def get_stocks_by_concept(*concept):
    """
    :param concept: str, 要查找的概念板块
    :return: 概念板块股票列表
    """
    pro = ts.pro_api()
    concept_map = pro.concept()
    id_list = concept_map[concept_map.name.isin(concept)].code.values.reshape(-1, ).tolist()
    if not id_list:
        return None
    result_df_list = []
    for id in id_list:
        result_df_list.append(pro.concept_detail(id = id))
    return pd.concat(result_df_list, ignore_index = True)[['ts_code','name','concept_name']]

def get_concept_by_stock(ts_code):
    """
    :param ts_code: str, 要查找的股票代码
    :return: 该股票所属的概念板块
    """
    pro = ts.pro_api()
    return pro.concept_detail(ts_code = ts_code)

