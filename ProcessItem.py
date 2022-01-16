#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@ Author: HeliantHuS
@ Codes are far away from bugs with the animal protecting
@ Time:  2022-01-16
@ FileName: ProcessItem.py
"""
import threading
import time

import config


class ProcessItem(threading.Thread):
    def __init__(self):
        super().__init__()
        self.server = config.init()

    def run(self) -> None:
        while True:
            item = self.server.spop(config.PROCESS_NAME)
            if item is not None:
                self.myProcess(item)
                time.sleep(0.2)
            else:
                time.sleep(3)

    def myProcess(self, item):
        print(item)


if __name__ == '__main__':
    for i in range(10):
        myItem = ProcessItem()
        myItem.start()
