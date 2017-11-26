import threading,time
def run(n):
    print('task',n)
    time.sleep(2)
    print("task done",n,threading.current_thread())
start_time=time.time()
t_obje=[]   #存线程实例
for i in range(20):
    t=threading.Thread(target=run,args=('t-%s'%i,))  #第一个参数是线程函数变量，第二个参数args是一个数组变量参数，如果只传递一个值，就只需要i, 如果需要传递多个参数，那么还可以继续传递下去其他的参数，其中的逗号不能少，少了就不是数组了，就会出错。
    t.setDaemon(True)  #把当前的线程设置为守护线程，执行时不等当前线程执行完，只等主线程执行完
    t.start()
    t_obje.append(t)

# for t in t_obje:
#     t.join()

print("-----all threads has finished---",threading.current_thread(),threading.active_count())
print(time.time()-start_time)

#线程模式执行
# t1=threading.Thread(target=run,args=("t1",))
# t2=threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()


#普通函数模式执行
# run(1)
# run(2)