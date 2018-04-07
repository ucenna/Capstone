import CtrlSocket

s = CtrlSocket.ClientSocket()

host = CtrlSocket.socket.gethostname()
port = 9999

s.connect(host, port)

sendMsg = 'kill'
sendMsg = sendMsg.encode('ascii')
s.send(sendMsg)
s.close()
