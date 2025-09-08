#!/usr/bin/env python3
""" string_utils.py is a sample Python module that exposes string utility functions """

import math

def halve_string(input_string):
    middle = math.ceil(len(input_string) / 2)
    return (input_string[:middle], input_string[middle:])