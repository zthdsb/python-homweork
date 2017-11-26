class Dog(object):
    

    def __init__(self,name):
        self.name=name

    # def eat(self,food):
    #     print("%s is eating %s"%(self.name,food))
     #属性方法：把一个方法变成一个静态属性
    @property
    def eat(self):
        print("%s is eating %s"%(self.name,"dd"))

d=Dog("ZTH")
# d.eat("hanbao")
d.eat