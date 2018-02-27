# 闭包
# 1 .global x
# 2. nonlocal x

# def outside():
#     var = 5
#     def inside():
#         var = 3
#         print(var)
#     inside()
# outside()


# def outside():
#     var = 5
#     def inside():
#         print(var)
#         var = 3
#     inside()
# outside()

# def ou():
#     def ins():
#         print('hjsdf')
#     return ins
# ou()()


# globals关键字
"""
count = 6
def check():
    '申明count是全局变量，阻止python默认将count是生成一个check函数的局部变量（与全局的count=6重名）'
    global count
    count = 4
    print(count)
check()
print(count)
"""


# nonlocal关键字
# def outside():
#     var = 10
#     def inside():
#         nonlocal var
#         print(var)    # 此时 的var=10
#         var = 11
#         print(var)
#     return inside
# b = outside()
# b()



