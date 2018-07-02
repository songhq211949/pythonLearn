'''
Created on 2018年6月20日

@author: Administrator
'''
def test(number):
    print("调用了test方法")
    def test_in(number_in):
        print(number+number_in)
    return test_in
a=test(100)
a(200)
    