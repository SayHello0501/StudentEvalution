# -*- coding: utf-8 -*-
# @Time : 2022/10/12 13:29
# @Author : 袁骏翼
# @File : get_log.py

import logging.handlers
import os
import time

from config import DIR_PATH


class GetLog:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 创建日志对象
            cls.logger = logging.getLogger()
            # 设置日志级别
            cls.logger.setLevel(logging.INFO)
            # 设置日志颜色
            log_color_config = {
                # 终端输出日志颜色配置
                'DEBUG': 'white',
                'INFO': 'cyan',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            }
            # 写入日志
            now = time.strftime("%Y-%m-%d %H-%m", time.localtime())
            th = logging.handlers.TimedRotatingFileHandler(
                filename=DIR_PATH + os.sep + "log" + os.sep + now + "log.log",
                when="midnight",
                interval=1,
                backupCount=30,
                encoding='utf-8'
            )
            # 创建一个日志handler，将日志输出到控制台
            ch = logging.StreamHandler()
            # 设置日志打印格式
            fmt = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-Line:%(lineno)d-Message:%(message)s")
            # 给日志控制器添加格式
            # 控制台
            # ch.setFormatter(fmt)
            # 日志文件
            th.setFormatter(fmt)
            # 将处理器添加到日志器
            # cls.logger.addHandler(ch)
            cls.logger.addHandler(th)
        return cls.logger


if __name__ == '__main__':
    gt = GetLog.get_logger()
    gt.info("info信息被执行")
    gt.info("error信息被执行")
