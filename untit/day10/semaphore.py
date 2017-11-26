import threading,time
def run(n):
    semaphore.acquire()
    # global num
    # num+=1
    time.sleep(1)
    print("run the thread %s"%n)
    semaphore.release()


if __name__=="__main__":
    num =0
    semaphore= threading.BoundedSemaphore(5)  #最多允许五个线程进行
for i in range(20):
    t=threading.Thread(target=run,args=(i,))
    t.start()
while threading.active_count() !=1:
    pass

    # print(threading.active_count())
print("num is ",num)