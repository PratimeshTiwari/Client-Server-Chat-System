import socket 
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',8888))
print("Trying to connect to 127.0.0.1:8888")
while True:
    data = input("Enter data to send :") #sending data to server
    client_socket.send(data.encode())

    server_data=client_socket.recv(1024)
    if(server_data=='end'):
        break
    if(data=='end'):
        break
    print("Server sent : ",server_data.decode())

client_socket.close()
