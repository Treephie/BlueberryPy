# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from page import Page


class MailPage(Page):
    """邮件页面"""
    url = ''

    frame_mail = (By.CLASS_NAME, "APP-editor-iframe")
    button_write = (By.XPATH, "//div[@id='dvNavTop']/ul/li[2]")  # 写信按钮
    button_send = (By.XPATH, "//header[@class='frame-main-cont-head']//span[@class='nui-btn-text']")  # 发送按钮
    button_send_confirm = (By.CSS_SELECTOR, ".nui-msgbox-ft-btns>div>span")  # 发送确认按钮
    input_receiver = (By.CLASS_NAME, 'nui-editableAddr-ipt')  # 收件人
    input_mail_title = (By.XPATH, "//input[@class='nui-ipt-input' and @maxlength='256']")  # 邮件主题
    input_mail_body = (By.XPATH, "//body[@class='nui-scroll']")  # 邮件正文
    input_attach = (By.XPATH, "//input[@type='file']")  # 邮件附件
    assert_msg = (By.CLASS_NAME, "tK1")  # 验证的信息

    def switch_to_mail_frame(self):
        self.switch_frame(self.find_element(*self.frame_mail))

    def switch_to_default(self):
        self.switch_default()

    def click_button_write(self):
        self.find_element(*self.button_write).click()

    def click_button_send_confirm(self):
        self.find_element(*self.button_send_confirm).click()

    def click_button_send(self):
        self.find_element(*self.button_send).click()

    def input_input_receiver(self, receiver):
        self.find_element(*self.input_receiver).send_keys(receiver)

    def input_input_mail_title(self, mail_title):
        self.find_element(*self.input_mail_title).send_keys(mail_title)

    def input_input_mail_body(self, mail_body):
        self.find_element(*self.input_mail_body).send_keys(mail_body)

    def input_input_attach(self, attach):
        self.find_element(*self.input_attach).send_keys(attach)

    def get_assert_msg(self):
        return self.get_text(*self.assert_msg)

