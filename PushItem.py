#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@ Author: HeliantHuS
@ Codes are far away from bugs with the animal protecting
@ Time:  2022-01-16
@ FileName: PushItem.py
"""
import uuid

import config


class PushItem():
    def __init__(self):
        self.server = config.init()

    def process(self):
        while True:
            self.server.sadd(config.PROCESS_NAME, f"test{uuid.uuid4()}")


if __name__ == '__main__':
    push = PushItem()
    push.process()
