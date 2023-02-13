"""
@Time: 20:48
@FileName: read_ini.py
@Author: Riveryoyo
"""


def read_ini():
    """
    用于将config.ini配置内容写入commons/settings中
    """
    with open(r'config/config.ini') as f:
        info = f.read()
    with open(r'commons/setting.py', mode='w') as f:
        f.write(info)
