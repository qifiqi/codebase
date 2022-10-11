import multiprocessing  # 进程包
import time

def start():
    time.sleep(2)  # 让程序沉睡 2 秒
    print(multiprocessing.current_process().name)  # 打印进程名字
    print(multiprocessing.current_process().pid)  # 打印pid
    print(multiprocessing.current_process().is_alive())  # 打印进程是否活着


if __name__ == "__main__":
    print('程序开始')
    p = multiprocessing.Process(target=start)  # 只用写函数名  不要加括号
    p.start()  # 开始
    p.join()  # 堵塞
    print('程序结束')
