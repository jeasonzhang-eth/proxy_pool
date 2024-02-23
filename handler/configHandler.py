# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     configHandler
   Description :
   Author :        JHao
   date：          2020/6/22
-------------------------------------------------
   Change Activity:
                   2020/6/22:
-------------------------------------------------
"""
__author__ = 'JHao'

import os
import setting
from util.singleton import Singleton
from util.lazyProperty import LazyProperty
from util.six import reload_six, withMetaclass


class ConfigHandler(withMetaclass(Singleton)):

    def __init__(self):
        pass

    @LazyProperty
    def server_host(self):
        return os.environ.get("HOST", setting.HOST)

    @LazyProperty
    def server_port(self):
        return os.environ.get("PORT", setting.PORT)

    @LazyProperty
    def db_conn(self):
        return os.getenv("DB_CONN", setting.DB_CONN)

    @LazyProperty
    def table_name(self):
        return os.getenv("TABLE_NAME", setting.TABLE_NAME)

    @property
    def fetchers(self):
        reload_six(setting)
        return setting.PROXY_FETCHER

    @LazyProperty
    def http_url(self):
        return os.getenv("HTTP_URL", setting.HTTP_URL)

    @LazyProperty
    def https_url(self):
        return os.getenv("HTTPS_URL", setting.HTTPS_URL)

    @LazyProperty
    def verify_timeout(self):
        return int(os.getenv("VERIFY_TIMEOUT", setting.VERIFY_TIMEOUT))

    # @LazyProperty
    # def proxyCheckCount(self):
    #     return int(os.getenv("PROXY_CHECK_COUNT", setting.PROXY_CHECK_COUNT))

    @LazyProperty
    def max_fail_count(self):
        return int(os.getenv("MAX_FAIL_COUNT", setting.MAX_FAIL_COUNT))

    # @LazyProperty
    # def maxFailRate(self):
    #     return int(os.getenv("MAX_FAIL_RATE", setting.MAX_FAIL_RATE))

    @LazyProperty
    def pool_size_min(self):
        return int(os.getenv("POOL_SIZE_MIN", setting.POOL_SIZE_MIN))

    @LazyProperty
    def proxy_region(self):
        return bool(os.getenv("PROXY_REGION", setting.PROXY_REGION))

    @LazyProperty
    def timezone(self):
        return os.getenv("TIMEZONE", setting.TIMEZONE)

