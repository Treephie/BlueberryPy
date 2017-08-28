# coding: utf-8
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from config import Config, LOG_PATH


CONFIG = Config()

LOGGING_FILENAME = CONFIG.get('logging', 'filename')
LOGGING_SUFFIX = CONFIG.get('logging', 'suffix')
LOGGING_WHEN = CONFIG.get('logging', 'when')
LOGGING_INTERVAL = CONFIG.getint('logging', 'interval')
LOGGING_BACKUPCOUNT = CONFIG.getint('logging', 'backupcount')
LOGGING_DATEFMT = CONFIG.get('logging', 'datefmt')
LOGGING_FMT = CONFIG.get('logging', 'fmt')


# 初始化日志对象
def init_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # 设置控制台输出
    consolehandler = logging.StreamHandler()
    consolehandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(LOGGING_FMT)
    consolehandler.setFormatter(formatter)
    logger.addHandler(consolehandler)
    # 设置日志文件输出
    # 日志文件所在的目录
    filename_directory = LOG_PATH
    # 创建日志文件目录
    if not os.path.exists(filename_directory):
        os.makedirs(filename_directory)
    filename = os.path.join(filename_directory, LOGGING_FILENAME)
    filehandler = TimedRotatingFileHandler(filename, when=LOGGING_WHEN, interval=LOGGING_INTERVAL, backupCount=LOGGING_BACKUPCOUNT)
    filehandler.setLevel(logging.INFO)
    filehandler.suffix = LOGGING_SUFFIX
    formatter = logging.Formatter(fmt=LOGGING_FMT, datefmt=LOGGING_DATEFMT)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger


logger = init_logger()
