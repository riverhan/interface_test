# -*- coding:utf-8 -*-
"""
# @File: cases
# @Time : 2023/2/6 20:26
# @Author : Riveryoyo
"""
from pathlib import Path

from commons.models import CaseInfo
from commons.yamlutils import YamlUtils
from commons.session import Session

_case_path = Path('../yaml_files')


class TestApi:
    @classmethod
    def find_yaml_case(cls, case_path: Path = _case_path):
        yaml_path_list = case_path.glob("**/test_*.yaml")
        for yaml_path in sorted(yaml_path_list):
            yaml_data = YamlUtils(yaml_path)
            case_info = CaseInfo(**yaml_data)
            case_func = cls.new_case(case_info)
            print(case_info)
            print(yaml_path.name)
            setattr(cls, f"{yaml_path.name}", case_func)

    @classmethod
    def new_case(cls, case_info):
        def test_func(self):
            Session().request(**case_info.request)

        return test_func


# if __name__ == '__main__':
#     TestApi().find_yaml_case()
TestApi().find_yaml_case()
