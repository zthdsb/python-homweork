
class Dog:
    def __init__(self,name):
        self.name=name

    def bulk(self):
        print("%s wang wang wang..."%self.name)

d1=Dog("t1")
d2=Dog("t2")
d3=Dog("t3")

d1.bulk()
d2.bulk()
d3.bulk()