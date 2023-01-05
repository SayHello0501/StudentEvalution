# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      AreaSaasManage
# FileName:         __init__.py.py 
# Author:           Administrator
# Email:            
# Datetime:         2023/1/4 17:06
# Description:      
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------

from selenium.webdriver.common.by import By

# 账户名
input_username = By.XPATH, '//*[@placeholder="请输入账户"]'
# 密码
input_pwd = By.XPATH, '//*[@placeholder="请输入密码"]'
# 登录按钮
click_login = By.XPATH, '//*[@type="button"]'
