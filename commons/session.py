# -*- coding:utf-8 -*-
"""
# @File: session
# @Time : 2023/2/6 19:22
# @Author : Riveryoyo
"""
from urllib.parse import urljoin
import logging

import allure
import requests
from requests import Response, PreparedRequest
from commons import setting

logger = logging.getLogger(__name__)


class Session(requests.Session):
    def __init__(self):
        super().__init__()
        self.base_url = setting.base_url

    @allure.step('发送请求')
    def request(self, method, url, *args, **kwargs):
        if not url.startswith("http"):  # 如果url不是以HTTP开头
            # 就自动添加baseurl
            url = self.base_url+url

        return super().request(method, url, *args, **kwargs)

    def send(self, request: PreparedRequest, *args, **kwargs) -> Response:
        logger.info(f"___发送请求>>>>>> 接口地址 = {request.method} {request.url}")
        logger.debug(f"___发送请求>>>>>> 请求头 = {request.headers}")
        logger.info(f"___发送请求>>>>>> 请求正文 = {request.body}")
        response = super().send(request, **kwargs)  # 按原有的方式发送请求
        logger.info(f"___接收响应      <<<<<< 状态码 = {response.status_code}")
        logger.debug(f"___接收响应      <<<<<< 响应头 = {response.headers}")
        logger.info(f"___接收响应      <<<<<< 响应正文 = {response.content}")
        return response


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    session = Session("https://baidu.com")

    resp = session.get("/123", data={"a": 1})

    print(resp.url)
