import socket

MSGLEN = 1024


class ClientSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        self.sock.send(msg)
        sockname = str(self.sock.getsockname())
        remotename = str(self.sock.getpeername())
        print('## '+msg.decode('ascii')+' : '+sockname+' => '+remotename)

    def recv(self, length):
        msg = self.sock.recv(length)
        sockname = str(self.sock.getsockname())
        remotename = str(self.sock.getpeername())
        print('## '+msg.decode('ascii')+' : '+sockname+' <= '+remotename)
        return msg

    def close(self):
        self.sock.close()


class ServerSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def bind(self, host, port):
        self.sock.bind((host, port))

    def listen(self, x):
        self.sock.listen(x)

    def accept(self):
        socket, addr = self.sock.accept()
        socket = ClientSocket(socket)
        return socket, addr
