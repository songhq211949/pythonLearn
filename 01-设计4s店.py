class CarStore(object):
    def order(self,car_type):
        if car_type=="索纳塔":
            #用一个对象里的方法返回对象
            return Suonata()
        elif car_type=="明途":
            return MingTu()

class Car(object):
    def move(self):
        print("车子在移动")
    def music(self):
        print("车子在放音乐")
    def stop(self):
        print("车子在制动")
class Suonata(Car):
    def introduce(self):
        print("我是索纳塔")
class MingTu(Car):
    def introduce(self):
        print("我是明途")
car_store=CarStore()
car=car_store.order("明途")
car.move()
car.music()
car.stop()
car.introduce()