#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import pymysql


class MysqlDatabase(object):
    # 定义基本属性
    mysql = ""
    database = ""
    cursor = ""
    result = ""

    def __init__(self, host='localhost', port=3306, user='root', passwd='', db='mysql', charset='utf8'):
        # 初始化连接数据
        try:
            # 使用连接数据连接数据库，返回连接信息
            self.database = pymysql.connect(host=host, port=port, user=user, passwd=passwd, charset=charset, db=db)
            print("Connect is successful！")
            # 创建游标，操作设置为字典类型
            self.cursor = self.database.cursor()
            print("Cursor is successful!")
        except:
            print("Database is error! ")

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭数据库
        print("Database is close！")
        self.database.commit()
        self.cursor.close()
        self.database.close()

    def execute_sql(self, sql):
        # 增加判断sql语句是否正确。
        try:
            self.cursor.execute(sql)
            self.result = self.cursor.fetchall()
            self.database.commit()
            print("Execute sql is successful! ")
        except Exception as e:
            self.database.rollback()
            print("Execute sql is error! ",e)
        return self.result

    def create_database(self, db_name):
        try:
            # 清空mysql语句
            self.mysql = ""
            self.mysql = "create database "+db_name+";"
            self.cursor.execute(self.mysql)
            print("Database create successful!")
        except:
            print("Database is create error ! ")


if __name__ == '__main__':
    mydb = MysqlDatabase(passwd='229183xiong', db='mysql')

