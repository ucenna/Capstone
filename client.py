import CtrlSocket
import sys

s = CtrlSocket.ClientSocket(CtrlSocket.UDPSocket())

host = CtrlSocket.socket.gethostname()
port = 9999

s.connect((host, port))

sendMsg = 'OPENCAST '+sys.argv[1]
sendMsg = sendMsg.encode('ascii')
s.broadcast(sendMsg, port)
s.close()
