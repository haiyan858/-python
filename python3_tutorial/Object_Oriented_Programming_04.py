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


class Student(object):
    count = 0
    # 【0】Student类的变量
    def __init__(self):
        count = 1              # 【1】init方法内部的一个临时变量
        self.count = 1         # 【2】创建实例后变为 实例的一个参数/变量
        self.count = count + 1 #  相当于【2】=【1】+ 1，所以最后【2】 == 2
        Student.count = 3      # 【3】Student类的变量， 与最上边的【0】是同一个东西

a = Student()
print(a.count, Student.count)  # 输出结果为 2 3

# 总结一下：
# 四个count：【0】和【3】等价且为类的变量/参数，【1】是临时变量，【2】是实例的参数