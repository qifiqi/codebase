import threading
from time import sleep, ctime


class MyThread(threading.Thread):  # 定义一个继承threading。thread的子类
    def __init__(self, num):  # 重载init含税
        super().__init__()  # 调用父类的init函数
        self.num = num

    def run(self) -> None:  # 重载了run函数
        sleep(2)
        print('同学%d说:现在是：' % self.num, ctime(), '\n')


if __name__ == '__main__':
    a = MyThread(2)  # 创建子类对象
    b = MyThread(3)
    a.start()  # 启动
    b.start()
