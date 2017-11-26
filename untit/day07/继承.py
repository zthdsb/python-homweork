
# class People:  #经典类
class People(object): #新式类
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.friends=[]
    def eat(self):
        print("%s is eating"%self.name)
    def sleep(self):
        print("%s is sleeping"%self.name)
    def talk(self):
        print("%s is talking"%self.name)

class Relation(object):
    def make_friends(self,obj):
        print("%s make friend with %s"%(self.name,obj.name))
        self.friends.append(obj)
class Man(People,Relation):  #继承
    def __init__(self,name,age,money):
        super(Man, self).__init__(name,age) #新式类写法 #该行和下一行都是继承父类的方法
        #People.__init__(self,name,age)
        self.money=money
        print("%s一出生就有%s money"%(self.name,self.money))

    def piao(self):
        print("%s is piaoing...."%self.name)
    def sleep(self):
        People.sleep(self)  #这样也能执行父类的函数
        print("man is sleeping")
    pass


class Women(People,Relation):
    def get_baby(self):
        print("%s is born a baby"%self.name)


m1=Man("chenronghua",12,100)
# m1.eat()
# m1.piao()
# m1.sleep()


m2=Women("lilei",32)
# m2.get_baby()
m1.make_friends(m2)
print(m1.friends[0].name)