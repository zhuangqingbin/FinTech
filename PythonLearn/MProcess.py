from multiprocessing import Process, Pool
import time
def run():
    print('123')
    time.sleep(1)
def run1():
    print('456')
    time.sleep(1)

class MyProcess(Process):
    def run(self):
        n = 2
        while n > 0:
            print(n)
            time.sleep(1)
            n -= 1

def work(num):
    print("Process %s" % str(num))
    time.sleep(1)
if __name__ == '__main__':
    ## 创建形式1：Process
    # p = Process(target=run)
    # p.start()
    # p1 = Process(target=run1)
    # p1.start()
    #
    # # 主进程等待子进程结束
    # p.join()
    #
    # p1.join()
    # ## 创建形式2：子类
    # p3 = MyProcess()
    # p3.start()

    ## 创建进程池
    ### apply_async使用非阻塞方式调用func
    ### applu使用阻塞方式调用func
    pool = Pool()
    for i in range(10):
        pool.apply_async(work, (i, ))
    ### 关闭进程池，不再接受新的请求
    pool.close()
    ### 让主进程等到进程池的所有进程结束，一定要写在close后面
    pool.join()