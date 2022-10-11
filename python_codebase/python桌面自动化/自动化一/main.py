# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/2012:32
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : main.py
# @Software: PyCharm
import pyautogui
import pyttsx3
import threading

size_dict = {
    'min': (1754, 27),
    'quit': (1898, 16),
    'bottom_edge': (210, 1050),
    'bottom_google': (270, 1050),
    'bottom_firefox': (330, 1050),
    'bottom_fileSystem': (390, 1050),
    'bottom_kugo': (450, 1050),
    'bottom_vscode': (510, 1050),
    'bottom_notbook': (580, 1050),
    'bottom_wx': (640, 1050),
    'bottom_qq': (700, 1050),
    'bottom_blbl': (760, 1050),
    'pycharm': (139, 865),

}


class AutoGui:
    # 设置全局停顿时间
    pyautogui.PAUSE = 0.5

    def cli(self):
        # 点击,左键点击两下
        pyautogui.click(clicks=2)

    def move(self, sizes, times):
        # 移动,根据绝对坐标
        pyautogui.moveTo(*sizes, duration=times)

    def hokeys(self, loc):
        pyautogui.hotkey('win', loc)
        pyautogui.press('enter')

    def pycharm(self):
        # 根据图片识别找到pycharm的坐标
        # size_dict['pycharm'] = pyautogui.locateCenterOnScreen('./pycharm.png')
        # print(size_dict['pycharm'] )
        # 移动,根据绝对坐标
        self.move(size_dict['pycharm'], 1)
        # 点击
        self.cli()

    def cli_bottom(self, sizes=(0, 0), times=1, loc='left'):
        # 移动,根据绝对坐标
        self.move(sizes, times)
        # 点击
        self.cli()
        # 移动位置
        self.hokeys(loc)


def main():
    autogui = AutoGui()
    # pycharm
    autogui.pycharm()
    # # edge
    autogui.cli_bottom(size_dict['bottom_edge'], 1)
    pyautogui.sleep(1)
    # # notbook
    autogui.cli_bottom(size_dict['bottom_notbook'], 0.5, 'right')
    pyautogui.sleep(1)
    # # blbl
    autogui.cli_bottom(size_dict['bottom_blbl'], 0.5, 'up')


def output_voice(text):
    weather = pyttsx3.init()  # 初始化说话的对象
    weather.say(text)  # 设置说话内容
    weather.runAndWait()  # 开始执行说话的操作


if __name__ == '__main__':
    threading.Thread(target=output_voice, args=('是否打开工作模式',)).start()
    aa = pyautogui.confirm(text='是否打开工作模式',title='工作模式', buttons=['是', '否'])
    pyautogui.sleep(1)
    threading.Thread(target=output_voice, args=(aa,)).start()
    main()
    threading.Thread(target=output_voice, args=('工作模式打开完成',)).start()
