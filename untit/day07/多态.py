class Animal(object):
    def __init__(self,name):
        self.name=name
    def talk(self):
        print("%s is talking "%self.name)

    def all_talk(obj):   #多态
        obj.talk()


class Dog(Animal):
    def talk(self):
        print("%s is talking WangWangWang... "%self.name)

class Cat(Animal):
    def talk(self):
        print("%s is talking MiaoMiaoMiao... "%self.name)


d=Dog("ZTH")
c=Cat("WBD")
d.talk()
c.talk()


Animal.all_talk(d)   #多态
Animal.all_talk(c)
