from socket import *
from multiprocessing import *
from time import sleep

def dealWithClient(newSocket, destAdrr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData) > 0:
            print('recv[%s]: %s' % (str(destAdrr), recvData))
        else:
            print('[%s]客户端已经关闭' % str(destAdrr))
            break
    newSocket.close()

def main():
    serSock = socket(AF_INET, SOCK_STREAM)
    socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    locaAddr = ('', 7788)
    serSock.bind(locaAddr)
    serSock.listen(5)
    try:
        while True:
            print('-----主进程，等待新客户端的到来-----')
            newSock, destAddr = serSock.accept()
            print('-----主进程，接下来创建一个新的进程负责处理数据-----')
            client = Process(target=dealWithClient, args=(newSock,destAddr))
            client.start()
            newSock.close()
    finally:
        serSock.close()

if __name__ == '__main__':
    main()
