# -*- coding:utf-8 -*-
"""
# @File: cases
# @Time : 2023/2/6 20:26
# @Author : Riveryoyo
"""
from pathlib import Path

from commons.models import CaseInfo
from commons.yamlutils import YamlUtils


class TestApi:
    @classmethod
    def find_yaml_case(cls, path):
        _case_path = Path(path)
        yaml_path_list = _case_path.glob("**/test_*.yaml")
        for yaml_path in sorted(yaml_path_list):
            yaml_data = YamlUtils(yaml_path)
            case_info = CaseInfo(**yaml_data)
            print(case_info)


if __name__ == '__main__':
    TestApi().find_yaml_case('../yaml_files')
