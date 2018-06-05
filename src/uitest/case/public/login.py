# coding: utf-8


def login(self, username, password):
    """
    登录
    :param self:
    :param username:
    :param password:
    :return:
    """
    self.page.switch_to_login_frame()
    self.page.input_username(username)
    self.page.input_password(password)
    self.page.submit()


def login_error(self, username, password):
    """
    异常登录
    :param self:
    :param username:
    :param password:
    :return: 返回错误提示信息
    """
    self.page.switch_to_login_frame()
    self.page.input_username(username)
    self.page.input_password(password)
    self.page.submit()
    return self.page.get_error_msg()


def logout(self):
    self.page.driver.find_element_by_link_text(u'退出').click()