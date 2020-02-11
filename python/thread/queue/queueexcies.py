#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import queue 
from time import sleep
print("queue....")
#Python queue模块的FIFO队列先进先出
#队列长度可为无限或者有限。可通过queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。
q=queue.Queue(maxsize = 10)
#队列长度可为无限或者有限。可通过queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。
for i in range(10):
    q.put(i)
#调用队列对象的get()方法从队头删除并返回一个项目。
for i in range(10):
    print(q.get())
    sleep(1)

print("\nLifoqueue...")
#LIFO类似于堆，即先进后出
q=queue.LifoQueue(maxsize = 10)
for i in range(10):
    q.put(i)
for i in range(10):
    print(q.get())
    sleep(1)

print("\n queue function....")
q.qsize()
q.empty()
q.empty()
# 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.task_done()
#实际上意味着等到队列为空，再执行别的操作
q.join()