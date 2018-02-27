
import time
# """
def timemer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        print('执行时间是%s' %(stop - start))
    return wrapper

@timemer    # 所谓装饰器就是将被装饰的函数作为参数传到装饰的函数里进行运行
def exe():
    print('i am running!')
    time.sleep(2)
    print('look out!')
exe()
# """

# 三：编写装饰器，为函数加上认证的功能
def auth(func):
    def wrapper(*args, **kwargs):
        name = input('请输入你的名字：').strip()
        passwd = input('请输入你的密码：').strip()
        if name == 'lvanka' and passwd == '123':
            func(*args, **kwargs)
    return wrapper

@auth
def my_log(name):
    print('%s欢迎登录'%(name))
my_log('lvanka')

# 四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
# 注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式






# def count_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         # time.sleep(2)
#         stop = time.time()
#         print('执行时间是%s' % (stop - start))
#     return wrapper
#
# @count_time
# def show_fab():
#     a = 0
#     b = 1
#     while True:
#         a, b = b, a+b
#         if a < 100000:
#             yield a
# show_fab()



# class fab():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
# # fab(0, 1)
# @count_time
# def show_fab():
#     for i in fab(0,1):
#         if i < 100:
#             print(i)
# show_fab()




