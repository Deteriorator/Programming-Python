#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    adder3.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.13   9:38
-------------------------------------------------------------------------------
   @Change:   2020.05.13
-------------------------------------------------------------------------------
"""

import sys

sum = 0
for line in sys.stdin:
    sum += int(line)
print(sum)

