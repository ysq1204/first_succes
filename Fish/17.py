# 0.编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。

# def power(x, y):
#     result = x ** y
#     return result
# print(power(2, 3))


# def power(x, y):
#     result = 1
#     for i in range(y):
#         result *= x
#     return result
# print(power(2, 3))



# 1.编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，例如gcd(x, y)返回值
# 为参数x和参数y的最大公约数。

def gcd(x, y):
    while y:
        temp = x % y
        x = y
        y = temp
    return x
print(gcd(15, 3))



# 2.编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，
# 结果与调用bin()一样返回字符串形式。

def Binary(x):
    list1 = []
    summary = ''
    while x:
        temp = x
        result = temp % 2
        list1.append(result)
        x = x // 2
    while list1:
        summary += str(list1.pop())
    return summary
print(Binary(5))