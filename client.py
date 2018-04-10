import CtrlSocket

s = CtrlSocket.ClientSocket(CtrlSocket.UDPConnection)

host = CtrlSocket.socket.gethostname()
port = 9999

# s.connect((host, port))

sendMsg = 'kill'
sendMsg = sendMsg.encode('ascii')
s.sendto(sendMsg, (host, port))
s.close()
