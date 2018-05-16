# -*- coding:utf-8 -*-

# Create_Author: cuihaiyan
# Create_time: 2018/5/16 11:26
# Desc:  面向对象高级编程

# 数据封装，继承和多态只是面向对象程序设计中最基础的3个概念

# 面向对象还有很多高级特性，允许我们写出非常强大的功能
# 多重继承，定制类，元类等等

class Student(object):
    __slots__ = ('name', 'age','set_age') # 用tuple定义允许绑定的属性名称


class GraduateStudent(Student):
    __slots__ = ('score')
    pass


# 在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
g = GraduateStudent()
g.score = 9999
g.name = 'Tom'
print(g.__slots__)


def set_age(self,age):
    self.age = age

s = Student()
from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


# 1、python支持动态给类和实例增加属性和方法；
# 2、python __slots__只能限制实例的属性及方法，对于类则没有影响，对于子类则更是没有限制。

