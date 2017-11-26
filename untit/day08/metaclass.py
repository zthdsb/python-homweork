class MyType(type):
    def __init__(self,*args,**kwargs):

        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)

print('here...')
class Foo(object):
    __metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__",cls, *args, **kwargs)
        return object.__new__(cls)  #继承父类的__new__方法

f = Foo("Alex")  #正真实例化的时候先走的new ，  new是用来创建实例的
print(object.name)
# print("f",f)
# print("fname",f.name)