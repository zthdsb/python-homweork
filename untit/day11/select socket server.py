# select()通过单进程实现同时处理多个非阻塞的socket连接
import socket
import select
import queue

server=socket.socket()
server.bind(("localhost",9000))
server.listen(1024)

server.setblocking(False)  #不阻塞
inputs=[server,]  #把内核需要检测的连接都放入input中
#inputs=[server,conn]  执行append命令就会添加一个conn，
outputs=[]
msg_dic={}
while True:
    readable,writeable,exceptional=select.select(inputs,outputs,inputs)#出现一个新连接就给readable，出现错误就给exceptional，中间参数先不管
    print(readable,writeable,exceptional)

    for r in readable:
        if r is server:#代表来个新连接
            conn,addr=server.accept()
            print("来了个新连接",addr)
            inputs.append(conn) #因为现在建的新连接还没有发数据过来，现在就接受的话就会报错，所以要是想实现这个客户端发数据过来时server端能知道，就需要让select再监测这个conn
            msg_dic[conn]=queue.Queue() #初始化一个队列，后面存要返回给这个客户端的数据
        else:
            data=r.recv(1024)
            print("收到数据",data)
            msg_dic[r].put(data)
            outputs.append(r)#放入返回的连接队列里

            # r.send(data)
    for w in writeable:  #要返回给客户端的连接列表
        data_to_client=msg_dic[w].get()
        w.send(data_to_client) #返回给客户端源数据
        outputs.remove(w)  #确保下次循环的时候writeable，不返回已经处理完的过程
    for e in exceptional:
        if e in outputs:
            outputs.remove(e)
        inputs.remove(e)
        del msg_dic[e]