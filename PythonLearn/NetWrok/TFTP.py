# 简单文件传输协议
## 使用这个协议可以实现简单文件的下载 tftp的端口号为69
## 基于UDP
## 实现一个TFTP下载器
## 下载：从服务器将一个文件复制到本机上
## 下载的过程：
##   在本地创建一个空文件（与服务器文件同名）
##   向里面写数据（接受一点写一点
##   关闭（接受完所有文件就关闭

import struct
# struct模块可以将python数据按照指定格式转为字符串（字节流
# 1、pack按照给定的格式，把数据封装成字符串（类似c结构的字节流
# 2、unpack按照给定的格式解析字节流，返回解析出来的元组
# 3、calsize计算给定的格式占用多少字节的内存
cmb_buf = "1.png"
# !表示按照网络传输数据要求的形式来组织数据
# H表示将后面的1替换成占两个字节
# 8s相当于8个s占8个字节
# b 占一个字节
cmb_buf = struct.pack("!H8sb5sb", 1, b"test.png", 0, b"octet",0)


from socket import *
filename = 'test.png'
server_ip = '192.168.199.241'

cmb_buf = struct.pack("!H%dsb5sb" % len(filename), 1, filename.encode(), 0, "octet".encode(), 0)
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.sendto(cmb_buf, (server_ip, 8083))
f = open(filename, 'ab')
while True:
    recvData = udpSocket.recvfrom(1024)
    operate_id, ack_id = struct.unpack("!HH", recvData[0][:4])
    rand_port = recvData[1][1]
    if int(operate_id) == 5:
        print("文件不存在")
        break
    print("操作码: %d, ACK: %d, 服务器随机端口号: %d, 数据长度: %d" % (operate_id, ack_id, rand_port, len(recvData)))
    f.write(recvData[0][4:])
    if len(recvData[0][4:]) < 516:
        break
    ack_data = struct.pack("!HH", 4, ack_id)
    # 客户端向服务器发送ack确认包
    udpSocket.sendto(ack_data, (server_ip, rand_port))