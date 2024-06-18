#!/usr/bin/env python3
"""
This script contains a function to update the 'topics' field of documents in a
MongoDB collection based on the 'name' field.
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of the document(s) in the specified MongoDB
    collection where the 'name' field matches the provided name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection where the document(s) will be updated.
        name (str): The value of the 'name' field to match the document(s)
        to be updated.
        topics (list): The list of topics to set in the 'topics' field of the
        matched document(s).

    Returns:
        pymongo.collection.Collection: The MongoDB collection after the
        update operation.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return mongo_collection
