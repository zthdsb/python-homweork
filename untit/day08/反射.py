def bulk(self):
    print("%s is yelling " % self.name)
    
class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print("%s is eating %s"%(self.name,food))

d=Dog("ZTH")
choise=input(">>>:").strip()

# print(hasattr(d,choise))
# print(getattr(d,choise))

if hasattr(d,choise): #hasattr ,判断一个对象d里是否有对应的choise字符串的方法
    # delattr(d,choise)    删除方法
    fun=getattr(d,choise)   #根据字符串获取d里边对应的方法的内存地址
    fun("baozi")
else:
    setattr(d,choise,bulk)  #setattr(x, 'y', v) is equivalent to ``x.y = v''
    fun = getattr(d, choise)
    fun(d)

