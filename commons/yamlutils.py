# -*- coding:utf-8 -*-
"""
# @File: yamlutils
# @Time : 2023/2/6 19:02
# @Author : Riveryoyo
"""
import yaml
import logging
from commons.models import CaseInfo
logger = logging.getLogger(__name__)


class YamlUtils(dict):
    def __init__(self, path):
        super().__init__()
        self._path = path
        self.load()

    def load(self):
        with open(self._path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if data:
            self.update(data)

    def save(self):
        with open(self._path, 'w', encoding='utf-8') as f:
            yaml.dump(dict(self), f)


if __name__ == '__main__':
    files = YamlUtils('../yaml_files/bbs/test_1_home.yaml')
    print(files)
    case_info = CaseInfo(**files)
    print(case_info)

