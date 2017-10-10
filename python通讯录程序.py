# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:59:44 2017

@author: Tidus
"""

print('---欢迎您使用通讯录程序---')
print('--- 1：查询联系人资料 ---')
print('--- 2：插入新的联系人 ---')
print('--- 3：删除已有联系人 ---')
print('--- 4：退出通讯录程序 ---')

def modify():
    name = input('请输入联系人姓名:')
    if name in data.keys():
        print('你输入的姓名在通讯录已经存在-->>',name,':',data[name])
        confirm = input('是否修改用户资料？(YES/NO):')
        if confirm == 'YES':
            new_number = input('请输入新的联系人电话:')
            data[name] = new_number
            cmd()
        elif confirm == 'NO':
            cmd()
    else:
        number = input('请输入联系人电话号码:')
        data[name] = number
        cmd()
        
def inquiry():
    name = input('请输入联系人姓名:')
    if name in data.keys():
        print(name,':',data[name])
        cmd()
    else:
        print('没有找到联系人')
        cmd()
        
def delete():
    name = input('请输入您想删除的联系人姓名:')
    if name in data.keys():
        del data[name]
        print('联系人已删除')
        cmd()
    else:
        print('没有找到联系人')
        cmd()
        
def cmd():
    cmd = input('\n请输入指令代码:')
    if cmd == '1':
        inquiry()
    elif cmd == '2':
        modify()
    elif cmd == '3':
        delete()
    elif cmd == '4':
        print('---感谢您使用通讯录程序---')
    else:
        '您输入的指令有误'
    
data = {}
cmd()
