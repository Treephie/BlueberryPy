# coding: utf-8
import time
import unittest
from src.utils.config import REPORT_PATH, CASE_PATH, API_CASE_PATH
from src.utils.mail import Mail
from src.utils import utils
from HTMLTestRunner import HTMLTestRunner


suite = unittest.TestSuite()
# suite.addTests(unittest.defaultTestLoader.discover(CASE_PATH, pattern='test_login*.py'))
suite.addTests(unittest.defaultTestLoader.discover(API_CASE_PATH, pattern='test_*.py'))


if __name__ == '__main__':
    tm = time.strftime('%H%M%S', time.localtime(time.time()))
    report = REPORT_PATH + '\\report_%s.html' % tm
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(
                stream=f,
                title=u'自动化测试报告',
                description=u'xxxxxxxxxxxx'
                )
        runner.run(suite)
    report = utils.get_report(REPORT_PATH)
    Mail(attach=report).send()
