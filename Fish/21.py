# 匿名函数：lambda



# 高端的bif filter()

# def odd(x):
#     return x % 2
# # odd(3)
# temp = range(10)
# show = filter(odd, temp)
# print(list(show))


# g = list(filter(lambda x : x % 2, range(10)))
# print(g)


# 高端bif map()
# map()有两个参数，第一个是函数，第二个是可迭代的序列，
# 将序列的每一个元素作为函数的参数，运算加工直到运算完成序列的所有的元素，
# 并返回加工完成的新序列

# 例如：
# new = list(map(lambda x : x * 2,range(10)))
# print(new)
# 0.
# g=lambda x, y=3: x*y
# print(g(5,y=3))
# 1.
# def transform(x):
#     if x % 2:
#         return x
#     else:
#         return None
#
# print(transform(11))

# 3.匿名函数可以节省代码量，
# 也可以减少起函数名带来的困扰
# 4.
# g = list(filter(lambda x : not(x % 3), range(1,100)))
# print(g)
# 5.
# l = [x for x in range(1,100) if not(x % 3)]
# print(l)
#
# 6.
l1 = list(zip([1,2,3,4],[9,8,7,6,5]))
print(l1)
l2 = list(map(lambda x,y :[x,y],[1,2,3,3,4],[9,8,7,6,5,4]))
print(l2)