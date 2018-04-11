import CtrlSocket

s = CtrlSocket.ClientSocket(CtrlSocket.UDPConnection)

host = CtrlSocket.socket.gethostname()
port = 9999

s.connect((host, port))

sendMsg = 'OPENCAST kill'
sendMsg = sendMsg.encode('ascii')
s.broadcast(sendMsg, port)
s.close()
