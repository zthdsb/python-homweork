#服务器
import socket,os
server=socket.socket()   #1.实例化一个socket
server.bind(('localhost',9999))  #2.绑定IP地址和客户端

server.listen()  #3.开始监听

while True:
    coon,addr=server.accept()  #开始阻塞，接受
    print("new coon:",addr)   #输出接受的IP地址
    while True:
        print("接受新的指令")
        data=coon.recv(1024)    #接受数据
        if not data:
            print("客户端已断开")
            break
        print("客户端执行命令：",data)
        cmd_res=os.popen(data.decode()).read()  #接受字符串，执行结果也是字符串
        print("before send",len(cmd_res))
        if cmd_res == 0:
            cmd_res="cmd has no output"
        coon.send(  str(len(cmd_res.encode())).encode('utf-8')  )  #先把大小发给客户端
        coon.send(cmd_res.encode('utf-8'))   #发回客户端
        print("send done")