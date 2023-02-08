# -*- coding:utf-8 -*-
"""
# @File: databases.py
# @Time : 2023/2/8 14:07
# @Author : Riveryoyo
# @Desc: 
"""
import pymysql as MySQLdb
from commons.yamlutils import YamlUtils
import logging


logger = logging.getLogger(__name__)
config_info = YamlUtils('./yaml_files/mysql_info.yaml')


class DBServer(object):
    def __init__(self):
        self.db = MySQLdb.connect(**config_info)
        self.conn = self.db.cursor()

    def execute_sql(self, sql):
        logging.info(f"{sql=}")
        self.conn.execute(sql)
        return self.conn.fetchone()


if __name__ == '__main__':
    res = DBServer().execute_sql("select count(1) from report where author='beifan_88'")
    print(res)
