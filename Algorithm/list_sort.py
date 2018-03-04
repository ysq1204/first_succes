list1 = [1,2,1,2,3,4,2,65,7,89,87,46,67,23,37,92]

# 1.直接使用集合，缺点是再转换成列表时无法保存之前的列表顺序，
print(list1)
print(list(set(list1)))
# 2.定义个空列表，遍历原来的列表里的值，
# 并判断遍历的每一个值是否在空列表里，
# 如果不在就添加进去
# 缺点：效率会底下，因为列表是按索引顺序去查找的，
# 当数据量很大时会变慢。
def remove_com(data):
    new_list = []
    for i in data:
        if i not in new_list:
            new_list.append(i)
    return new_list


# result = remove_com(list1)
# print(result)

# 3.集合加遍历
# 既然在判断时用列表会影响效率，
# 那我们就转换一个思路，我们用集合，
# 那你可能要问了，那集合就快了?
# 没错，因为set使用的hash函数查找值，
# 虽然set无序，但位置是固定的，
# 只需一次就可以查到特定元素是否存在，
# 网上有人做了列表和set的元素查找对比，
# 相同的数据条件下，用list耗时16分钟，
# 用set耗时是52秒
list2 = []
set2 = set()

for i in list1:
    if i not in set2:
        set2.add(i)
        list2.append(i)
print(list2)
