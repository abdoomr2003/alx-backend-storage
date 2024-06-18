#!/usr/bin/env python3
"""
This script contains a function to find documents in a MongoDB collection
that contain a specific topic in the 'topics' field.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Finds all documents in the specified MongoDB collection that contain the
    given topic in the 'topics' field.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection to search.
        topic (str): The topic to search for in the 'topics' field.

    Returns:
        pymongo.cursor.Cursor: A cursor to the documents that match the query.
    """
    return mongo_collection.find({"topics": topic})
