import os
import keyword

print(keyword.kwlist)   # 打印出所有的关键字
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
#  'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
#  'try', 'while', 'with', 'yield']

while True:
    strl = input('')
    if strl == 'ysq':
        print('it ok')
    elif strl == 'exit':
        break
    else:
        print('it is worry')

a=2313213
b=324221204
print(a*b)

print('marry'+'lily')

