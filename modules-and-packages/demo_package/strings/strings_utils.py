#!/usr/bin/env python3
""" strings_utils.py is a sample Python module that exposes string list utility functions """

from strings.string_utils import halve_string

def halve_strings(string_list):
    halved_string_list = []
    
    for string in string_list:
        halved_string_list.append(halve_string(string))
    
    return halved_string_list