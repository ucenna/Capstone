import CtrlSocket

serversocket = CtrlSocket.ServerSocket()

host = '0.0.0.0'
port = 9999
print(host)

serversocket.bind((host, port))

serversocket.listen(5)

alive = True
while alive:
    clientsocket, addr = serversocket.accept()
    print('## Got Connection')
    msg = 'Thank you for connecting' + str(addr) + '\r\n'
    clientsocket.send(msg.encode('ascii'))
    recvMsg = clientsocket.recv(1024)
    recvMsg = recvMsg.decode('ascii')
    if recvMsg == 'kill':
        print('## killing self')
        alive = False
    clientsocket.close()
