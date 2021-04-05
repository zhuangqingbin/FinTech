from socket import *
clienSocket = socket(AF_INET, SOCK_STREAM)
clienSocket.connect(('192.168.199.241', 7788))
clienSocket.send(b'hello')
data = clienSocket.recv(1024)
print(data)
clienSocket.close()