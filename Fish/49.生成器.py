# 0.一般函数从第一行开始执行，并在
# 对于调用一个昔通的Python 函数，一般是从函数的第一行代码开始执行，结束于return 语句、异常或者函数
# 所有语句执行完毕。一旦函数将控制权交还给调用者，就意味着全部结束。函数中做的所有工作以及保存在局部变
# 量中的数据都将丢失。如果再次调用这个函数时，一切都将重新开始。

# 1.什么是协同和程序？
# 答:所谓的协同程序就是可以运行的独立函数调用，函数可以暂停或者挂起，并在需要的时候从程序离开的地方继
# 续或者重新开始。
# Python 是通过生成器来实现类似于协同程序的概念:生成器可以暂时挂起函数并保留函数的局部变量等数据，然
# 后在再次调用它的时候，从上次暂停的位置继续执行下去。

# 2.生成器就是一个特殊的迭代器。
# 答是的，都可以。因为生成器事实上就是基于迭代器来实现的,生成器只需要一个yield 语句即可但它内部会白
# 动创建iter_0 和_next__O 方法。


# 3.把return改为yield
# 4.生成器的最大最用就是挂起，下次从挂起的地方继续执行，既保留现场
# 5.是的程序一直循环执行，
# 答: 这个whileTrue循环是用来确保生成器函数永远也不会执行到函数末尾的。只要调用next0 这个生成器就会生
# 成一个值。这是一个处理无穷序列的常见方法(这类生成器也是很常见的)。
# def get_prime(number):
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1


# 0.用生成器实现reversed()功能


# def transform(data):
#     for index in range(len(data)-1,-1,-1):
#         yield data[index]
#
#
# tran = transform('ilovefishc')
# for i in tran:
#     print(i)

# for i in range(10,-1,-1):
    # print(i)

# """
def fab():
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield a

sum = 0
for i in fab():
    if i >100:
        break
    sum += i
    # print(i, end=' ')
print(sum)
# """

# 1.1000以内的素数之和？
"""
import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
    return False


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def solve():
    total = 2
    for next_prime in get_primes(3):
        if next_prime < 10000:
            total += next_prime
        else:
            print(total)
            return


if __name__ == '__main__':
    solve()

# """


# n = int(input("please enter the number："))
# for i in range(2, n):
#     if n % i == 0:
#         print(" %d is not a prime number！" % n)
#         break
# else:
#     print(" %d is a prime number！" % n)

#
# def is_prime(n):
#     # x = 1    # x累计1到n中的质数个数，由于2也是质数，这里先加+1
#     for i in range(3,n+1):  # 3到n+1取值（取一个值出来用内循环判断此数是否为质素）
#         result = True
#         for j in range(2,i-1):   # 2到i-1之间有没有被整数的数，有则不是质素
#             if i % j == 0:
#                 result = False
#         # if result == True:
#         #     print(i)
#
#     # print('\n%d 内有 %d 个质数' %(n,x))
# is_prime(10)