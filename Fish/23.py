# 递归实现10 ---> 2进制转换，除2取余法
# def transform(n):
#     result = ''
#     if n:
#         result = transform(n // 2)
#         return result + str(n % 2)
#     else:
#         return result
#
#
# sum1 = transform(17)
# print(sum1)

"""
def trans2(x):
    result = ''
    if x:
        result = trans2(x // 2)
        return result + str(x % 2)
    else:
        return result

sum2 = trans2(20)
print(sum2)
"""


# 01.
result = []
def get_digits(n):
    if n:
        result.append(n % 10)
        get_digits(n // 10)
        return reversed(result)

b = get_digits(12345)
print(list(b))

# 02.回文字符
# 上海自来水来自海上

"""
def check(str1, start, end):
    if start > end:
        return 1
    else:
        if str1[start] == str1[end]:
            return check(str1,start+1,end-1)
        else:
            return 0
string = input("请输入一串字符串")
lenght = len(string)-1
print(lenght)

if check(string,0,lenght):
    print('“%s”是回文字符'%string)
else:
    print('%s不是回文字符'%string)
"""
'''
def check(n, start, end):
    if start > end:
        return True
    else:
        if n[start] == n[end]:
            return check(n, start+1, end-1)
        else:
            return False

string = input('请输入要检查的字符串')
lenght = len(string)-1

if check(string, 0, lenght):
    print("'%s'：是回文字符串" % string)
else:
    print("'%s'：不是回文字符串" % string)
# 递归调用字符串的每一个字，并判断start字与end的字是否相等
'''


# 0.3判断年龄，第一个人10岁，其他几个人依次比第一个人大2岁,求第n个人多少岁
def get_age(n):
    if n == 1:
        return 10
    else:
        return get_age(n - 1) + 2

print(get_age(15))