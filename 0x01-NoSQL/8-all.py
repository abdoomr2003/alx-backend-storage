#!/usr/bin/env python3
"""
Module: 8-all

Provides a function to retrieve all documents from a MongoDB collection.

Functions:
    list_all(mongo_collection):
        Retrieves all documents from the specified MongoDB collection.

"""


def list_all(mongo_collection):
    """
    Retrieves all documents from the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): A MongoDB collection
        object.

    Returns:
        pymongo.cursor.Cursor: A cursor iterating over the documents found.

    Raises:
        TypeError: If mongo_collection is not an instance of pymongo.collection
    .Collection.

    Example:
        Assuming `client` is a MongoClient instance and `my_db` is the database
        >>> collection = my_db.some_collection
        >>> documents = list_all(collection)
        >>> for document in documents:
        >>>     print(document)

    """
    school = mongo_collection.find()
    return school
