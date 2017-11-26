import threading

def run(n):
    lock.acquire()  #线程锁，保证锁里边的线程是按照串行的方式进行
    global num
    num+=1
    lock.release()
num =0
t_abj=[]
lock=threading.Lock()
for i in range(20):
    t=threading.Thread(target=run,args=("t-%s"%i,))
    t.start()
    t_abj.append(t)
for t in t_abj:
    t.join()

print("num",num)
