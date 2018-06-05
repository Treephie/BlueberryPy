# -*- coding: utf-8 -*-

# ------------------------------------
# file: excel.py
# author: panhui
# time: 2018-06-04 17:00 
# ------------------------------------

import pandas as pd


def get_sheet_data(filename, sheet_name):
    """
    get excl data by sheet, return a dict object.
    :param filename: excl filename
    :param sheet_name: excl sheet name
    :return: row data dict
    """
    excel_data = pd.read_excel(filename, sheet_name=sheet_name)
    return excel_data.to_dict(orient='records')


def get_row_data(filename, sheet_name, row_num=0):
    """
    get excl data by row number, return a dict object.
    :param filename: excl filename
    :param sheet_name: excl sheet name
    :param row_num: row number
    :return: row data dict
    """
    excel_data = pd.read_excel(filename, sheet_name=sheet_name)
    row_data = excel_data.loc[row_num]
    return row_data.to_dict()
