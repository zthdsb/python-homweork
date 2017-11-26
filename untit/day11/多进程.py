import multiprocessing
import threading,time
def thread_run():
    print(threading.get_ident())
def run(n):
    time.sleep(2)
    print("hello world",n)
    t = threading.Thread(target=thread_run)
    t.start()

if __name__== "__main__":
    for i in range(10):
        m=multiprocessing.Process(target=run,args=(i,))
        # t=threading.Thread(target=thread_run)
        m.start()
        # t.start()
