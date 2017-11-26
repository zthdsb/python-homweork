#客户端
import socket
client=socket.socket()  #1.实例化一个socket
#2.连接
client.connect(('localhost',9999))
#3.发送数据
while True:
    cmd=input(">>>>:").strip()  #strip()是用来除去输入中包含的空格，回车等多余的字符，只留下字符串
    if len(cmd) == 0: continue
    client.send(cmd.encode('utf-8'))
    cmd_rec_size= client.recv(1024)   #接受命令结果的长度
    print("命令结果长度：",cmd_rec_size)
    receive_size=0
    receive_data=b''
    while receive_size < int(cmd_rec_size.decode()):
        data=client.recv(1024)
        receive_size += len(data)  #每次收到的可能小于1024，所以必须用len判断
        receive_data+=data
        print(receive_size)

    else:
        print("命令执行完毕！",receive_size)
        print(receive_data.decode())
    # print(receive_data.decode())

