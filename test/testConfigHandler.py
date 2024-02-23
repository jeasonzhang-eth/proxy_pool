# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     testGetConfig
   Description :   testGetConfig
   Author :        J_hao
   date：          2017/7/31
-------------------------------------------------
   Change Activity:
                   2017/7/31:
-------------------------------------------------
"""
__author__ = 'J_hao'

from handler.configHandler import ConfigHandler
from time import sleep


def testConfig():
    """
    :return:
    """
    conf = ConfigHandler()
    print(conf.db_conn)
    print(conf.server_port)
    print(conf.server_host)
    print(conf.table_name)
    assert isinstance(conf.fetchers, list)
    print(conf.fetchers)

    for _ in range(2):
        print(conf.fetchers)
        sleep(5)


if __name__ == '__main__':
    testConfig()

