"""import keyword
print(keyword.kwlist)
# 只有关键词不能作为变量名，内置函数的名字可以作为变量名,但是最好不用
input = 'name'
print(input)
super='nini'
print(super)
"""

"""
DayPerYear = 365
HourPerDay = 24
MinPerHour = 60
SecondPerMin = 60
SecondPerYear = DayPerYear*HourPerDay*MinPerHour*SecondPerMin
print(SecondPerYear)
"""

"""
import random

print('-------welcome to my house-------')
num = random.randint(1, 10)
times = 3
while times:
    temp = input('Please input your number!You total have 3 times!')
    guess = int(temp)
    if guess == num:
        print('you are right!!!')
        break
    else:
        if guess > num:
            print('it is too large!')
        else:
            print('it is too small!')
    times -= 1
    print('You have %d times! ' % times)

    if times == 0:
        print('Times is over!The num is %d' % num)
print('Game over!')
"""


'''
import random

guess = int(input("请输入小甲鱼心中的数字："))
secret = random.randint(1, 10)
count = 3
while count:
    if guess == secret:
        print("恭喜你，猜对了！")
        break
    else:
        if guess > secret:
            print("大了！", end='')
        else:
            print("小了！", end='')
        count -= 1
        print("你还有 %d 次机会，请继续：" % count, end='')
        guess = int(input())

    if count == 1:
        break
if count == 1:
    print("次数用完了，游戏结束")
    print("小甲鱼心中的数字是：%d" % secret)
'''


# num = int(input('请输入一个整数：'))
# i = 0
# while num:
#     num -= 1
#     i += 1
#     print(i)


# num = int(input('请输入一个整数：'))
# while num:
#     print(' '*(num-1)+'*'*num)
#     num -= 1