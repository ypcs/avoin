# -*- coding: utf-8 -*-

from pymongo import MongoClient

class Database(object):
    def __init__(self, database, **kwargs):
        self._client = MongoClient()
        self._database = self._client[database]
        self._kwargs = kwargs

    def collection(self, name):
        return self._database[name]

def main():
    db = Database('test')
    restaurants = db.collection('restaurants')
    print restaurants.find_one()
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
