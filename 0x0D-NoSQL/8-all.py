#!/usr/bin/env python3
"""Pymongo lists all document"""


def list_all(mongo_collection):
    """Inserts kwargs into collection"""
    return mongo_collection.find()
