# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/8/1519:33
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : demo-入门.py
__author__ = 'Small Fu'

import asyncio, time
from pyppeteer import launch


async def main():
    browser = await launch(headless=False, dumpio=True, autoClose=False,userDataDir = './',
                           args=['--no-sandbox', '--window-size=1920,1080', '--disable-infobars'])   # 进入有头模式

    page = await browser.newPage()           # 打开新的标签页
    await page.setViewport({'width': 1920, 'height': 1080})      # 页面大小一致
    await page.goto('https://www.baidu.com') # 访问主页
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    time.sleep(2)

    print(await page.content())
    await page.screenshot({"path": 'example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
