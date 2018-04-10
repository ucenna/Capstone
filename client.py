import CtrlSocket

s = CtrlSocket.ClientSocket(CtrlSocket.UDPConnection)

host = '127.0.0.1'
port = 9999

# s.connect((host, port))

sendMsg = 'kill'
sendMsg = sendMsg.encode('ascii')
s.sendto(sendMsg, (host, port))
s.close()
