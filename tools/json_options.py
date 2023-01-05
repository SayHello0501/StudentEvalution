# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      PycharmProjects
# FileName:         json_options.py 
# Author:           袁骏翼
# Email:            
# Datetime:         2022/10/17 9:15
# Description:      
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------
import json
import os
from config import DIR_PATH


# 读取json文件
def read_json(folder, filename, key):
    file_path = DIR_PATH + os.sep + "data" + os.sep + folder + os.sep + filename
    list_data = []
    with open(file_path, 'r', encoding="utf-8") as f:
        for data in json.load(f).get(key):
            list_data.append(tuple(data.values())[1:])
        return list_data


# 读取json文件
def read_api_json(folder, filename, key):
    file_path = DIR_PATH + os.sep + "data" + os.sep + folder + os.sep + filename
    list_data = []
    with open(file_path, 'r', encoding="utf-8") as f:
        for data in json.load(f).get(key):
            list_data.append(tuple(data.values()))
        return list_data


# 写入json文件
def write_json():
    pass


if __name__ == '__main__':
    print(read_api_json("api_data", "test_get_all_app_list.json", "get_all_app_list"))
