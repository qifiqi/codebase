# Python_gadgets
自己的写的关于python模块的小玩意

## faker

​	用于自动生成一下随机数据的模块

## python语音播报

### 安装

```python
pip  install pyttsx3
```

### 导入模块

```python
"""
使用：pyttsx3
"""
import pytt、sx3
weather_info = get_weather(city)  # weather_info来获取抓取到的天气文字
weather = pyttsx3.init()  # 初始化说话的对象
weather.say(weather_info)  # 设置说话内容
weather.runAndWait()  # 开始执行说话的操作
```

## pywifi模块

### 安装

```python
pip install pywifi
```

## logging模块

自带模块

### 简单使用

```python
	 
	"""
	logging配置
	"""
	
	import os
	import logging.config
	
	# 定义三种日志输出格式 开始
	
	standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
	                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
	
	simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
	
	id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
	
	# 定义日志输出格式 结束
	
	logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
	
	logfile_name = 'all2.log'  # log文件名
	
	# 如果不存在定义的日志目录就创建一个
	if not os.path.isdir(logfile_dir):
	    os.mkdir(logfile_dir)
	
	# log文件的全路径
	logfile_path = os.path.join(logfile_dir, logfile_name)
	
	# log配置字典
	"""
	logging配置
	"""
	
	import os
	
	# 1、定义三种日志输出格式，日志中可能用到的格式化串如下
	# %(name)s Logger的名字
	# %(levelno)s 数字形式的日志级别
	# %(levelname)s 文本形式的日志级别
	# %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
	# %(filename)s 调用日志输出函数的模块的文件名
	# %(module)s 调用日志输出函数的模块名
	# %(funcName)s 调用日志输出函数的函数名
	# %(lineno)d 调用日志输出函数的语句所在的代码行
	# %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
	# %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
	# %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
	# %(thread)d 线程ID。可能没有
	# %(threadName)s 线程名。可能没有
	# %(process)d 进程ID。可能没有
	# %(message)s用户输出的消息
	
	# 2、强调：其中的%(name)s为getlogger时指定的名字
	standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
	                  '[%(levelname)s][%(message)s]'
	
	simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
	
	test_format = '%(asctime)s] %(message)s'
	
	# 3、日志配置字典
	LOGGING_DIC = {
	    'version': 1,
	    'disable_existing_loggers': False,
	    'formatters': {
	        'standard': {
	            'format': standard_format
	        },
	        'simple': {
	            'format': simple_format
	        },
	        'test': {
	            'format': test_format
	        },
	    },
	    'filters': {},
	    'handlers': {
	        #打印到终端的日志
	        'console': {
	            'level': 'DEBUG',
	            'class': 'logging.StreamHandler',  # 打印到屏幕
	            'formatter': 'simple'
	        },
	        #打印到文件的日志,收集info及以上的日志
	        'default': {
	            'level': 'DEBUG',
	            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
	            'formatter': 'standard',
	            # 可以定制日志文件路径
	            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
	            # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
	            'filename': 'a1.log',  # 日志文件
	            'maxBytes': 1024*1024*5,  # 日志大小 5M
	            'backupCount': 5,
	            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
	        },
	        'other': {
	            'level': 'DEBUG',
	            'class': 'logging.FileHandler',  # 保存到文件
	            'formatter': 'test',
	            'filename': 'a2.log',
	            'encoding': 'utf-8',
	        },
	    },
	    'loggers': {
	        #logging.getLogger(__name__)拿到的logger配置
	        '': {
	            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
	            'level': 'DEBUG', # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
	            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
	        },
	        '专门的采集': {
	            'handlers': ['other',],
	            'level': 'DEBUG',
	            'propagate': False,
	        },
	    },
	}
	
	def load_my_logging_cfg():
	    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
	    logger = logging.getLogger(__name__)  # 生成一个log实例
	    logger.info('It works!')  # 记录该文件的运行状态
	
	if __name__ == '__main__':
	    load_my_logging_cfg()

```

## 自动化案例—工作模式

### 安装

```python
pip install pyautogui
```

### 自动 防故障功能

```python
pyautogui.FAILSAFE =False 
默认这项功能为True, 这项功能意味着：当鼠标的指针在屏幕的最坐上方，程序会报错；目的是为了防止程序无法停止；
```

### 停顿功能

```python
pyautogui.PAUSE = 1  
意味着所有pyautogui的指令都要暂停一秒；其他指令不会停顿；这样做，可以防止键盘鼠标操作太快；
```

### 鼠标操作函数

操作鼠标点击的函数。

| 函数                                | 简单说明                                       |
| ----------------------------------- | ---------------------------------------------- |
| move(x,y)、  moveTo(x,y)            | 移动鼠标，前者移动相对位置，后者移动到指定位置 |
| click(x,y)、doubleClick、rightClick | 单击/双击/右击，无参版本在当前位置点击鼠标     |
| drag(x,y)、dragTo(x,y)              | 拖动鼠标                                       |
| mouseDown、mouseUp                  | 按下按键，松开按键                             |
| scroll                              | 向下滚动鼠标滚轮的函数                         |

### 键盘操作函数

操作键盘按键的函数。

| 函数                  | 简介               |
| --------------------- | ------------------ |
| press(‘left’,press=3) |                    |
| hotkey(‘ctrl’,‘s’)    | 按下Ctrl+S组合键   |
| keyDown、keyUp        | 按下和松开键盘按键 |

### 提示框函数

PyAutoGUI可以显示提示框，这时候程序会暂停运行，直到用户点击提示框。

| 函数                                           | 简介               |
| ---------------------------------------------- | ------------------ |
| alert(text=’’,title=’’,button=[‘OK’,‘Cancle’]) | 显示警告对话框     |
| confirm()                                      | 显示确认对话框     |
| prompt()                                       | 显示提示对话框     |
| password()                                     | 显示密码输入对话框 |

### 屏幕截图和定位函数

截取屏幕的函数，也可以从屏幕中寻找匹配的图片，并返回其坐标。你可以事先保存一些按钮的截图，然后通过这种方式定位按钮的位置，然后点击。

| 函数                    | 简介                                           |
| ----------------------- | ---------------------------------------------- |
| screenshot(‘image.png’) | 保存截图并返回截图，无参版本直接返回截图不保存 |
| center(‘image.png’)     | 从屏幕上寻找图片位置，返回框位置               |
| locateOnScreen(‘img’)   | 从屏幕寻找图片位置，直接返回坐标               |
