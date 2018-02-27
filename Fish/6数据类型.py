import random

# num = 3.900
# print(int(num))
# 你好=3
# print('你好')


"""
import random

print('-------welcome to my house-------')
num = random.randint(1, 10)
times = 3
while times:
    guess = int(input('Please input your number!You total have 3 times!'))
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
times = 3
secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
guess = 0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input("抱歉，您的输入有误，请输入一个整数：")
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
print("游戏结束，不玩啦^_^")
'''

"""
print('********欢迎来到小甲鱼之家*********')
serect = random.randint(1,10)
times = 3
guess = 0
while times > 0 and guess != serect:
    temp = input('请输入你要猜的数字：')
    while not temp.isdigit():
        temp = input('你的输入有误，请输入整数！')
    guess = int(temp)
    if guess == serect:
        print('恭喜你答对了')
    else:
        if guess >= serect:
            print('大了，大了！！')
        else:
            print('小了小了！~~')
        if times > 0:
            times -= 1
            print('你好有%d次机会'%times)
            print('-------------')
        else:
            print('你的机用完了，真正的答案是%d'%serect)
print('游戏结束了')
"""

# :能被4整除但不能被100整除,或者能被400整除都是闰年。

temp = input('请输入特定的年份，例如：1994')

while not temp.isdigit():
    temp = input('您的输入有误，请输入正确的年份，例如：1994')
year = int(temp)
print(year)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('%d是闰年' % year)
else:
    print('%d不是闰年' % year)







