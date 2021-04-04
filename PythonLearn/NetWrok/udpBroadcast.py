# 广播 - 当前网络所有的电脑某个进程都能收到同样的数据，TCP里无
## 广播方 - 交换机（如果收到的是广播地址） - 接受方1、2、3、4
## 用hub会导致广播风暴
## MAC地址（物理地址、实际地址，唯一），交换机进行过通信之后就会记录电脑的MAC地址

from socket import  *
dest = ("<broadcast>", 8080)
s = socket(AF_INET, SOCK_DGRAM)
# 重新设置套接字选项 让他可以发送广播数据
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

s.sendto(b'Hello', dest)
while True:
    s.recvfrom()

# 路由器（确定一条路径的设备
## 连接因特网当中网络号不同的不同的网络用的，相当于一个中间人，根据信道的作用自动的选择和设定路由，以最佳方式发送数据