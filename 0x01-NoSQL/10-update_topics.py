#!/usr/bin/env python3
"""
10-update.py.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on name.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}},
                                 True)
