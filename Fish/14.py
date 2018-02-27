a="ilovefishc.com"
print(list(a))
print(tuple(a))
print(str(a))

# 1. 视频中我们说 sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，请写出一个新的实现过程，自动“无视”参数里的字符串并返回正确的计算结果
def sum(x):
    result = 0
    for i in x:
        if type(i) == int or type(i) == float:
            result += i
        else:
            continue
    return result
print(sum([1,2,9,'h',12]))


name = input('请输入待查找的用户名：')
score = [['迷途', 85], ['黑夜', 80], ['小布丁', 65], ['福禄娃娃', 95], ['怡静', 90]]
IsFind = False

for each in score:
    if name in each:
        print(name + '的得分是：', each[1])
        IsFind = True
        break

if IsFind == False:
    print('查找的数据不存在！')





