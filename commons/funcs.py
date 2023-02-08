# -*- coding:utf-8 -*-
"""
# @File: funcs.py
# @Time : 2023/2/7 20:53
# @Author : Riveryoyo
# @Desc: 
"""
import urllib.parse
import time
from commons.databases import DBServer
from commons.yamlutils import YamlUtils
import logging

logger = logging.getLogger(__name__)
db = DBServer()


def url_unquote(s: str) -> str:
    return urllib.parse.unquote(s)


def time_str():
    return str(time.time())


def sql(s: str) -> str:
    return db.execute_sql(s)[0]


def new_id():
    # 自增，用不重复
    id_file = YamlUtils("id.yaml")
    id_file["id"] += 110
    id_file.save()
    return id_file["id"]


def last_id():
    # 不自增，只会结果
    id_file = YamlUtils("id.yaml")
    return id_file["id"]
