#!/usr/bin/env python3
"""
11-main.py.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    """
    return list(mongo_collection.find({"topics": topic}))
