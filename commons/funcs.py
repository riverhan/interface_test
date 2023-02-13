# -*- coding:utf-8 -*-
"""
# @File: funcs.py
# @Time : 2023/2/7 20:53
# @Author : Riveryoyo
# @Desc: 
"""
import base64
import hashlib
import urllib.parse
import time

import rsa

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

    return int(time.time())


# def last_id():
#     # 不自增，只会结果
#     id_file = YamlUtils('./yaml_files/id.yaml')
#     return id_file["id"]


def md5(content):
    # 1. 原文转为字节
    content = str(content).encode("utf-8")

    # 2. 进行md5计算
    result = hashlib.md5(content).hexdigest()

    return result


def base64_encode(content):
    # 1. 原文转为二进制
    content = str(content).encode("utf-8")

    # 2. base64编码(二进制)
    encode_value = base64.b64encode(content)

    # 3.转成字符串
    encode_str = encode_value.decode("utf-8")

    return encode_str


def base64_decode(content):
    # 1. 原文转为二进制
    content = str(content).encode("utf-8")

    # 2. base64解密(二进制)
    decode_value = base64.b64decode(content)

    # 3.转成字符串
    encode_str = decode_value.decode("utf-8")

    return encode_str


def rsa_encode(content):
    # 1. 原文转为二进制
    content = str(content).encode("utf-8")

    with open('./data/public.pem') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())  # 公钥

    # 2.得到加密结果
    ras_value = rsa.encrypt(content, pubkey)  # 加密得到二进制数据

    # 加密结果是对二进制进行某种数学计算得到，可能不时候转为字符串

    # 3.转成base64字符串
    # 3.1 base64编码(二进制)
    base64_value = base64.b64encode(ras_value)

    # 3.2 转成字符串
    encode_str = base64_value.decode("utf-8")

    return encode_str


def rsa_decode(content):
    # # 1. 原文转为二进制

    base64_value = base64.b64decode(content)

    # 2. 加密二进制
    with open('./data/private.pem') as f:
        priv_key = rsa.PrivateKey.load_pkcs1(f.read().encode())  # 私钥

    rsa_value = rsa.decrypt(base64_value, priv_key)

    # 3. 转成字符串
    decode_str = rsa_value.decode("utf-8")

    return decode_str


def beifan_len(content):
    """得到数据长度"""

    return len(content)
