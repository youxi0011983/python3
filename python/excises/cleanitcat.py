#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


import itchat
import json
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 获取处理分组
def create_process_list(process_size):
    process_list = []
    default_process_size = 35
    process_group_size = process_size / default_process_size
    if process_size % default_process_size > 0:
        process_group_size = process_group_size + 1
    for i in range(process_group_size):
        start = (i * default_process_size)
        end = start + default_process_size
        if end > process_size:
            end = process_size
        process_list.append({'start': start, 'end': end})
    return process_list


def get_delete_user_list(start, end, friends):
    print 'start run get_delete_user start: ' + str(start) + ', end: ' + str(end)
    process_member_list = friends[start:end]
    member_dict = {}
    for member in process_member_list:
        member_dict[member['UserName']] = member
        print member['NickName'] + '-----' + str(start)

    group_name = 'g1' + str(random.randint(0,1199))
    print 'group_name：' + group_name
    result = itchat.create_chatroom(process_member_list, group_name)
    print 'result: ' + json.dumps(result)
    result_member_list = result['MemberList']
    delete_list = []
    for result_member in result_member_list:
        print '---------------member-------------'
        print json.dumps(result_member)
        if result_member['MemberStatus'] == 4:  # 被对方删除了
            delete_list.append(result_member['UserName'])
            print '这个人删除了我' + result_member['UserName']
    return delete_list


itchat.auto_login(hotReload=True)

friends = itchat.get_friends()
friends_len = len(friends)
print '打印好友数量：' + str(friends_len)


process_list = create_process_list(friends_len)
delete_user_list = []
for process in process_list:
    start = process['start']
    end = process['end']
    list = get_delete_user_list(start, end, friends)
    print '删除我的人数:' + str(len(list))

# list = get_delete_user_list(170, 173, friends)
# print '删除我的人数:' + str(len(list))

# print '删除我的人数：' + str(len(delete_user_list))
# for

itchat.dump_login_status()