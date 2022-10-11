import _thread
from time import sleep, ctime


def loop(thread1, nsec, lock):
    print('线程'+str(thread1)+' 开始:'+ctime()+'\n')
    print('线程%d挂起%d秒' % (thread1, nsec))
    sleep(nsec)
    print('线程', thread1, '结束：', ctime())
    lock.release()


def main():
    print('主程序开始')
    locks = []  # 锁列表
    threads = range(0, 3)
    wait = [4, 2, 1]  # 子线程的等待时间
    for i in threads:
        lock = _thread.allocate_lock()  # 分配一个locktype 类型的锁对象
        lock.acquire()  # 尝试获取锁对象
        locks.append(lock)
    for i in threads:
        # 用来生产新的线程
        _thread.start_new_thread(loop, (i + 1, wait[i], locks[i]))
    for i in threads:
        while locks[i].locked():pass   # 检查每一个子进程的加锁状态
    print('已经释放了所有的锁所有的子进程结束:' , ctime())


if __name__ == '__main__':
    main()