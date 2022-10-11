## 爬取美女网站的多进程

```python
import os

import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor
import threading
import requests

from faker import Faker
from lxml import etree
```

### 使用到了ThreadPoolExecutor线程池和threading线程模块

```python
threa = ThreadPoolExecutor(max_workers=3)  # 设置爬取地址线程
for div in divs:
    img_url = div.xpath('./div/div[1]/div/a/@href')[0]
    print(f"当前爬取到这个了: {img_url}")
    threa.submit(get_img_url, img_url, header)  # 获取当前页面的所有url 传到爬取进程里开始多进程爬取
    time.sleep(0.1)	
```

### 最后打包成可执行文件

#### 第一步：安装打包所需要的包（pyinstaller）

```python
# 在cmd窗口中输入
pip install pyinstaller
# 并从新创建一个环境
 
```

#### 第二步修改路径

#### 第三步：输入打包命令

pyinstaller -F -w (-i icofile) 文件名.py

解释一下该命令：

1、-w 表示在打包好程序后，双击.exe文件不会不会不会（重要的事情说三遍）出现黑色的命令窗口。（如果你的程序有print等输出命令，就不要加）

2、小括号中的内容是可以省略的，-i 表示给.exe文件一个图标，icofile表示图标的文件名，图标的图片格式为.ico格式的。不懂.ico图片的可以百度一下。打包时如果需要给.exe加入图标，将图标文件放到和.py文件同一目录下。

3、文件名.py 这里的文件名是你要打包的.py文件的名称。