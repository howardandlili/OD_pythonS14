#!/user/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Howie'
import time
time_format = '%Y-%m-%d %x'
time_current = time.strftime(time_format)
print(time_current,type(time_current))