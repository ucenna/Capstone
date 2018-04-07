import CtrlSocket

s = CtrlSocket.ClientSocket()

host = CtrlSocket.socket.gethostname()
port = 9999

s.connect((host, port))

sendMsg = 'kill'
sendMsg = sendMsg.encode('ascii')
s.sendto(sendMsg, ('255.255.255.255', 9999))
s.close()
