# -*- coding: utf-8 -*-
"""
author: ShiinaClariS
time: 2021年8月19日17:06:22
"""
import pandas as pd


class get_excel_data:
    data = pd.DataFrame

    def __init__(self, path):
        try:
            self.data = pd.read_excel(path)
        except Exception as e:
            print(e)

    def get_data_raws(self):
        """
        :return: 按行返回列表
        """
        return self.data.values

    def get_data_keys(self):
        """
        :return: 返回列名列表
        """

        keys = []
        for key in self.data.keys():
            keys.append(key)

        return keys
