#!/usr/bin/env python3
"""
This script provides statistics about the logs stored in the MongoDB collection
'nginx'
in the 'logs' database, including the count of logs, methods, status checks,
and top 10
most present IPs.
"""

import pymongo


def log_stats(mongo_collection):
    """
    Prints statistics about the logs in the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB
        collection to query.
    """
    print(f"{mongo_collection.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = mongo_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    # Access the database and collection
    db = client['logs']
    nginx_collection = db['nginx']

    # Print log stats
    log_stats(nginx_collection)
