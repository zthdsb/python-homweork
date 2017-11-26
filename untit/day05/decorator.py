import time
def timer(func):   #func=text1
    def deco(*agre,**kwargs):   #当（）里边加上*arge和**kwargs的时候就可以装饰所有的函数，无论函数有没有参数
        start_time=time.time()
        func(*agre,**kwargs)   #运行func（）这个程序
        stop_time=time.time()
        print("the fun run time is %s"%(stop_time-start_time))
    return deco

@timer
def text1():
    time.sleep(3)
    print("in the text1")
@timer   #等同于text1=timer(text1)
def text2(name,age):
    time.sleep(3)
    print("text2:",name,age)

#print(timer(text1)) #返回的是deco的地址
text1()
text2("alse",45)
# text1=timer(text1)
# text1()