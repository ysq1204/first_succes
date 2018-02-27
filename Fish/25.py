# 0.字典又称哈希，散列，映射，关系数组
# 1.
# dict1=dict((('F',70,),('C',67),('h',104),('i',105),('s',115)))
# print(dict1['C'])

# 2。对，例如：集合
# ll = {1,2,3,4}
# print(type(ll))

# 3.列表在映射关系上不如字典强大

# 4.都是在创建一个字典
# d = dict([('two',2),('one',1),('three',3)])
# e = dict({'three':3,'one':1,'two':2})
# print(d, e)

# 5.
# data = '1000,小甲鱼,男'
# MyDict = {}
# (MyDict['id'],MyDict['name'],MyDict['sex']) = data.split(',')
# print('id:'+ MyDict['id'])
# print('name:'+ MyDict['name'])
# print('sex:'+ MyDict['sex'])

# 0.
# '''
print('---欢迎来到通讯录程序！---')
print('---1:查询联系人的资料---')
print('---2:插入新的联系人---')
print('---3:删除已有联系人---')
print('---4:退出通讯录程序---')

contacts = dict()
while True:
    order = int(input('请输入相关指令：'))
    if order == 1:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print(name + ':' + contacts[name])
        else:
            print('您输入的名字不在通讯录中！')

    if order == 2:
        name = input('请输入联系人的姓名：')
        if name in contacts:
            print('该成员已经在通讯录之中！')
            print(name + ':' + contacts[name])
            if input('是否修改用户资料（yes？no？）') == 'yes':
                contacts[name] = int(input('请输入用户联系电话:'))
        else:
            contacts[name] = input('请输入用户联系电话')

    if order == 3:
        name = input('请输入用户姓名：')
        if name in contacts:
            del(contacts[name])
            print('已删除用户：%s' % name)
        else:
            print('该用户不存在！')

    if order == 4:
        break

print('---感谢使用通讯录程序---')

print(contacts)
        # tel = input('请输入用户联系电话：')

# '''

#
# dict_test = {'le':13,'cc':19}
# name = input('请输入姓名')
# # print(type(name))
# if name in dict_test:
#     print(dict_test[name])

