import socket


mysocket = socket.socket()

host = '192.168.1.104'
port = 12345


mysocket.connect((host,port))


while True : 
    smsg = mysocket.recv(1024).decode()
    print(f"server-->{smsg}".rjust(200))

    cmsg = input("client-->")
    cmsg = "client-->"+cmsg
    mysocket.send(cmsg.encode())

    if cmsg.lower() == 'bye' or smsg.lower() == 'bye' : 
        mysocket.close()
