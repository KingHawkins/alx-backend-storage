#!/usr/bin/env python3
"""
8-all
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    """
    if list(mongo_collection.find()) == 0:
        return []
    return list(mongo_collection.find())
