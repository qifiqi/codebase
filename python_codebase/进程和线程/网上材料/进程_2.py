from multiprocessing import Process
import time


class NewProcess(Process):
    def run(self) -> None:
        while True:
            print('子进程')
            print('-'*100)
            time.sleep(1)


if __name__ == '__main__':
    p = NewProcess()
    p.start()

    while True:
        print('父进程')
        time.sleep(1)
