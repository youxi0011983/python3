#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
爬虫的时候，经常遇到一种情况，刚开始的运行的时候，都如丝般顺滑，
可能一杯茶的功夫，就完犊子了，可能会出现各种各样的限制，比如 403 Forbidden 、 
429 Too Many Request 等等。
这时候，很有可能就是我们的 IP 被限制了
"""
from MysqlDatabase import MysqlDatabase

if __name__ == '__main__':
    mydb = MysqlDatabase(passwd='229183xiong', db='test')
    #sql ='create table proxy_pool(id varchar(255) NOT NULL ,scheme varchar(255),ip varchar(255),port varchar(255),status varchar(255),response_time int,create_date datetime,update_date datetime );'
    #sql ='create table QuoteItem (text varchar(255),author varchar(255),tags varchar(255) );'
    sql ='create table way_fair_produce (id varchar(255), average_overall_rating varchar(16), consumer_price varchar(16), display_price varchar(16), manufacturer varchar(32), product_name varchar(128), review_count varchar(16), size_option_count varchar(16), sku varchar(32), url varchar(500));'
    #sql = 'select * from proxy_pool'
    result = mydb.execute_sql(sql)
    #for i in result:
        #print(i)

