# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      AreaSaasManage
# FileName:         all_case.py 
# Author:           Administrator
# Email:            
# Datetime:         2022/11/8 9:21
# Description:      所有测试用例运行脚本
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------
from config import DIR_PATH
import os
import unittest


def all_case():
    case_dir = DIR_PATH + os.sep + "Script"

    test_case = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py', top_level_dir=None)

    for test_suite in discover:
        for test_list in test_suite:
            test_case.addTests(test_list)
    return test_case


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_case())
# case_dir = DIR_PATH + os.sep + "Script"
# discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py', top_level_dir=None)
# print(discover)
