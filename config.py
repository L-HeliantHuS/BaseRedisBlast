#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@ Author: HeliantHuS
@ Codes are far away from bugs with the animal protecting
@ Time:  2022-01-16
@ FileName: config.py
"""

import logging

# redis 实例
import redis

REDIS: redis.Redis = None

# hostname. is required
REDIS_HOST = ""

# port. default:6379
REDIS_PORT = 6379

# password
REDIS_PASSWORD = ""

# list name
PROCESS_NAME = "test"


def init():
    try:
        redis_server = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, socket_timeout=2)
        if redis_server.ping() == True:
            return redis_server
    except:
        logging.error("redis connect error!")
        exit()
