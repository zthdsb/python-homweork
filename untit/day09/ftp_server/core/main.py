import socketserver
import json,os
class MyTCPHandler(socketserver.BaseRequestHandler):
    def put(self,*args):
        '''接受客户端文件'''
        cmd_dic=args[0]
        filename=cmd_dic["filename"]
        filesize=cmd_dic["size"]
        if os.path.isfile(filename):
            f=open(filename+".new","wb")
        else:
            f=open(filename,"wb")
        self.request.sendall(b"200 ok")
        received_size=0
        while received_size<filesize:
            data=self.request.recv(1024)
            f.write(data)
            received_size+=len(data)
        else:
            print("file %s has uploade"%filename)


    def handle(self):
        while True:
            try:
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic= json.loads(self.data.decode())
                action=cmd_dic["action"]
                if hasattr(self,action):
                    func= getattr(self,action)
                    func(cmd_dic)

                # just send back the same data, but upper-cased
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  #ThreadingTCPServer支持多线程，多并发
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()