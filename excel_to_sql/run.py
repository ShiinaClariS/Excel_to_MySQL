# -*- coding: utf-8 -*-
"""
author: ShiinaClariS
time: 2021年8月25日17:19:30
"""

from sql.conn import mysql_conn
from excel.Excel import get_excel_data
import time


if __name__ == '__main__':
    data = get_excel_data(r'W:\workspace\label_to_sql\ExcelFile\标签汇总.xlsx')
    mysql = mysql_conn(host='127.0.0.1', port=3306, user='root', pw='tqf1234321fqt', db='test')
    # print(data.get_data_raws())
    # print(data.get_data_keys())
    # for raw in data.get_data_raws():
    #     mysql.sql_insert(table='test_table', colunms=data.get_data_keys(), raw=raw)
    data.replace(key_name='分类名称', text={'特': '游戏'})
    data_raws = data.get_data_by_raws(500)
    # print(data_raws)
    i = 1
    start = time.time()
    for raws in data_raws:
        # print(raws)
        spend_time = mysql.sql_insert(table='test_table', colunms=['classify_name', 'label', 'label_code'], raws=raws)
        print('第', i, '次写入完成, 用时:', spend_time)
        i += 1
    end = time.time()
    print('写入结束，总用时:', end - start)

# 1   7.8937
# 10  0.8867
# 20  0.5381
# 50  0.2201
# 100 0.0961
# 500 0.0431
