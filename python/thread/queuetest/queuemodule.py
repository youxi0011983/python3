#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from queue import Queue
from numpy import block

q = Queue()

# 此包中的常用方法(q =queue.queue()):
q.qsize()  # 返回队列的大小
q.empty()  # 如果队列为空，返回True,反之False
q.full()  # 如果队列满了，返回True,反之False
# q.full 与 maxsize 大小对应
# q.get([block[, timeout]])  # 获取队列，timeout等待时间
# q.get_nowait() 相当q.get(False)
# 非阻塞 q.put(item) 写入队列，timeout等待时间
# q.put_nowait(item)  # 相当q.put(item, False)
q.task_done()  # 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.join()  # 实际上意味着等到队列为空，再执行别的操作

# queue.qsize() 返回队列的大小
# queue.empty() 如果队列为空，返回True,反之False
# queue.full() 如果队列满了，返回True,反之False
# queue.full 与 maxsize 大小对应
# queue.get([block[, timeout]])获取队列，timeout等待时间
# queue.get_nowait() 相当queue.get(False)
# queue.put(item) 写入队列，timeout等待时间
# queue.put_nowait(item) 相当queue.put(item, False)
# queue.task_done() 在完成一项工作之后，queue.task_done()函数向任务已经完成的队列发送一个信号
# queue.join() 实际上意味着等到队列为空，再执行别的操作
