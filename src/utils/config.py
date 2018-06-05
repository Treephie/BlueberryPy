# coding: utf-8
import ConfigParser
import os


BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..\..')
CONFIG_FILE = BASE_PATH + '\conf\config.ini'
DATA_PATH = BASE_PATH + '\data\\'
DRIVER_PATH = BASE_PATH + '\drivers\\'
LOG_PATH = BASE_PATH + '\logs\\'
REPORT_PATH = BASE_PATH + '\\report\\'
CASE_PATH = BASE_PATH + '\\src\\uitest\case\\'
API_CASE_PATH = BASE_PATH + '\\src\\apitest\\'


class Config:
    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.config.read(CONFIG_FILE)

    def get(self, section, option):
        return self.config.get(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)


if __name__ == '__main__':
    print Config().get('db', 'host')
