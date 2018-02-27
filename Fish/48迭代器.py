# 0.迭代就是就是一个重复反馈过程的活动，目的是为了接近并达到索要要的目标或结果，
# 每一次对过程的重复称之为迭代，而且每一次迭代的结果会被用作下一次迭代的初始值

# 1.迭代器不是一个容器，列表，字典，元组都是可以存放数据的容器，而迭代器就是实现了__next__()方法的对象（用于遍历容器中的数据）
# 2.迭代器不可以回退区上一个值
# 3.判断一个容器是否有迭代功能，应该判断它是否有__iter__(),__next__()魔法方法
# 4.for语句如何判断迭代器内容去空了？
# 答：迭代器通过__next__()方法返回每一个元素，并指向下一个元素。如果当前位置已无元素，通过抛出StopIterations异常表示


# 5.只能用迭代器访问的Python数据结构是？集合
# sete = {1,2,3}
# tuple1 = (1,2,3)
# # print(sete[0])
# print(tuple1[2])
# print(type(tuple1))

# 0.用while与实现以下功能
# for each in range(5):
#     print(each)
#

# it = iter(range(5))
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

# 1.写一个迭代器，要求输入闰年
# for i in range(2000, 2018):
#     if i % 4 == 0 and i % 100 !=0 or i % 400 == 0:
#         print(i)

import datetime as dt
# ll = dt.datetime.now().year
# print(ll)

class LeapYears:
    def __init__(self):
        self.now = dt.datetime.now().year

    def isleapyear(self, year):
        if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    def __iter__(self):
        return self

    def __next__(self):
        while not self.isleapyear(self.now):
            self.now -= 1
        temp = self.now
        self.now -= 1
        return temp


leapyear = LeapYears()
for i in leapyear:
    if i >= 2000:
        print(i)
    else:
        break

# 2.写一个类功能与reversed()相同
# str1 = 'i love fishc.com'
# ll = reversed(str1)
# for i in ll:
#     print(i)

"""
class MyRev:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index-1
        return self.data[self.index]


myrev = MyRev('ilovefishc.com')
for i in myrev:
    print(i, end = '')
"""


# 3.自己联系，生成菲波那切数列,迭代器
"""
class fab:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.b, self.a = self.a, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a


fa = fab(0, 1, 100)
for i in fa:
    print(i)
"""


class Transform:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


tran = Transform('ilovefishc.com')
for i in tran:
    print(i)