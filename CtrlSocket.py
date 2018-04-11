import socket

MSGLEN = 1024
UDPConnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class BaseSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.setSock(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        else:
            self.setSock(sock)
        self.alive = True
        self.name = socket.gethostname()+'(here)'

    def setSock(self, sock):
        self.sock = sock

    def execute(self, cmd):
        print("## executing: "+cmd)
        try:
            result = getattr(self, cmd)()
            successMsg = str(result)
            if result is None:
                successMsg = 'Success'
            print('## result: '+successMsg)
            return result
        except AttributeError:
            print('## result: No such cmd')

    def getSock(self):
        return self.sock

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def kill(self):
        print('## killing self')
        self.alive = False

    def close(self):
        self.sock.close()

    def send(self, msg):
        self.sock.send(msg)
        remotename = str(self.sock.getpeername())
        print('## '+msg.decode('ascii')+' : '+self.name+' => '+remotename)

    def recv(self, bufsize):
        msg = self.sock.recv(bufsize)
        remotename = str(self.sock.getpeername())
        print('## '+msg.decode('ascii')+' : '+self.name+' <= '+remotename)
        return msg

    def recvfrom(self, bufsize):
        msg, addr = self.sock.recvfrom(bufsize)
        remotename = str(addr)
        print('## '+msg.decode('ascii')+' : '+self.name+' <= '+remotename)
        return msg, addr


class ClientSocket(BaseSocket):
    def sendto(self, msg, addr):
        remotename = str(addr)
        print('## '+msg.decode('ascii')+' : '+self.name+' => '+remotename)
        self.sock.sendto(msg, addr)

    def connect(self, addr):
        self.sock.connect(addr)

    def send(self, msg):
        self.sock.send(msg)
        remotename = str(self.sock.getpeername())
        print('## '+msg.decode('ascii')+' : '+self.name+' => '+remotename)

    def recv(self, bufsize):
        msg = self.sock.recv(bufsize)
        remotename = str(self.sock.getpeername())
        print('## '+msg.decode('ascii')+' : '+self.name+' <= '+remotename)
        return msg

    def broadcast(self, msg, port=None):
        if port is None:
            port = self.port
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sendto(msg, ('<broadcast>', port))
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 0)


class ServerSocket(BaseSocket):
    def bind(self, addr):
        self.sock.bind(addr)

    def listen(self, x):
        self.sock.listen(x)

    def ListenForBroadcast(self):
        data, addr = self.recvfrom(1024)
        msg = None
        try:
            msg = data.decode('ascii')
        except UnicodeDecodeError:
            return
        return msg

    def accept(self):
        socket, addr = self.sock.accept()
        socket = ClientSocket(socket)
        return socket, addr
