import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def handle(self):
        while True:
            try:
                # self.request is the TCP socket connected to the client
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                # if self.data==0:  #代表服务器断开了
                #     print(self.client_address,"断开了")
                #     break
                print(self.data)
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