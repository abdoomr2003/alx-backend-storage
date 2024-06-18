#!/usr/bin/env python3
"""
Script to provide statistics about
Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    stats = nginx_collection.count_documents({})
    print(f"{stats} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        countMethods = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {countMethods}")
    statusCount = nginx_collection.count_documents({'path': '/status'})
    print(f"{statusCount} status check")
