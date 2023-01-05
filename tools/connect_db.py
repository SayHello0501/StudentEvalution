# coding=utf-8
# -----------------------------------------------------------------
# ProjectName:      AreaSaasManage
# FileName:         connect_db.py 
# Author:           Administrator
# Email:            
# Datetime:         2022/10/22 15:50
# Description:      连接数据库
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，常量大写
# -----------------------------------------------------------------


import pymysql


class ConnectDatabase:

    @classmethod
    def connect_db(cls, user, password, host, database, sql):
        # 创建数据库连接
        db = pymysql.connect(user=user, password=password, host=host, database=database, charset="utf8", port=3306)
        # 创建游标
        cursor = db.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute(sql)
        # 使用 fetchone() 方法获取单条数据.
        result = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
        print(result)
        return result

    @classmethod
    def get_db_result(cls, user, password, host, database, sql):
        list_result = []
        for i in cls.connect_db(user, password, host, database, sql):
            print(i)
            for j in i:
                list_result.append(j)
            print(list_result[0])
            return list_result[0]


ConnectDatabase.get_db_result(user="root",
                              password="Jf@123csb",
                              host="10.4.3.66",
                              database="jf_isbmp_area",
                              sql="""
                                  SELECT count(*) FROM application a WHERE a.app_group_id ='area002_01' AND a.is_enable =1;
                                  """)
