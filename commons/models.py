# -*- coding:utf-8 -*-
"""
# @File: models
# @Time : 2023/2/6 19:18
# @Author : Riveryoyo
"""
from dataclasses import dataclass, asdict

import yaml


@dataclass
class CaseInfo:
    """
    yaml文件或是用例文件中应该包括的字段
    """
    title: str
    request: dict
    extract: dict
    validate: dict

    def to_yaml(self):
        yaml_str = yaml.dump(asdict(self), allow_unicode=True)
        return yaml_str

    @classmethod
    def from_yaml(cls, yaml_str):
        return cls(**yaml.safe_load(yaml_str))


if __name__ == '__main__':
    with open(r'E:\PycharmProjects\interface_test\yaml_files\weixin\test_1_get_token.yaml', encoding="utf-8") as f:
        data = yaml.safe_load(f)
    print(data)
    case_info = CaseInfo(**data)

    s = case_info.to_yaml()  # 字符串
    print(s)
    new_case = case_info.from_yaml(s)
    print(new_case)
