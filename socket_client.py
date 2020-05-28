import socket

client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_server.connect(('127.0.0.1', 10048))

while True:
    data = input("Enter Data: ")
    client_server.send(data.encode())

    server_data = client_server.recv(1024)
    # if(server_data == ''): break
    if(server_data == ''): break
    if(data == 'bye'): break
    print("[+] Server Send: ", server_data.decode())

client_server.close()