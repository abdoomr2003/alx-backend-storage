#!/usr/bin/env python3
"""
This script contains a function to insert a document into a MongoDB collection
using pymongo.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document into the specified MongoDB collection with the provided
    keyword arguments.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection where the document will be inserted.
        **kwargs: Arbitrary keyword arguments representing the fields and
        values of the document to be inserted.

    Returns:
        bson.objectid.ObjectId: The unique identifier (_id) of the inserted
        document.
    """
    insert_one = mongo_collection.insert_one(kwargs)
    return insert_one.inserted_id
