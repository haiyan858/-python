# -*- coding:utf-8 -*-

# Create_Author: cuihaiyan
# Create_time: 2018/5/16 11:48
# Desc: 装饰器（decorator）


# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
#
# s = Student()
# s.set_score(66)
# print(s.get_score())
#
# s.set_score(999)
'''
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print(s.score)

s.score = 9999

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
'''

# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature
#
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

# c = Celsius()
# print(c.to_fahrenheit())

# https://www.programiz.com/python-programming/property

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# -*- coding: utf-8 -*-

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height



# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')


