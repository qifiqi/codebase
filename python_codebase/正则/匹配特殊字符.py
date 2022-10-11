# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2022/7/3021:32
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : 匹配特殊字符.py
__author__ = 'Small Fu'
def character_handling(character: str) -> str:
    """
    处理特殊字符
    @param character: str
    @return: str
    """
    com = re.compile('[^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a]')
    return com.sub('', character)
