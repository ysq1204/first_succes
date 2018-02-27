name=input('请输入你的名字')
print('你好'+name+'!')

# 按要求输入1-100之间的数字，
temp = input('请输入数字')
num = int(temp)
if 1 <= num <= 100:
    print('你的输入正确')
else:
    print('你的输入太小或者太大')