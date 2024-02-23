# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     testRedisClient
   Description :
   Author :        JHao
   date：          2020/6/23
-------------------------------------------------
   Change Activity:
                   2020/6/23:
-------------------------------------------------
"""
__author__ = 'JHao'


def testRedisClient():
    from db.dbClient import DbClient
    from helper.proxy import Proxy

    uri = "redis://:pwd@127.0.0.1:6379"
    db = DbClient(uri)
    db.change_table("use_proxy")
    proxy = Proxy.create_from_json('{"proxy": "118.190.79.36:8090", "https": false, "fail_count": 0, "region": "", "anonymous": "", "source": "freeProxy14", "check_count": 4, "last_status": true, "last_time": "2021-05-26 10:58:04"}')

    print("put: ", db.put(proxy))

    print("get: ", db.get(https=None))

    print("exists: ", db.exists("27.38.96.101:9797"))

    print("exists: ", db.exists("27.38.96.101:8888"))

    print("pop: ", db.pop(https=None))

    print("getAll: ", db.get_all(https=None))

    print("getCount", db.get_count())


if __name__ == '__main__':
    testRedisClient()
