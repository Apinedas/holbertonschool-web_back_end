#!/usr/bin/env python3
"""Auth class for basic authentication"""

from flask import request
from typing import List, TypeVar


class Auth():
    """Auth class for basic authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Auth header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get current user"""
        return None
