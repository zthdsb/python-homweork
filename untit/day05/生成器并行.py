import time
def consumer(name):
    print("%s 准备吃包子了！"%name)
    while True:
        baozi=yield
        print("包子[%s]来了，被[%s]吃了！"%(baozi,name))
c=consumer("ChenRonghua")
c.__next__()  #next只是唤醒yield
b1="韭菜馅"
c.send(b1) #send是唤醒yield，并给yield传一个值
 

def producer(name):
    c=consumer("A")
    c2=consumer("B")
    c.__next__()
    c2.__next__()
    print("老子开始做包子了啊")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子分两半！")
        c.send(i)
        c2.send(i)
producer("Alex")