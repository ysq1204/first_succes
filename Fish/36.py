# 0.对象的属性和方法，在编程里实际是什么？
# 答：属性就是变量，方法就是函数
# 1.类和对象的关系？
# 答 ：类本身就是一个对象，只不过类这个对象，需要有一个实例化的对象才可以使用
# 2.咖啡猫、tom、kitty
# 3.矩形类，属性：长，宽，高；方法：计算面积，计算周长
# 4.类的属性应该尽可能抽象，这样更符合面向对象的编程思维
# 5.面向对象的几个特征概述：
# 封装、对外部隐藏对象的工作细节
# 继承、子类自动共享父类之间数据和方法的机制
# 多态、可以对不同类的对象调用的相同的方法，产生不同的结果
# 6.函数和方法的区别？
# 方法里面多了一个self参数，self指类本身

"""
class dog():
    sex = 'male'
    def eat(self):
        print('woshieat!')
    def cry(self):
        print('woshicry!')

a = dog()
print(id(a.cry()))
b = dog()
print(id(b.cry()))
"""

# 0.
class Person:
    name = '小甲鱼'
    def printname(self):
        print(self.name)