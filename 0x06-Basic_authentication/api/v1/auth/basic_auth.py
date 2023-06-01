#!/usr/bin/env python3
"""Basic auth module"""

from .auth import Auth
import base64
from typing import TypeVar
from ..views.users import User


class BasicAuth(Auth):
    """Class Basic Auth"""
    def extract_base64_authorization_header(self, authorization_header: str):
        '''Extracts base 64 from auth_header'''
        if authorization_header is None\
                or type(authorization_header) is not str\
                or not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header):
        '''Decodes base64'''
        if not base64_authorization_header\
                or type(base64_authorization_header) is not str:
            return None
        to_decode = base64_authorization_header.encode('utf-8')
        try:
            return base64.b64decode(to_decode).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header):
        '''Extracts user credentials from string'''
        if not decoded_base64_authorization_header or \
                type(decoded_base64_authorization_header) is not str or\
                ":" not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":"))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) ->\
            TypeVar('User'):
        '''Get user object from credentials'''
        list_user_from_db = User.search({'email': user_email})
        if type(user_email) is not str or type(user_pwd) is not str or\
                len(list_user_from_db) == 0 or not\
                list_user_from_db[0].is_valid_password(user_pwd):
            return None
        return list_user_from_db[0]
