# 1.选择排序：选择第一个数与后面的数依次比较，遇到最小的就将该数提到前面
# 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 重复第二步，直到所有元素均排序完毕。
def SelectSort(list):
    lenght = len(list)
    for i in range(0, lenght):
        min = i
        for j in range(i+1, lenght):
            if list[j] < list[min]:
                min = j
                list[min], list[i] = list[i], list[min]
    return list
print(SelectSort([1,2,11,4,3]))