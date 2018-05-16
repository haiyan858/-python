# -*- coding:utf-8 -*-

# Create_Author: cuihaiyan
# Create_time: 2018/5/16 11:00
# Desc:  类的属性和实例的属性

# class Student(object):
#     def __init__(self,name):
#         self.name = name
#
#
# s = Student('Tom')
#
# print(s.name)

# 为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1 # Student.count 类属性


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart') # 创建实例 bart
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

