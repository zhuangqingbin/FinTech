import socket

udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpSocket.bind(('192.168.199.241', 8077))
while True:
    recvData = udpSocket.recvfrom(1024)
    print(recvData[0].decode('gbk'))
    data = input("Please input:")
    udpSocket.sendto(data, recvData[1])
udpSocket.close()