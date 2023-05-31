#!/usr/bin/env python3
"""Basic auth module"""

from .auth import Auth


class BasicAuth(Auth):
    """Class Basic Auth"""
    def extract_base64_authorization_header(self, authorization_header: str):
        '''Extracts base 64 from auth_header'''
        if authorization_header is None\
           or type(authorization_header) is not str\
           or not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
