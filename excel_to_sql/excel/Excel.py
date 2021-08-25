# -*- coding: utf-8 -*-
"""
author: ShiinaClariS
time: 2021年8月25日17:17:30
"""
import pandas as pd


class get_excel_data:
    data = pd.DataFrame

    def __init__(self, path):
        try:
            self.data = pd.read_excel(path)
        except Exception as e:
            print(e)

    def get_data_by_raws(self, raws_size):
        """
        将多行数据合成子列表，最后返回包含全部数据的列表
        :param raws_size: 子列表中数据行数
        :return: all data
        """
        values = self.data.values
        length = len(values)
        raws = length // raws_size
        new_values = []

        if raws_size > length:
            first, last = 0, length
        else:
            first, last = 0, raws_size

        if length % raws_size != 0:
            raws += 1

        for i in range(raws):
            tem1 = []
            for raw in range(first, last):
                tem2 = []
                for j in values[raw]:
                    tem2.append(j)
                tem1.append(tem2)
            new_values.append(tem1)
            first, last = first + raws_size, last + raws_size
            if last > length:
                last = length

        return new_values

    def get_data_keys(self):
        """
        :return: 返回列名列表
        """
        keys = []
        for key in self.data.keys():
            keys.append(key)

        return keys

    def replace(self, key_name, text):
        """
        :param data:
        :param key_name: the name of colunm
        :param text: like {'a': 'b', 'c': 'd'}, keys is str that should be replaced, values is str that should replace to
        :return: None
        """
        # text = {'a': 'b', 'c': 'd'}
        count = 0
        for i in self.data.loc[:][key_name]:
            for k, v in zip(text.keys(), text.values()):
                if i.__contains__(k):
                    self.data.loc[count][key_name] = v
            count += 1
