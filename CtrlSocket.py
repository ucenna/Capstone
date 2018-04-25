import socket
import ctrlInput

MSGLEN = 1024


def UDPSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class BaseSocket:
    input = ctrlInput.ctrlInput()

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        self.alive = True
        self.name = socket.gethostname()+'(here)'

    def setsock(self, sock):
        self.sock = sock

    def getsock(self):
        return self.sock

    def execute(self, cmd, *args):
        print("## executing: "+cmd)
        print('## cmd: '+cmd)
        # print('## args: '+str(*args))
        try:
            if args:
                result = getattr(self, cmd)(*args)
            else:
                result = getattr(self, cmd)()
            successMsg = str(result)
            if result is None:
                successMsg = 'Success'
            print('## result: '+successMsg)
            return result
        except AttributeError:
            self.input.execute(cmd, *args)

    def setname(self, name):
        self.name = name

    def getname(self):
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
        broadcastSocket = UDPSocket()
        broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        broadcastSocket.sendto(msg, ('<broadcast>', port))
        broadcastSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 0)


class ServerSocket(BaseSocket):
    def bind(self, addr):
        self.sock.bind(addr)

    def listen(self, x):
        self.sock.listen(x)

    def recvbroadcast(self):
        broadcastSocket = UDPSocket()
        broadcastSocket.bind(('0.0.0.0', 9999))
        data, addr = broadcastSocket.recvfrom(1024)
        broadcastSocket.close()
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
