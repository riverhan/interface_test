# -*- coding:utf-8 -*-
"""
# @File: models
# @Time : 2023/2/6 19:18
# @Author : Riveryoyo
"""
from dataclasses import dataclass


@dataclass
class CaseInfo:
    """
    yaml文件或是用例文件中应该包括的字段
    """
    title: str
    request: dict
    extract: dict
    validate: dict
