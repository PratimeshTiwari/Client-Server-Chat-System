import socket 

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #AF Address Family #SockStream:TCP
server_socket.bind(('127.0.0.1',8888))  #local address 

#converting to passive socket server
server_socket.listen(10)  #simultaneous listen request 
print("Listening for connections on 127.0.0.1:8888...")

#accepting client request
while True:
    connection,address = server_socket.accept()
    print(f"Connection received from {address}")
    while True: #for individual client request 
        data = connection.recv(1024)   #bytes to receive over network
        if(data=='end'):
            break
        print("Client sent :",data.decode())   #UTF8 data is converted to string using .decode()
        server_data=input("Enter data to send:")
        connection.send(server_data.encode())
    connection.close()  