'''
抽象基类(Abstract Base Class, ABC) - 第一版
'''

from collections import abc
print(issubclass(tuple, abc.Sequence))
print(issubclass(list, abc.MutableSequence))