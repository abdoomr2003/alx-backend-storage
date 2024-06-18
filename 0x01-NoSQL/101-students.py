
#!/usr/bin/env python3
"""
Module to provide the top students sorted by average score.
"""


def top_students(mongo_collection):
    """ Returns all students sorted by average score.

    Args:
        mongo_collection (pymongo.collection.Collection):
        The MongoDB collection to query.

    Returns:
        list: A list of dictionaries representing the students,
        sorted by average score.

    """
    pipeline = [
        {
            '$project': {
                'name': 1,
                'topics': 1,
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
