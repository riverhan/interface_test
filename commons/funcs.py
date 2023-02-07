# -*- coding:utf-8 -*-
"""
# @File: funcs.py
# @Time : 2023/2/7 20:53
# @Author : Riveryoyo
# @Desc: 
"""
import urllib


def url_unquote(s: str) -> str:
    return urllib.parse.unquote(s)
