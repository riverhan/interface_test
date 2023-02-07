# -*- coding:utf-8 -*-
"""
# @File: exchange.py
# @Time : 2023/2/7 18:54
# @Author : Riveryoyo
# @Desc: 
"""
import copy
import json
import re

import jsonpath
from commons.yamlutils import YamlUtils
from commons.models import CaseInfo
from commons.templates import Template


class Exchange(object):
    def __init__(self, path):
        self.files = YamlUtils(path)
        self.resp = None

    def extract(self, resp, key_value, attr, expr: str, index=0):
        self.resp = copy.deepcopy(resp)
        try:
            self.resp.json = resp.json()
        except json.JSONDecodeError:
            self.resp.json = {"msg": "is not json data"}

        data = getattr(self.resp, attr)
        print(self.resp.cookies)
        match expr[0]:
            case '/':
                res = None
            case '$':
                data = dict(data)
                res = jsonpath.jsonpath(data, expr)
            case _:
                res = re.findall(expr, data)
        print(f"{res=}")
        if res:
            value = res[index]
        else:
            value = 'not data'
        self.files[key_value] = value
        self.files.save()

    def replace(self, case_info: CaseInfo):
        # 1. 将case_info 转成字符串
        case_info_str = case_info.to_yaml()
        # 2. 替换字符串
        case_info_str = Template(case_info_str).render(self.files)
        # 3. 将字符串 转成case_info
        new_case_info = case_info.from_yaml(case_info_str)
        return new_case_info


if __name__ == '__main__':
    class MockResponse:
        text = '{"name": "beifan", "age": "18", "data": [3,66,99], "aaa": null}'

        def json(self):
            return json.loads(self.text)


    mock_resp = MockResponse()

    print(type(mock_resp.text))
    print(type(mock_resp.json()))
    exchange = Exchange('../yaml_files/test_1_home.yaml')