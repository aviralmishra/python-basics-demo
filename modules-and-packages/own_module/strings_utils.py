#!/usr/bin/env python3
""" strings_utils.py is a sample Python module that exposes string list utility functions """

import string_utils

def halve_strings(string_list):
    halved_string_list = []
    
    for string in string_list:
        halved_string_list.append(string_utils.halve_string(string))
    
    return halved_string_list