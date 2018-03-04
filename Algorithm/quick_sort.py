

# """
def quick_sort(list):
    less = []
    pivotList = []
    more = []
    # 递归出口
    if len(list) <= 1:
        return list
    else:
        # 将第一个值做为基准
        pivot = list[0]
        for i in list:
            # 将比基准值小的值放到less数列
            if i < pivot:
                less.append(i)
            # 将比基准大的值放到more数列
            elif i > pivot:
                more.append(i)
            # 将和基准相同的值保存在基准数列
            else:
                pivotList.append(i)
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more


lists = [1,21,12,32,43,14,24,54,11,2,5,7,5,4,28]
print(quick_sort(lists))
# """

"""
def quick_sort(list):
    less = []
    middle = []
    more = []

    if len(list) <= 1:
        return list
    else:
        base = list[0]
        for i in list:
            if base > i:
                less.append(i)
            elif base < i:
                more.append(i)
            else:
                middle.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + middle + more
    
"""