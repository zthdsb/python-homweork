#服务器端
import socket
server = socket.socket()
server.bind(('10.67.1.200',6969))     #绑定要监听的端口

server.listen()#监听
print("我要开始等电话了")
while True:
    conn, addr = server.accept()  # 等电话打进来
    # conn就是客户端连接过来而在服务器端为其生成一个连接实例
    print(conn, addr)
    print("电话来了")
    
    while True:
        data=conn.recv(1024)
        print("recv:",data)
        conn.send(data.upper())

server.close()