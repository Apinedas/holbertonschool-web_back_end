#!/usr/bin/env python3
'''First filter data task'''
import logging
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''Filter datum with regex'''
    for obf in fields:
        message = re.sub("(?<={:s}=)(.*?)(?={:s})".format(obf, separator),
                         redaction, message)

    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Format logging method'''
        newRecord = record.getMessage()
        for obf in self.fields:
            newRecord = filter_datum(self.fields, self.REDACTION, newRecord,
                                     self.SEPARATOR)
        log_record = logging.LogRecord("my_logger", logging.INFO, None, None,
                                       newRecord, None, None)
        return super(RedactingFormatter, self).format(log_record)

def get_logger() -> logging.Logger:
    '''Returns the user_data logger object'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logger.INFO)
    logger.StreamHandler(formatter=RedactingFormatter)
    
    return logger

PII_FIELDS = ('name', 'phone', 'ssn', 'password', 'email')
