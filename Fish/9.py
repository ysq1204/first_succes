# 设计一个验证用户密码程序，用会输入错误，户只有三次机不过如果用户输入的内容中包含"*"则不计算在内。

"""
count = 3
password = 'ilovefish'
while count:
    passwd = input('请输入密码：')
    if passwd == password:
        print('欢迎登录')
        break
    elif '*' in passwd:
        print('密码里不能含有"*",你还有%d次机会'%count)
        continue
    else:
        count -= 1
        print('密码有误，你还有%d次机会！'%count)
"""


# 1. 编写一个程序，求 100~999 之间的所有水仙花数。
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
"""
for i in range(100,1000):
    sum1 = 0
    temp = i
    while temp:
        sum1 = sum1 + (temp % 10)**3
        temp //= 10
    if sum1 == i:
        print('水仙花数为：%d' % i)
"""

"""
for i in range(100,1000):
    sum2 = 0
    temp = i
    while temp:
        sum2 = sum2 + (temp % 10) ** 3
        temp //= 10
    if sum2 == i:
        print('水仙花数为%d'%i)
"""

# 有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。

# red = 3
# yellow = 3
# green = 6
print('red','yellow','green')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t', green)








# print('red\tyellow\tblue')
# for red in range(0, 4):
#     for yellow in range(0, 4):
#         for green in range(2, 7):
#             if red + yellow + green == 8:
# # 注意，下边不是字符串拼接，因此不用“+”哦~
#                 print(red, '\t', yellow, '\t', green)

