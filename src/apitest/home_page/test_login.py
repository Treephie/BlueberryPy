# -*- coding: utf-8 -*-

# ------------------------------------
# file: test_login.py
# author: panhui
# time: 2018-06-05 9:27 
# ------------------------------------

import unittest
from src.utils import excel
from src.utils.config import DATA_PATH
from src.utils.log import logger
from src.utils import reuse_methods

filename = DATA_PATH + 'test_data.xlsx'
sheet_name = 'user_login'
# case_data = excel.get_sheet_data(filename, sheet_name)


class UserLoginTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login_normal(self):
        logger.info('test_login_normal')
        test_data = excel.get_row_data(filename, sheet_name, 0)
        resp = reuse_methods.request(test_data['Method'], test_data['Url'], test_data['Data'])
        self.assertEqual(resp.content.decode('utf-8'), test_data['Response'])

    def test_login_pwWrong(self):
        logger.info('test_login_pwWrong')
        test_data = excel.get_row_data(filename, sheet_name, 1)
        resp = reuse_methods.request(test_data['Method'], test_data['Url'], test_data['Data'])
        self.assertEqual(resp.content.decode('utf-8'), test_data['Response'])

if __name__ == '__main__':
    unittest.main()
