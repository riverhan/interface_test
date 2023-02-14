# -*- coding:utf-8 -*-
"""
# @File: models
# @Time : 2023/2/6 19:18
# @Author : Riveryoyo
"""
from dataclasses import dataclass, asdict
from commons import setting
import allure
import yaml
from commons.templates import Template
import logging

logger = logging.getLogger(__name__)


@dataclass
class CaseInfo:
    """
    yaml文件或是用例文件中应该包括的字段
    """
    title: str
    request: dict
    extract: dict
    validate: dict
    parametrize: list = ''
    epic: str = setting.allure_epic
    feature: str = setting.allure_feature
    story: str = setting.allure_story

    def to_yaml(self):
        yaml_str = yaml.dump(asdict(self), allow_unicode=True)
        return yaml_str

    @classmethod
    def from_yaml(cls, yaml_str):
        return cls(**yaml.safe_load(yaml_str))

    @allure.step('断言')
    def assert_all(self):
        if not self.validate:
            return
        for assert_type, assert_value in self.validate.items():
            for msg, data in assert_value.items():
                expected_value, actual_value = data[0], data[1]
                try:
                    match assert_type:
                        case 'equals':
                            logger.info(f"___assert:{msg},{expected_value} == {actual_value}")
                            assert expected_value == actual_value, msg
                        case "not_equals":
                            logger.info(f"___assert:{msg},{expected_value} != {actual_value}")
                            assert expected_value != actual_value, msg
                        case "contains":
                            logger.info(f"___assert:{msg},{expected_value} in {actual_value}")
                            assert expected_value in actual_value, msg
                        case "not_contains":
                            logger.info(f"___assert:{msg},{expected_value} not in {actual_value}")
                            assert expected_value not in actual_value, msg
                except AssertionError:
                    logger.error(f"___assert fail {expected_value=}，{actual_value=}")

    def ddt(self) -> list:  # 返回一个列表，列表中应该包含N个 注入了变量的 CaseInfo

        case_list = []

        if not self.parametrize:  # 没有使用数据驱动测试
            case_list.append(self)
        else:  # 使用了数据驱动测试
            args_name = self.parametrize[0]
            args_value_list = self.parametrize[1:]
            self.parametrize = []
            for args_value in args_value_list:
                d = dict(zip(args_name, args_value))
                case_info_str = self.to_yaml()  # 转字符串
                case_info_str = Template(case_info_str).render(d)  # 输入变量
                case_info = self.from_yaml(case_info_str)  # 转成类

                case_list.append(case_info)  # 加入到返回值

        return case_list


if __name__ == '__main__':
    with open(r'E:\PycharmProjects\interface_test\yaml_files\bbs\test_2_login.yaml', encoding="utf-8") as f:
        data = yaml.safe_load(f)
    # print(data)
    case_info = CaseInfo(**data)

    # s = case_info.to_yaml()  # 字符串
    #     # print(s)
    #     # new_case = case_info.from_yaml(s)
    #     # print(new_case)
    case_info.ddt()
