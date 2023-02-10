# -*- coding:utf-8 -*-
"""
# @File: main
# @Time : 2023/2/7 16:32
# @Author : Riveryoyo
"""
import os
from pathlib import Path

import pytest
from commons.cases import TestApi

if __name__ == '__main__':
    case_path = Path('yaml_files/encrypt')
    TestApi.find_yaml_case(case_path)
    pytest.main(["-vs", __file__])
    os.system("allure generate temp -o allure_report --clean")
