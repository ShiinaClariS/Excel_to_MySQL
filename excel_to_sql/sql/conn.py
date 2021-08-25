# -*- coding: utf-8 -*-
"""
author: ShiinaClariS
time: 2021年8月25日17:18:11
"""

import pymysql
import pandas as pd
import time


class mysql_conn:

    def __init__(self, host, port, user, db, pw):
        self.host = host
        self.port = port
        self.user = user
        self.db = db
        self.pw = pw

    def get_conn_cur(self):
        conn, cur = None, None
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.pw,
                                   database=self.db)
            cur = conn.cursor()
            # print('Connect Success')
        except Exception as e:
            print(e)

        return conn, cur

    def sql_insert(self, table, colunms, raws):
        """
        :param table: 表名
        :param colunms: 列名
        :param raw: 要插入的一条数据
        :return:
        """

        conn, cur = self.get_conn_cur()
        col = ""
        val = ""
        start = time.time()

        # insert into table(``,``,``...) values('','',int,...)
        for colunm in colunms:
            col = col + '`' + colunm + '`,'
        col = col.strip(',')
        # print(col)

        for raw in raws:
            for value in raw:
                if pd.isnull(value) is True:
                    val = val + 'null,'
                else:
                    if isinstance(value, int) or isinstance(value, float):
                        val = val + str(int(value)) + ','
                    else:
                        val = val + '"' + str(value) + '",'
            val = val.strip(',') + '),\n('
            # print(val)

        val = val.strip('),\n(')
        sql = "insert into " + table + "(" + col + ") values(" + val + ");"

        print(sql)
        self.execute_(sql, conn, cur)
        end = time.time()

        self.close_(conn, cur)
        return end - start

    def sql_update(self, table, colunms, raw):
        """
        :param table: 表名 type:str
        :param colunms: 列名 type:list
        :param raw: 要更改的一条数据
        :return:
        """

        conn, cur = self.get_conn_cur()
        update = ''

        # update table set colunm = value where colunm = value
        for colunm, value in zip(colunms, raw):
            if pd.isnull(value) is True:
                update = update + colunm + ' = null,'
            else:
                if isinstance(value, int) or isinstance(value, float):
                    update = update + colunm + ' = ' + str(int(value)) + ','
                else:
                    update = update + colunm + " = '" + str(value) + "',"

        update.strip(',')

        whe = colunms[0] + ' = ' + str(raw[0])
        sql = "update " + table + " set " + update + " where " + whe
        self.execute_(sql, conn, cur)
        self.close_(conn, cur)
        # return sql

    # def sql_delete(self, table):
    #     # delete from table where ..=..
    #     delete = 'delete from ' + table + ' where '
    #
    #     pass

    def check_repeat(self, table, name):
        """
        :param table:
        :param id:
        :return:
        """
        conn, cur = self.get_conn_cur()

        sql = 'select * from ' + table
        self.execute_(sql, conn, cur)
        self.close_(conn, cur)

        result = cur.fetchall()
        if name not in result:
            return False
        else:
            return True

    def execute_(self, sql, conn, cur):
        cur.execute(sql)
        conn.commit()
        print('执行成功')

    def close_(self, conn, cur):
        cur.close()
        conn.close()
        # print('连接关闭')


# mysql = mysql_conn(host='39.105.243.180', port=3306, user='appstore', pw='2E5484FF0E1EF36E74FC4D06', db='pc_store')
mysql = mysql_conn(host='127.0.0.1', port=3306, user='root', pw='tqf1234321fqt', db='test')
# data = pd.read_excel(r'W:\workspace\label_to_sql\sql\input\test.xlsx')
# colunms = data.keys()
# raw = data.values[0]
# mysql.sql_insert(table='test_table', colunms=colunms, raw=raw)
# print(mysql.sql_update(table='test_table', colunms=colunms, raw=raw))
