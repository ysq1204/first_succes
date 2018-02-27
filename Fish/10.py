"""假设给定以下列表：
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
要求将列表修改为：
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
方法一：使用 insert() 和 append() 方法修改列表。
方法二：重新创建一个同名字的列表覆盖。
"""
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member.insert(1,88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.append(88)
# print(member)

# 1. 利用 for 循环打印上边 member 列表中的每个内容
# for i in member:
#     print(i)

#  2. 上一题打印的样式不是很好，能不能修改一下代码打印成下图的样式呢？【请至少使用两种方法实现】
# 方法一：
# count = 0
# lenght = len(member)
# while count < lenght:
#     print(member[count], member[count+1])
#     count += 2

# 方法二：
# lenght = len(member)
# for i in range(lenght):
#     if i % 2 == 0:
#         print(member[i], member[i+1])

list1 = ['许怒', 12, '小孩', 34, '白化', 90]
len1 = len(list1)
for i in range(len1):
    if i % 2 == 0:
        print(list1[i], list1[i+1])