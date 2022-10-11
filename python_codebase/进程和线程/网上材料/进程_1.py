from multiprocessing import Process
import time


def aa(a):
    for i in range(a):
        print('子进程')
        print('-'*100)
        time.sleep(1)
    pass


if __name__ == '__main__':
    p = Process(target=aa, args=(5,))
    p.start()
    p.join(1)
    while True:
        print('父进程')
        time.sleep(1)
