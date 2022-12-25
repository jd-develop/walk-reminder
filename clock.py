#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import notifier

while True:
    time.sleep(5 * 60)
    notifier.notify()
    time.sleep(5 * 60)
    notifier.notify("walk")
