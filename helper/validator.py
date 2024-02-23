# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     _validators
   Description :   定义proxy验证方法
   Author :        JHao
   date：          2021/5/25
-------------------------------------------------
   Change Activity:
                   2023/03/10: 支持带用户认证的代理格式 username:password@ip:port
-------------------------------------------------
"""
__author__ = 'JHao'

import re
from requests import head
from util.six import withMetaclass
from util.singleton import Singleton
from handler.configHandler import ConfigHandler

conf = ConfigHandler()

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
          'Accept': '*/*',
          'Connection': 'keep-alive',
          'Accept-Language': 'zh-CN,zh;q=0.8'}

IP_REGEX = re.compile(r"(.*:.*@)?\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}")


class ProxyValidator(withMetaclass(Singleton)):
    pre_validator = []
    http_validator = []
    https_validator = []

    @classmethod
    def add_pre_validator(cls, func):
        cls.pre_validator.append(func)
        return func

    @classmethod
    def add_http_validator(cls, func):
        cls.http_validator.append(func)
        return func

    @classmethod
    def add_https_validator(cls, func):
        cls.https_validator.append(func)
        return func


@ProxyValidator.add_pre_validator
def format_validator(proxy):
    """检查代理格式"""
    return True if IP_REGEX.fullmatch(proxy) else False


# @ProxyValidator.add_http_validator
# def http_timeout_validator(proxy):
#     """ http检测超时 """
#
#     proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy)}
#
#     try:
#         r = head(conf.http_url, headers=HEADER, proxies=proxies, timeout=conf.verify_timeout)
#         return True if r.status_code == 200 else False
#     except Exception as e:
#         return False


# @ProxyValidator.add_https_validator
# def https_timeout_validator(proxy):
#     """https检测超时"""
#
#     proxies = {"http": "http://{proxy}".format(proxy=proxy), "https": "https://{proxy}".format(proxy=proxy)}
#     try:
#         r = head(conf.https_url, headers=HEADER, proxies=proxies, timeout=conf.verify_timeout, verify=False)
#         return True if r.status_code == 200 else False
#     except Exception as e:
#         return False


@ProxyValidator.add_http_validator
def custom_validator_example(proxy):
    """自定义validator函数，校验代理是否可用, 返回True/False"""
    return True
