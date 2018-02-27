# 打印出0-100的奇数

"""
num = 100
for i in range(num):
    if i % 2 != 0:
        print(i, end = ' ')
"""

"""
i = 0
while i <= 100:
    if i % 2 != 0:
        print( i, end = ' ')
        i += 1
    else:
        i += 1

"""

# 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。

# total = 0
#
# total % 2 == 1 and total % 3 == 2 and
# total % 5 == 4 and total % 6 == 5 and
# total % 7 == 0

# x = 7
# i = 1
# flag = 0
# while i <= 100:
#     if (x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5):
#         flag = 1
#     else:
#         x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
# i += 1
# if flag == 1:
#    print('阶梯数是：', x)
# else:
#     print('在程序限定的范围内找不到答案！')



