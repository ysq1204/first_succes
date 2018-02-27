# 递归---算法（函数调用自身）
# def recursion():
#     return recursion()
# recursion()

# def mul(x):
#     sum = 1
#     for i in range(1, x+1):
#         sum *= i
#     return sum
#
# print(mul(10))


# 递归实现阶乘，有进有出
# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
# num = int(input('please input a number：'))
# result = factorial(num)
# print('%d的阶乘是:%d'%(num, result))

# 0.
def function1(x):
    if x == 1:
        return 1
    return x * function1(x - 1)

# 1.递归满足条件：1.调用自身。2.正确的终止递归的条件
# 2.必须使用递归的情形：目录索引，快速排序
# 3.因为递归十分暂用内存，而且很耗时
# 4.递归优点：代码量减少；方便
# 缺点：耗时，耗内存；容易出错，导致程序崩溃；

# 0.递归实现，x的y次幂
