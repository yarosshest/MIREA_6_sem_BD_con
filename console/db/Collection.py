from pymongo import collection

from db import db


class Collection:
    name: str
    coll: collection

    def __init__(self, nameCollection: str):
        collist = db.list_collection_names()
        self.name = nameCollection
        if "customers" in collist:
            print(f"The collection {nameCollection} exists.")
        else:
            print(f"The collection {nameCollection} created.")
        self.coll = db["nameCollection"]

    def insert(self, data: dict | list[dict]):
        if type(data) is dict:
            self.coll.insert_one(data)
        else:
            self.coll.insert_many(data)


