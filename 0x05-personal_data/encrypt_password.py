#!/usr/bin/env python3
'''Module to hash a password and store it on the DB'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Function to hash a password'''
    password = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    return (hashed_password)


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Function to check a password'''
    return (bcrypt.checkpw(password.encode('utf-8'), hashed_password))
