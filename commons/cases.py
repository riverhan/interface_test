# -*- coding:utf-8 -*-
"""
# @File: cases
# @Time : 2023/2/6 20:26
# @Author : Riveryoyo
"""
from pathlib import Path


from commons.exchange import Exchange
from commons.models import CaseInfo
from commons.yamlutils import YamlUtils
from commons.session import Session

_case_path = Path(r'E:\PycharmProjects\interface_test\yaml_files\weixin')
exchange = Exchange(r'E:\PycharmProjects\interface_test\extract.yaml')


class TestApi:
    @classmethod
    def find_yaml_case(cls):
        yaml_path_list = _case_path.glob("**/test_*.yaml")
        for yaml_path in sorted(yaml_path_list):
            yaml_data = YamlUtils(yaml_path)
            case_info = CaseInfo(**yaml_data)
            case_func = cls.new_case(case_info)
            setattr(cls, f"{yaml_path.name.split('.')[0]}", case_func)

    @classmethod
    def new_case(cls, case_info):
        def test_func(self):
            new_case_info = exchange.replace(case_info)
            result = Session().request(**new_case_info.request)
            print(type(result))
            if new_case_info.extract is not None:
                for key_val, value in new_case_info.extract.items():
                    exchange.extract(result, key_val, *value)

        return test_func


# if __name__ == '__main__':
#     pytest.main(['-vs'])
TestApi().find_yaml_case()
