## 介绍一下

### 安装

```python
pip  install pyttsx3
```



### 导入模块

```python
"""
使用：pyttsx3
"""
import pyttsx3
```



```python
weather_info = get_weather(city)  # weather_info来获取抓取到的天气文字
weather = pyttsx3.init()  # 初始化说话的对象
weather.say(weather_info)  # 设置说话内容
weather.runAndWait()  # 开始执行说话的操作
```