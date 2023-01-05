# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      AreaSaasManage
# FileName:         get_headers.py 
# Author:           Administrator
# Email:            
# Datetime:         2022/11/16 17:02
# Description:      获取请求头方法
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------

import requests


def get_headers():
    url = "http://10.4.3.77/service/isptlarea/open/sso/login"
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "appId": "JF-ISWCC-WEB",
        "appToken": "8470b0b0b9351089feeeeee5ff16512f9567f8f02b9922f1d15288a7726a104e862f43c5554013d19fddb4d66fc3b6b62c0af39ad78f38b54d2572d994d6b022",
        "orgCode": "area002",
        "timeStamp": "1669101912033"
    }
    body = {
        "loginType": "1",
        "accountName": "area002",
        "password": "268d4985f96e3984631037c49bd247868142698246bac64163f86714b9b2edc2",
        "mobile": "13628146725",
        "verifyCode": "",
        "personId": ""
    }
    resp = requests.request("POST", headers=header, json=body, url=url)
    # 获取token
    token = resp.json().get("data").get("token")
    header = {"Content-Type": "application/json;charset=UTF-8", "devType": "1", "orgCode": "area002", "token": token}
    # print(token)
    # print(header)
    return header


if __name__ == '__main__':
    get_headers()
