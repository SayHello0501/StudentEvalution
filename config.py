# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      PycharmProjects
# FileName:         config.py 
# Author:           袁骏翼
# Email:            
# Datetime:         2022/10/13 17:14
# Description:      系统配置文件
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------

import os
import time

# 区域Saas平台登录地址
host1 = 'http://10.4.3.83/web/isptl/index.html?orgCode=510100#/login'
host2 = 'http://10.20.5.81/web/isptl/index.html?schName=5115020001000#/login'

# 项目路径
DIR_PATH = os.path.dirname(__file__)
# print(DIR_PATH)

# 邮件默认参数
sender = "yuanjunyi001@163.com"  # 发送发邮件地址
receivers = ["yuanjunyi001@163.com"]  # 邮件接收方的邮件地址
mail_host = 'smtp.163.com'  # 163邮箱地址
mail_user = 'yuanjunyi001'  # 用户名
mail_pwd = 'RTQDYGRDYUSTDNDE'  # 密码

now = time.strftime("%Y-%m-%d %H-%m", time.localtime())
# 测试报告存放路径
report_path = DIR_PATH + os.sep + "report" + os.sep + now + "report.html"

# 文件路径
