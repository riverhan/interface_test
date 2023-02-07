# -*- coding:utf-8 -*-
"""
# @File: session
# @Time : 2023/2/6 19:22
# @Author : Riveryoyo
"""
from urllib.parse import urljoin
import logging
import requests
from requests import Response, PreparedRequest

logger = logging.getLogger('session')


class Session(requests.Session):
    def __init__(self, base_url=None):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        if not url.startswith("http"):  # 如果url不是以HTTP开头
            # 就自动添加baseurl
            url = urljoin(self.base_url, url)

        return super().request(method, url, *args, **kwargs)

    def send(self, request: PreparedRequest, *args, **kwargs) -> Response:
        logger.info(f"发送请求>>>>>> 接口地址 = {request.method} {request.url}")
        logger.debug(f"发送请求>>>>>> 请求头 = {request.headers}")
        logger.info(f"发送请求>>>>>> 请求正文 = {request.body}")
        response = super().send(request, **kwargs)  # 按原有的方式发送请求
        logger.info(f"接收响应      <<<<<< 状态码 = {response.status_code}")
        logger.debug(f"接收响应      <<<<<< 响应头 = {response.headers}")
        logger.info(f"接收响应      <<<<<< 响应正文 = {response.content.decode('utf-8')}")
        return response


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    session = Session("https://baidu.com")

    resp = session.get("/123", data={"a": 1})

    print(resp.url)
