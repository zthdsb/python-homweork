'''#高阶函数 1.
import time
def bar():
    time.sleep(2)
    print("the import thing is xuexi")

def text(fun):
    start_time = time.time()
    #print(fun)
    fun()
    stop_time = time.time()
    print("the bar runing time is %s"%(stop_time-start_time) )
text(bar)
'''


import time
def bar():
    time.sleep(2)
    print("the import thing is xuexi")
def text2(func):
    print(func)
    return func
t=text2(bar)#t获取了返回来的地址
print(t)
t()