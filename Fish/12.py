# 0.请写一个密码安全性检查的脚本代码：check.py
#
# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
"""
nums = '0123456789'
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '''~!@#$%^&*()_=-/,.?<>;:[]{}\|'''
passwd = input('请输入你的密码：')
lenght = len(passwd)

while passwd.isspace() or lenght == 0:
    passwd = input('你的输入为空（空格），请重新输入！')
flag_len = 0
if lenght <= 8:
    flag_len = 1
elif 8< lenght <= 16:
    falg_len = 2
elif lenght > 16:
    flag_len = 3

flag_con = 0
# 判断是否包含特殊字符
for each in passwd:
    if each in symbols:
        flag_con += 1
        break

# 判断是否包含数字
for each in passwd:
    if each in nums:
        flag_con += 1
        break


# 判断是否包含字母
for each in passwd:
    if each in chars:
        flag_con += 1
        break

while 1:
    if flag_len == 1 or flag_con == 1 :
        print('低')
        break
    elif flag_len == 2 or flag_con == 2:
        print('中')
        break
    else:
        print('高')
        break
"""

'''这是给出的参考答案，用的是for循环，依次判断，思路比较明白'''

"""
symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input('请输入需要检查的密码组合：')

# 判断长度
length = len(passwd)

while (passwd.isspace() or length == 0):
    passwd = input("您输入的密码为空（或空格），请重新输入：")

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3

flag_con = 0
# 判断是否包含特殊字符
for each in passwd:
    if each in symbols:
        flag_con += 1
        break

# 判断是否包含字母
for each in passwd:
    if each in chars:
        flag_con += 1
        break

# 判断是否包含数字
for each in passwd:
    if each in nums:
        flag_con += 1
        break

    # 打印结果
while 1:
    print("您的密码安全级别评定为：", end='')
    if flag_len == 1 or flag_con == 1:
        print("低")
    elif flag_len == 2 or flag_con == 2:
        print("中")
    elif flag_len == 3 or flag_con == 3:
        print("高")
        print("请继续保持")
        break

    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位'")
    break

# 有小疑惑，例如：687gjh￥#@&hujsdf 并未遵循以字母开头，却是高等级
# 有的时候不必太过在意，因为只有低、中、高三个等级，没有的等级可以遵循

"""

'''
# 这是楼主用正则表达是的方法写的，有点麻烦
import re


def lowprint():
    print("请按以下方式提升您的密码安全级别：\n\
          1.密码必须由数字、字母及特殊字符三种组合 \n\
          2.密码只能由字母开头\n\
          3.密码长度不能低于16位")


def highprint():
    print("请继续保持！")


def judgeishigh(temp):
    flag = 0
    specialsignal = r'~!@#$%^&*()_=-/\,.?<>;:[]{}|'
    length = len(temp)
    if len(temp) >= 16:
        if re.search('.*([a-z,A-Z]).*', temp[0]):
            if re.search('.*([0-9]).*', temp):
                for i in temp:
                    if i in specialsignal:
                        flag = 1
                if flag:
                    print("您的密码安全级别评定为：高")
                    highprint()
                else:
                    judgeismid(temp)
            else:
                judgeismid(temp)
        else:
            judgeismid(temp)
    else:
        judgeismid(temp)


def judgeismid(temp):
    specialsignal = r'~!@#$%^&*()_=-/\,.?<>;:[]{}|'
    if len(temp) >= 8:
        if re.search('.*([0-9]).*', temp) and re.search('.*([a-z,A-Z]).*', temp):
            print("您的密码安全级别评定为：中")
            lowprint()
        else:
            if re.search('.*([specialsignal]).*', temp) and re.search('.*([a-z,A-Z]).*', temp):
                print("您的密码安全级别评定为：中")
                lowprint()
            else:
                if re.search('.*([specialsignal]).*', temp) and re.search('.*([0-9]).*', temp):
                    print("您的密码安全级别评定为：中")
                    lowprint()
                else:
                    print("您的密码安全级别评定为：低")
                    lowprint()
    else:
        print("您的密码安全级别评定为：低")
        lowprint()


if __name__ == '__main__':
    temp = input("请输入需要检查的密码组合：")
    judgeishigh(temp)
'''