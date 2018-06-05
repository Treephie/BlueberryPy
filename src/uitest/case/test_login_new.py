# coding: utf-8
"""
测试登录的各种异常情况
"""
import unittest
from src.uitest.page.login_page import LoginPage
from src.utils.config import DATA_PATH
from src.utils.log import logger
from public import login
import xml.dom.minidom


# 读取测试文件
dom = xml.dom.minidom.parse(DATA_PATH + '/login_data.xml')
root = dom.documentElement


class TestLogin(unittest.TestCase):
    u"""测试登录模块"""
    def setUp(self):
        self.page = LoginPage(browser_type='chrome')
        self.page.open()

    def tearDown(self):
        self.page.quit()

    def test_login_null(self):
        u"""输入用户名和密码均为空"""
        login_info = root.getElementsByTagName('null')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        error_msg = login_info[0].firstChild.data

        text = login.login_error(self, username, password)
        self.assertEqual(text, error_msg)

    def test_login__pwd_null(self):
        u"""输入用户名、密码为空"""
        login_info = root.getElementsByTagName('pwd_null')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        error_msg = login_info[0].firstChild.data

        text = login.login_error(self, username, password)
        self.assertEqual(text, error_msg)

    def test_login__user_null(self):
        u"""输入用户名为空、密码"""
        login_info = root.getElementsByTagName('user_null')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        error_msg = login_info[0].firstChild.data

        text = login.login_error(self, username, password)
        self.assertEqual(text, error_msg)

    def test_login__error(self):
        u"""输入用户名和密码错误"""
        login_info = root.getElementsByTagName('error')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        error_msg = login_info[0].firstChild.data

        text = login.login_error(self, username, password)
        self.assertEqual(text, error_msg)


if __name__ == '__main__':
    unittest.main()
