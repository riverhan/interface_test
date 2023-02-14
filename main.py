# -*- coding:utf-8 -*-
"""
# @File: main
# @Time : 2023/2/7 16:32
# @Author : Riveryoyo
"""
import datetime
import os
import shutil
import pytest
from commons.cases import TestApi

if __name__ == '__main__':
    # 初始化测试类
    TestApi.find_yaml_case()
    pytest.main([__file__])
    shutil.move("logs/pytest.log", f"logs/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    os.system("allure generate temp -o allure_report --clean")
