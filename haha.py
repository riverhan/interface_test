# -*- coding:utf-8 -*-
"""
# @File: haha.py
# @Time : 2023/2/7 19:15
# @Author : Riveryoyo
# @Desc: 
"""
import base64
import hashlib
from base64 import b64encode, b64decode

import rsa


def md5(content):
    content = str(content).encode('utf-8')
    result = hashlib.md5(content).hexdigest()
    return result


def base64_encode(content):
    content = str(content).encode('utf-8')
    result_64_encode = b64encode(content)
    return result_64_encode.decode('utf-8')


def base64_decode(content):
    # content = str(content).encode('utf-8')
    result_64_decode = b64decode(content)
    return result_64_decode.decode('utf-8')


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
    with open(
            r"D:\PycharmProjects\TestClass\api_framework\data\private.pem") as f:
        priv_key = rsa.PrivateKey.load_pkcs1(f.read().encode())  # 私钥

    rsa_value = rsa.decrypt(base64_value, priv_key)

    # 3. 转成字符串
    decode_str = rsa_value.decode("utf-8")

    return decode_str


if __name__ == '__main__':
    s = 'beifan'
    print(md5(s))
    print(base64_encode(s))
    print(base64_decode(base64_encode(s)))
    print(rsa_encode(s))
