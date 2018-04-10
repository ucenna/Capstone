import CtrlSocket

serversocket = CtrlSocket.ServerSocket(CtrlSocket.UDPConnection)

host = '127.0.0.1'
port = 9999


serversocket.bind((host, port))

# serversocket.listen(5)

alive = True
while alive:
    data, addr = serversocket.recvfrom(1024)
    print('## '+data.decode('ascii')+' : '+str(addr))
    if data.decode('ascii') == 'kill':
        alive = False
    # clientsocket, addr = serversocket.accept()
    # print('## Got Connection')
    # msg = 'Thank you for connecting' + str(addr) + '\r\n'
    # clientsocket.send(msg.encode('ascii'))
    # recvMsg = clientsocket.recv(1024)
    # recvMsg = recvMsg.decode('ascii')
    # if recvMsg == 'kill':
    #     print('## killing self')
    #     alive = False
    # clientsocket.close()
