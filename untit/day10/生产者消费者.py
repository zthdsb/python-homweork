import threading,queue,time

def Produce(name):
    count = 1
    while True:
        q.put("[%s]骨头"%count)
        print("生产了骨头%s"%count)
        count+=1
        time.sleep(0.5)
def Consumer(name):
    while True:
        c=q.get()
        print("[%s]吃到骨头了%s"%(name,c))
        time.sleep(1)

q=queue.Queue()

p=threading.Thread(target=Produce,args=("ZTH",))
c=threading.Thread(target=Consumer,args=("cccc",))
c1=threading.Thread(target=Consumer,args=("dddd",))

p.start()
c.start()
c1.start()