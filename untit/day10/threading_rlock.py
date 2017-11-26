import threading
def run1():
    print("this is runing first thread")
    lock.acquire()
    global num
    num +=1
    lock.release()
    return num
def run2():
    print("this is runing second thread")
    lock.acquire()
    global num1
    num1 +=1
    lock.release()
    return num1
def run3():
    lock.acquire()
    r1=run1()
    print("this is betwern run1 and run2")
    r2=run2()
    lock.release()
    print(r1,r2)

if __name__=="__main__":
    num,num1=0,0
    # t_obj=[]
    lock=threading.RLock()
    for i in range(10):
        t=threading.Thread(target=run3)
        t.start()
while threading.active_count() !=1:
    print(threading.active_count())
else:
    print("----all thread has done----")
    print("mum",num,num1)