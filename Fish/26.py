# 0.python不支持一键多值
# 1.为不存在的键赋值就会新增加该键值对
# 2.dict.get(key,)或者直接dict[key]但是该方法不如第一个用户体验好
# 3.str，int，float,bool都可以
dict1 = {True:True}
# print(type(dict1))
# 4.答案：
# {1:('one','two','three'),2:('one','two','three'),3:('one','two','three')}
# {1:'数字',2:'数字'}
# help(dict.fromkeys)
# 5.
# dict2 = dict1.copy()   # 浅拷贝
# print(dict2)
# help(dict.setdefault)


# 0.简单版
"""
print('---新建用户：N/n---')
print('---登录账号：E/e---')
print('---退出程序：Q/q---')
contacts = dict()
while True:
    order = input('请输入指令：')
    if order == 'N' or order == 'n':
        name = input('请输入新建用户名：')
        if name in contacts:
            name = input('此用户名已经被使用，请重新输入：')
        else:
            passwd = input('请输入密码：')
            contacts[name] = passwd
            # print(contacts)
        print('注册成功，赶紧试试登录吧~~~')

    if order == 'E' or order == 'e':
        name = input('请输入登录账号：')
        if name in contacts:
            passwd = input('请输入登录密码：')
            if passwd == contacts[name]:
                print('登录成功！')
            else:
                print('你的密码输入有误！')
        else:
            print('你输入的用户名不存在，请重新输入：')

    if order == 'Q' or order == 'q':
        print('欢迎进入xxoo系统，请点击右上角的x结束程序！')
        break
"""


 # '封装函数，高级版'
contacts = dict()


def new_user():
    prompt = input('请输入用户名：')
    while True:
        name = input(prompt)
        if name in contacts:
            prompt = '该用户已存在，请登录！'
        else:
            break
    passwd = input('请输入密码：')
    contacts[name] = passwd
    print('注册成功，赶紧试试登录吧~~~')


def old_user():
    prompt = input('请输入用户名：')
    while True:
        name = input(prompt)
        if name not in contacts:
            prompt = '该用户不存在，请重新输入！'
            continue
        else:
            break
    passwd = input('请输入密码：')
    if passwd == contacts[name]:
        print('欢迎进入xxoo系统，请点击右上角的x结束程序！')
    else:
        print('您的密码输入有误！')


def show_meu():
    prompt ='''
    ---新建用户：N/n---
    ---登录账号：E/e---
    ---退出程序：Q/q---
    ---请输入指令：'''
    while True:
        chosen = False
        while not chosen:
            choice = input(prompt)
            if choice not in 'NnEeQq':
                print('你的指令输入有误，请重新输入！')
            else:
                chosen = True
        if choice == 'q' or choice == 'Q':
            break
        if choice == 'N' or choice == 'n':
            new_user()
        if choice == 'e' or choice == 'E':
            old_user()
show_meu()







