import socket

MSGLEN = 1024


class ClientSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def recvfrom(self, bufsize):
        msg, addr = self.sock.recvfrom(bufsize)
        sockname = str(self.sock.getsockname())
        remotename = str(addr[0])+str(addr[1].decode('ascii'))
        print('## '+msg.decode('ascii')+' : '+sockname+' <= '+remotename)
        return msg, addr

    def sendto(self, msg, host_port_tuple):
        sockname = str(self.sock.getsockname())
        remotename = str(host_port_tuple)
        print('## '+msg.decode('ascii')+' : '+sockname+' => '+remotename)
        self.sock.sendto(msg, host_port_tuple)

    def connect(self, host_port_tuple):
        self.sock.connect(host_port_tuple)

    def send(self, msg):
        self.sock.send(msg)
        sockname = str(self.sock.getsockname())
        remotename = str(self.sock.getpeername())
        print('## '+msg.decode('ascii')+' : '+sockname+' => '+remotename)

    def recv(self, bufsize):
        msg = self.sock.recv(bufsize)
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

    def bind(self, host_port_tuple):
        self.sock.bind(host_port_tuple)

    def listen(self, x):
        self.sock.listen(x)

    def accept(self):
        socket, addr = self.sock.accept()
        socket = ClientSocket(socket)
        return socket, addr
