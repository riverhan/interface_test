# -*- coding:utf-8 -*-
"""
# @File: cases
# @Time : 2023/2/6 20:26
# @Author : Riveryoyo
"""
from pathlib import Path

import pytest

from commons.exchange import Exchange
from commons.models import CaseInfo
from commons.yamlutils import YamlUtils
from commons.session import Session
import logging


logger = logging.getLogger(__name__)
_case_path = Path('./yaml_files/ddt')
exchange = Exchange('extract.yaml')
session = Session()


class TestApi:
    @classmethod
    def find_yaml_case(cls):
        yaml_path_list = _case_path.glob("**/test_*.yaml")
        for yaml_path in sorted(yaml_path_list):
            logger.info(f"load file: {yaml_path=}")
            yaml_data = YamlUtils(yaml_path)
            case_info = CaseInfo(**yaml_data)
            case_func = cls.new_case(case_info)
            setattr(cls, f"{yaml_path.name.split('.')[0]}", case_func)

    @classmethod
    def new_case(cls, case_data):
        ddt_data = case_data.ddt()
        ddt_title = [data.title for data in ddt_data]

        @pytest.mark.parametrize("case_info", ddt_data, ids=ddt_title)
        def test_func(self, case_info):
            logger.info(f"用例开始执行：{case_info.title}".center(80, "="))
            new_case_info = exchange.replace(case_info)
            result = session.request(**new_case_info.request)
            for key_val, value in new_case_info.extract.items():
                exchange.extract(result, key_val, *value)
            # 断言判断
            assert_case_info = exchange.replace(case_info)
            assert_case_info.assert_all()
            logger.info(f"用例执行结束：{case_info.title}".center(80, "="))
        return test_func


# if __name__ == '__main__':
#     pytest.main(['-vs'])
TestApi().find_yaml_case()
