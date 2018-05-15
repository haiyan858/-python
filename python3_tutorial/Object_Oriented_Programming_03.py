# -*- coding:utf-8 -*-

# Create_Author: cuihaiyan
# Create_time: 2018/5/15 17:09
# Desc:  获取对象信息

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？


# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。

class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

print('ABC'.lower())


class MyObject(object):
    def __init__(self):
        self.x=9

    def power(self):
        return self.x * self.x


# type()
# isinstance() 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# dir() 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
#         仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()



