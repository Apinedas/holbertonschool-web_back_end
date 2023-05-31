#!/usr/bin/env python3
"""Basic auth module"""

from .auth import Auth
import base64


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
