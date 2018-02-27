"""
def MySum(*parameter, base=3):
    sum = 0
    if parameter[-1] == 5:
        base = 5
        for i in parameter:
            sum = sum + i
        return (sum - 5) * base
    else:
        for i in parameter:
            sum = sum + i
        return sum * base


result = MySum(1, 1, 2, 8, base=5)
print(result)


def Func(*parameter, base=3):

    result = 0
    for i in parameter:
        result += i
        result *= base
    print('结果是：{}' .format(result))


Func(1, 21, 1, base=5)
"""

"""
def find_flower():
    '水仙花数的算法。例如：153 = 1^3 + 5^3 + 3^3'
    for num in range(100,1000):
        temp = num
        sum = 0
        while temp:
            sum += (temp % 10) ** 3
            temp = temp // 10
        if sum == num:
            print('水仙花数有：{}'.format(num))


find_flower()

"""


def find_str(original_str, target_str):
    count = 0
    lenght = len(original_str)
    if target_str not in original_str:
        print('目标字符串不在原字符串中')
    else:
        for each in range(lenght):
            if original_str[each] == target_str[0]:
                if original_str[each+1] == target_str[1]:
                    count += 1
    print('目标字符串出现了:{}次'.format(count))


original_str = input('请输入的原字符串：')
    # 'you are a beautiful girl, marry is a girl, but she is not beautiful girl!'
target_str = input('请输入目标字符串（两个字符）：')
find_str(original_str, target_str)