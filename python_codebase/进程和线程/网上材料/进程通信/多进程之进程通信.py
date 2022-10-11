from multiprocessing import Process, Queue


def write(q):  # 放入队列

    print('加入队列成功：{}'.format(Process.pid))  # 打印进程pid

    for i in range(10):  # 0~9
        print('往队列放入：{}'.format(i))
        q.put(i)  # 放入


def read(q):  # 读取队列

    print('加入队列成功：{}'.format(Process.pid))  # 打印进程pid

    while True:  # 一有东西 就马上读取
        value = q.get()  # 读取
        print('获取队列中的东西：{}'.format(value))


if __name__ == "__main__":
    # 由于Python的多进程默认无法进行通信   因为是并发执行的
    # 所以要借助别的数据结构
    # 一般用栈 或者 队列

    q = Queue()  # 实例化Queue   队列
    pw = Process(target=write, args=(q,))  # 创建写入进程
    pr = Process(target=read, args=(q,))  # 创建读取进程
    pw.start()  # 启动写入
    pr.start()  # 启动读取

    pw.join()  # 堵塞读取
