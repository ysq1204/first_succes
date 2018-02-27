temp = input('请输入你的成绩')
while not temp.isdigit():
    temp = input('你的输入有误，请输入一个整数')
score = int(temp)
if 0 < score <= 100:
    if 90 <= score<= 100:
        print('A')
    elif 80 <= score < 90:
        print('B')
    elif 70 <= score <80:
        print('C')
    elif 60 <= score < 70:
        print('D')
    else:
        print('E')
else:
    print('你的输入范围有误，请输入0-100的数字')
