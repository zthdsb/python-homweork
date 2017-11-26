from  multiprocessing import Process, Pool
import time,os

def Foo(i):
    time.sleep(2)
    print("process",os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__=="__main__":  #这行代码表示从这行开始的下面的代码可以直接手动执行，通过模块导入就不会执行下面的代码
    pool = Pool(5) #允许进程池同时放入5个进程
    print("主进程id",os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  #callback 回调Foo执行玩以后就会调用Bar  回调是用的父进程的id
        # pool.apply(func=Foo, args=(i,))  #apply串行
        # pool.apply_async(func=Foo, args=(i,))  #apply_async并行
    # print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。