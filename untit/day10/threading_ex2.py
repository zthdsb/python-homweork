import threading,time
class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()
        self.n=n
        self.sleep_time=sleep_time
    def run(self):
        print("run tasking",self.n)
        time.sleep(self.sleep_time)
        print("thread done ",self.n)
t1=MyThread("t1",2)
t2=MyThread("t2",4)
# t1.start()
# t1.join()#=wite  等待第一个线程执行完了以后再执行下一个线程，这样就变成串行执行的了
# t2.start()

#线程1和线程2先都启动执行，然后等待第一个线程的结果，执行完以后打印
t1.start()
t2.start()
t1.join()
print("main done...")