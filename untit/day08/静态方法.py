class Dog(object):
    def __init__(self,name):
        self.name=name

    # def eat(self,food):
    #     print("%s is eating %s"%(self.name,food))
     #静态方法
    @staticmethod
    def eat(self,food):
        print("%s is eating %s"%(self.name,food))

d=Dog("ZTH")
# d.eat("hanbao")
Dog.eat(d,"miantiao")