#客户端
import socket

client=socket.socket()  #声明socket类型，同时生成socket连接对象
client.connect(('localhost',9000))

while True:
    msg=input(">>>:").strip()
    client.sendall(msg.encode("utf-8"))
    data=client.recv(1024)
    print(data)
    # print("recv:",data.decode())
client.close()
