# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      AreaSaasManage
# FileName:         api_base.py 
# Author:           Administrator
# Email:            
# Datetime:         2022/11/8 14:32
# Description:      接口登录方法
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------

import requests


class ApiLogin(object):

    # 定义登录接口
    @classmethod
    def api_login(cls, json_data):
        url = "http://10.4.3.77/service/isptlarea/open/sso/login"
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "appId": "JF-ISWCC-WEB",
            "appToken": "05bd91d386acfbd64b97e23da56851e121040dd42dc50bfa7768dc3f3e4df84bc28f3f6e7e9c48862081e7d6b8b4701e2ed0bf7fe4efeab50d6021855cbdea96",
            "orgCode": "area001",
            "timeStamp": "1668477030876"
        }
        resp = requests.request("POST", headers=header, json=json_data, url=url)
        # print(resp.json().get("code"))
        # print(resp.status_code)
        return resp


if __name__ == '__main__':
    json_data = {
        "loginType": "1",
        "accountName": "area001",
        "password": "268d4985f96e3984631037c49bd247868142698246bac64163f86714b9b2edc2",
        "mobile": "13628146725",
        "verifyCode": "",
        "personId": ""
    }
    ApiLogin.api_login(json_data)
