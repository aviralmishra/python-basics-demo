#!/usr/bin/env python3
""" string_utils.py is a sample Python module that exposes string utility functions """

import math

def halve_string(input_string):
    length = len(input_string)
    
    if(length % 2 == 0):
        return (
            input_string[0:length // 2],
            input_string[length // 2:length]
        )
    else:
        return (
            input_string[0:math.ceil(length / 2)],
            input_string[math.ceil(length / 2):length]
        )