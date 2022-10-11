# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/1716:06
# @Author  : 小符玩代码
# @Email   : 2737454073@qq.com
# @File    : python日志.py
# @Software: PyCharm

import logging, os

# 单个日志配置
"""
	可在logging.basicConfig()函数中通过具体参数来更改logging模块默认行为，可用参数有
	filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
	filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
	format：指定handler使用的日志显示格式。 
	    	%(name)s：Logger的名字，并非用户名，详细查看	
            %(levelno)s：数字形式的日志级别            
            %(levelname)s：文本形式的日志级别            
            %(pathname)s：调用日志输出函数的模块的完整路径名，可能没有           
            %(filename)s：调用日志输出函数的模块的文件名            
            %(module)s：调用日志输出函数的模块名            
            %(funcName)s：调用日志输出函数的函数名            
            %(lineno)d：调用日志输出函数的语句所在的代码行            
            %(created)f：当前时间，用UNIX标准的表示时间的浮 点数表示            
            %(relativeCreated)d：输出日志信息时的，自Logger创建以 来的毫秒数            
            %(asctime)s：字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒 
            %(message)s：用户输出的消息
	datefmt：指定日期时间格式。 如：'%Y-%m-%d %H:%M:%S %p',
	level：设置rootlogger（后边会讲解具体概念）的日志级别 
    stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
"""
# logging.basicConfig(
#     filename='./aa.log',
#     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     level=10,
#     encoding='utf-8'
# )
# logging.debug('调试debug')
# logging.info('消息info')
# logging.warning('警告warn')
# logging.error('错误error')
# logging.critical('严重critical')


# 多个日志配置
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
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志，分区
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件,日志轮转
            'formatter': 'standard',
            # 可以定制日志文件路径
            # BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
            # LOG_PATH = os.path.join(BASE_DIR,'a1.log')
            'filename': 'a1.log',  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 保存到文件
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'test',
            'filename': 'a2.log',
            'encoding': 'utf-8',
        },
    },
    # 获取这个里面的，在日志传入的时候会开启通道传入到指定的handlers中
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '专门的采集': {
            'handlers': ['other', ],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# 初始化日志
import logging.config
# 识别字典
logging.config.dictConfig(LOGGING_DIC)

# 获得loggers，看具体作用具体添加
log_aa = logging.getLogger('aa')
log_aa.debug('调试debug')
log_aa.info('消息info')
log_aa.warning('警告warn')
log_aa.error('错误error')
log_aa.critical('严重critical')
