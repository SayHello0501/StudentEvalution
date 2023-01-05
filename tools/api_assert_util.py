# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      AreaSaasManage
# FileName:         api_assert_util.py 
# Author:           Administrator
# Email:            
# Datetime:         2022/11/17 15:53
# Description:      接口断言方法
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------

def assert_util(resp, code, result, message):
    assert code == resp.json().get("code")
    assert result == resp.json().get("result")
    assert message in resp.json().get("message")
