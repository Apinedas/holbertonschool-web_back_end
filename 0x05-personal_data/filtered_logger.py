#!/usr/bin/env python3
'''First filter data task'''
import logging
from typing import List
import re


def filter_datum(field: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''Filter datum with regex'''
    for obf in field:
        message = re.sub("(?<={:s}=)(.*?)(?={:s})".format(obf, separator),
                         redaction, message)

    return message
