import CtrlSocket
import OpenCastCmd
import clientInput

serversocket = CtrlSocket.ServerSocket()
serverControl = clientInput
host = '0.0.0.0'
port = 9999


serversocket.bind((host, port))

# serversocket.listen(5)


while serversocket.alive:
    msg = serversocket.recvbroadcast()
    cmds = OpenCastCmd.process(msg)
    for cmdarr in cmds:
        cmd = cmdarr[0]
        args = cmdarr[1]
        serverControl.execute(cmd, *args)
        serversocket.execute(cmd, *args)
    if msg is 'kill':
        serversocket.alive = False
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
