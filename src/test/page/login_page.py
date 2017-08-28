# coding: utf-8
from selenium.webdriver.common.by import By
from src.test.common.page import Page


class LoginPage(Page):
    """
    登录页面模型
    """
    url = 'http://mail.163.com'

    login_frame_loc = (By.ID, 'x-URS-iframe')
    username_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.ID, 'dologin')
    assert_name_loc = ()
    error_msg_loc = (By.CLASS_NAME, 'ferrorhead')

    def open(self, maximize_window=True, implicitly_wait=30):
        self.get(self.url, maximize_window, implicitly_wait)

    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def switch_to_login_frame(self):
        self.switch_frame(self.find_element(*self.login_frame_loc))

    def switch_to_default(self):
        self.switch_default()

    def get_error_msg(self):
        return self.find_element(*self.error_msg_loc).text


if __name__ == '__main__':
    login_page = LoginPage()
    login_page.open()
    login_page.quit()

