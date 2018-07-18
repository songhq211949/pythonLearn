class Dog(object):
    def print_self(self):
        print("大家好，我是xxx,以后请多多关照")

class Xiaotq(Dog):
    def print_self(self):
        print("大家好，我是你们的老大")

def introduce(temp):
    "动态类型的语言"
    temp.print_self()
dog1=Xiaotq()
dog2=Dog()
introduce(dog1)
introduce(dog2)
