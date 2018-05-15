# -*- coding:utf-8 -*-

# Create_Author: cuihaiyan
# Create_time: 2018/5/15 13:35
# Desc:  继承，多态

class Animal(object):
    def run(self):
        print('Animal is running....')


class Dog(Animal):
    def run(self):
        print('Dog is running....')

class Cat(Animal):
    def run(self):
        print('Cat is running....')


class Tortoise(Animal):
    # pass
    def run(self):
        print('Tortoise is running slowly...')


# d = Dog()
#
# d.run()

# a = list() # a是list类型
# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型



def run_twice(animal):
    animal.run()
    animal.run()



run_twice(Animal())

run_twice(Dog())

run_twice(Cat())

# 新增一个Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
# 因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，
# 因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：

run_twice(Tortoise())


# 这就是著名的“开闭”原则：
#
# 对扩展开放：允许新增Animal子类；
#
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

