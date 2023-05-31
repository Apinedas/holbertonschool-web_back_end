#!/usr/bin/env python3
"""Auth class for basic authentication"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Auth class for basic authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth"""
        if path and path[-1] != "/":
            path += "/"
        if path is None or excluded_paths is None or len(excluded_paths) == 0 \
           or path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """Auth header"""
        if not request or "Authorization" not in request.headers.keys():
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """Get current user"""
        return None
