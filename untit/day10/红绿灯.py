import threading,time

event=threading.Event()
# count=0
event.set()
def light():
    count = 0
    while True:
        if count>5 and count<10:
            event.clear()
            print("\033[41;1m ---The red light is lighting---\033[0m")
        elif count>10:
            event.set()
            print("\033[42;1m ---The green is lighting---\033[0m")
            count=0
        else:
            print("\033[42;1m ---The green is lighting---\033[0m")
        time.sleep(1)
        count +=1
def car(name):
    while True:
        if event.is_set():  #代表事件是否设定 ，绿灯
            print("[%s] the car see the light is green,running---"%name)
            time.sleep(1)
        else:
            print("[%s] the car see the light is red,waiting---"%name)
            event.wait()


light =threading.Thread(target=light)
light.start()
car=threading.Thread(target=car,args=("tesla",))
car.run()