# coding: utf-8
"""
测试发送邮件
"""
import unittest
import xml.dom.minidom
from time import sleep

from po.mail_po import MailPage
from selenium import webdriver

from src.uitest.case.public import login

# 读取测试文件
dom = xml.dom.minidom.parse('../data/login_data.xml')
root = dom.documentElement


class TestSendMail(unittest.TestCase):
    u"""测试发送邮件"""
    def setUp(self):
        options = self.driver = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)
        self.base_url = root.getElementsByTagName('url')[0].firstChild.data

    def test_send1(self):
        u"""只输入收信人发送"""
        # 登录
        login_info = root.getElementsByTagName('normal')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        login.login(self, username, password)
        # 写信
        mail_page = MailPage(self.driver)
        mail_page.click_button_write()
        mail_page.input_input_receiver('838927564@qq.com')
        mail_page.click_button_send()
        mail_page.click_button_send_confirm()

        text = mail_page.get_assert_msg()
        self.assertIn(u'发送成功', text)

        # 退出
        login.logout(self)

    def test_send2(self):
        u"""输入收信人、主题、正文、附件发送"""
        # 登录
        login_info = root.getElementsByTagName('normal')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        login.login(self, username, password)
        # 写信
        mail_page = MailPage(self.driver)
        mail_page.click_button_write()
        mail_page.input_input_receiver('838927564@qq.com')
        mail_page.input_input_mail_title(u'自动发送的主题')
        mail_page.switch_to_mail_frame()
        mail_page.input_input_mail_body(u'自动发送的正文内容，啊哈哈哈哈哈')
        mail_page.switch_to_default()
        mail_page.input_input_attach('F://attach.txt')
        mail_page.click_button_send()
        sleep(3)
        text = mail_page.get_assert_msg()
        self.assertIn(u'发送成功', text)

        # 退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
