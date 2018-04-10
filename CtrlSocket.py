import socket

MSGLEN = 1024
UDPConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class BaseSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def close(self):
        self.sock.close()

    def recvfrom(self, bufsize):
        msg, addr = self.sock.recvfrom(bufsize)
        # sockname = str(self.sock.getsockname())
        # remotename = str(addr[0])+str(addr[1].decode('ascii'))
        # print('## '+msg.decode('ascii')+' : '+sockname+' <= '+remotename)
        return msg, addr


class ClientSocket(BaseSocket):
    def sendto(self, msg, host_port_tuple):
        sockname = 'here'
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


class ServerSocket(BaseSocket):
    def bind(self, host_port_tuple):
        self.sock.bind(host_port_tuple)

    def listen(self, x):
        self.sock.listen(x)

    def accept(self):
        socket, addr = self.sock.accept()
        socket = ClientSocket(socket)
        return socket, addr
