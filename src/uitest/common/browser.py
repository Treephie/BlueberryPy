# coding: utf-8
from selenium import webdriver
from src.utils.config import DRIVER_PATH, REPORT_PATH
from src.utils.log import logger
import time
import os


CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'

BROWSER_TYPE = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'geckodriver', 'chrome': CHROMEDRIVER_PATH, 'phantomjs': PHANTOMJSDRIVER_PATH}


class Browser(object):
    def __init__(self, browser_type='firefox'):
        self.browser = None
        self.driver = None
        self._type = browser_type.lower()
        if self._type in BROWSER_TYPE:
            self.browser = BROWSER_TYPE[self._type]
        else:
            logger.info('不支持的浏览器类型%s！仅支持%s' % (self._type, ','.join(BROWSER_TYPE.keys())))

    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    driver = Browser('chrome')
    driver.get('http://www.baidu.com')
    driver.save_screen_shot()
    driver.quit()
