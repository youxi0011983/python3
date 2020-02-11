#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql 
import uuid

MYSQL_HOST = 'localhost' 
MYSQL_PORT = 3306 
MYSQL_USER = 'root' 
MYSQL_PASSWORD = '229183' 
MYSQL_DB ='test' 
MYSQL_CHARSET = 'utf8mb4' 
 

class MysqlClient(object): 
	def __init__(self, host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB, charset=MYSQL_CHARSET): 
		""" 初始化 mysql 连接 :param host: mysql 地址 :param port: mysql 端口 :param user: mysql 用户 :param password: mysql 密码 :param database: mysql scheme :param charset: 使用的字符集 """ 
		self.conn = pymysql.connect( host = host, port = port, user = user, password = password, database = database, charset = charset )
		print("Mysql conn succesfull!!!!")
		print("="*50)
	
	def add_proxy(self, proxy): 
		""" 新增代理 :param proxy: 代理字典 :return: """ 
		sql = 'INSERT INTO `proxy_pool` VALUES (%(id)s, %(scheme)s, %(ip)s, %(port)s, %(status)s, %(response_time)s, now(), null )' 

		data = { "id": str(uuid.uuid1()), "scheme": proxy['scheme'], "ip": proxy['ip'], "port": proxy['port'], "status": proxy['status'], "response_time": proxy['response_time'], } 
		try:
			self.conn.cursor().execute(sql, data) 
			self.conn.commit() 
		except:
			self.conn.rollback()
	
	def find_all(self): 
		""" 获取所有可用代理 :return: """ 
		sql = 'SELECT * FROM proxy_pool WHERE status = "0" ORDER BY update_date ASC ' 
		#sql = 'SELECT * FROM proxy_pool WHERE status = "1" ORDER BY update_date ASC ' 
		cursor = self.conn.cursor() 
		cursor.execute(sql) 
		self.conn.commit()
		res = cursor.fetchall() 
		return res

	def update_proxy(self, proxy): 
		""" 更新代理信息 :param proxy: 需要更新的代理 :return: """ 
		sql = 'UPDATE proxy_pool SET scheme = %(scheme)s, ip = %(ip)s, port = %(port)s, status = %(status)s, response_time = %(response_time)s, update_date = now() WHERE id = %(id)s ' 
		data = { "id": proxy['id'], "scheme": proxy['scheme'], "ip": proxy['ip'], "port": proxy['port'], "status": proxy['status'], "response_time": proxy['response_time'], } 
		self.conn.cursor().execute(sql, data) 
		self.conn.commit()

'''
在这个类中，我们首先定义了一些常量，都是和数据库连接有关的常量，如 MYSQL_HOST 数据库地址、 MYSQL_PORT 数据库端口、 MYSQL_USER 数据库用户名、 MYSQL_PASSWORD 数据库密码、 MYSQL_DB 数据库的 scheme 、 MYSQL_CHARSET 字符集。
接下来定义了一个 MysqlClient 类，定义了一些方法用以执行数据库的相关操作。
init()： 初始化方法，在初始化 MysqlClient 这个类时，同时初始化了 Mysql 数据库的链接信息，获得了数据库连接 connection 。
add_proxy()：向数据库中添加代理，并添加相关信息，包括代理响应延时和健康状况。
find_all()：获取所有数据库可用代理，并根据更新时间正序排布，主要用于后续代理检查。
update_proxy()：更新代理信息，主要用户检查模块检查完代理后更新代理信息，根据取出当前代理的主键 id 进行更新。
'''
