# class Foo(object):
#     def __init__(self,name):
#         self.name=name
#         print("Foo __init__")
#     def __new__(cls, *args, **kwargs):   #new是用来创建实例的
#         print("Foo __new__")
#
# f=Foo("456")

# f=Foo("alex")
# print(type(f))
# print(type(Foo))





#装配
def func(self):
    print("hello %s"%self.name)
def __init__(self, name,age):
    self.name = name
    self.age=age
Foo=type('Foo',(object,),{'talk':func,
                   '__init__':__init__})
f=Foo("zth",23)
f.talk()
print(type(Foo))


