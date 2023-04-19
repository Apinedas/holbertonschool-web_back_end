#!/usr/bin/env python3
'''First filter data task'''
import logging, re, os, mysql.connector
from typing import List


PII_FIELDS = ('name', 'phone', 'ssn', 'password', 'email')

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
        for _ in self.fields:
            newRecord = filter_datum(self.fields, self.REDACTION, newRecord,
                                     self.SEPARATOR)
        log_record = logging.LogRecord("my_logger", logging.INFO, None, None,
                                       newRecord, None, None)
        return super(RedactingFormatter, self).format(log_record)


def get_logger() -> logging.Logger:
    '''Returns the user_data logger object'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    logger.setFormatter(RedactingFormatter(PII_FIELDS))

    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    username = os.getenv('PERSONAL_DATA_DB_USERNAME') or 'root'
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ''
    host = os.getenv('PERSONAL_DATA_DB_HOST') or 'localhost'
    db = os.getenv('PERSONAL_DATA_DB_NAME')

    conection = mysql.connector.connection.MySQLConnection(user=username, password=password,
                                                           host=host, database=db)
    
    return conection
