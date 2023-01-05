# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      PycharmProjects
# FileName:         get_time.py 
# Author:           袁骏翼
# Email:            
# Datetime:         2022/10/19 13:16
# Description:      获取时间模块
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------
import datetime


class GetTime:

    def get_start_time(self):
        end_time = datetime.datetime.now()
        st = end_time + datetime.timedelta(days=-1)
        start_time = st.strftime('%Y-%m-%d')
        return start_time

    def get_end_time(self):
        et = datetime.datetime.now()
        end_time = et.strftime('%Y-%m-%d')
        return end_time


if __name__ == '__main__':
    gt = GetTime()
    gt.get_start_time()
    gt.get_end_time()
