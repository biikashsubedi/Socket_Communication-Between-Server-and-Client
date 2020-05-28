import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('127.0.0.1',10048))

server_socket.listen(10)
print("[+] Listning For Connection on 127.0.0.1:5090..")

while True:
    conn, addr = server_socket.accept()
    print(f'[+] Got Connection Form {addr}')

    while True:
        data = conn.recv(1024)
        # if(data == ''): break
        if (data.decode() == 'bye'): break
        print("[+] Client Sent:", data.decode())

        data = input("Enter Data: ")
        conn.send(data.encode())

    conn.close()
    print("[+] Client Disconnected")