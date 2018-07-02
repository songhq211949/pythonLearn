'''
Created on 2018年6月20日

@author: Administrator
'''
from collections import Iterable
a=isinstance({}, Iterable)
print(a)

b=[x for x in range(10)]

c=range(10)
print(c)
print(b)
