import socket
server_socket = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 12345
server_socket.bind((host,port))
print("Server is ready to listen for clients as {}:{}".format(host,port))
server_socket.listen()
client_socket,client_addr = server_socket.accept()
while True :
    msg = input("server->")
    client_socket.send(msg.encode())
    cl_msg = client_socket.recv(1024)
    print("\t\t\tclient->",cl_msg.decode())
    if ( msg.lower() == 'bye' ) or ( cl_msg.decode() == 'bye' ) :
        client_socket.close()
        server_socket.close()
        break

