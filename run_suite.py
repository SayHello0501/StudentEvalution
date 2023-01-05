# -*- coding: utf-8 -*-
# @Time : 2022/10/12 15:06
# @Author : 袁骏翼
# @File : run_suite.py
import time
import unittest

from tools.HTMLTestRunner import HTMLTestRunner
from config import report_path, DIR_PATH
from tools import send_email
import os


def run_suite():
    suite = unittest.defaultTestLoader.discover("./Script/web_case", pattern="test_*.py")
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(stream=fp, title="区域Saas平台测试报告", description="区域Saas平台测试报告", verbosity=9)
    runner.run(suite)


if __name__ == '__main__':
    run_suite()
    # send_email.send_email()
