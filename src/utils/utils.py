# coding: utf-8
import os


def get_report(file_dir):
    """
    在报告目录下获取最新生成的测试报告
    :param file_dir: 测试报告的路径
    :return: 最新的报告文件路径
    """
    # print file_dir
    lists = os.listdir(file_dir)
    lists = [x for x in lists if os.path.isfile(os.path.join(file_dir, x))]
    lists.sort()
    return os.path.join(file_dir, lists[-1])
