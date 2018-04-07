import CtrlSocket

serversocket = CtrlSocket.ServerSocket()

port = 9999

serversocket.bind('0.0.0.0', port)

serversocket.listen(5)

alive = True
while alive:
    clientsocket, addr = serversocket.accept()

    msg = 'Thank you for connecting' + str(addr) + '\r\n'
    # clientsocket.send(msg.encode('ascii'))
    recvMsg = clientsocket.recv(1024)
    recvMsg = recvMsg.decode('ascii')
    if recvMsg == 'kill':
        print('## killing self')
        alive = False
    clientsocket.close()
