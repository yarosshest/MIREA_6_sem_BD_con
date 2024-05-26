import re

from prettytable import PrettyTable
from pymongo import collection
import abc
from console.db.db import db


def parse_conditions(filter_string: str):
    or_conditions = filter_string.split('or')
    all_conditions = []
    for or_condition in or_conditions:
        and_conditions = or_condition.split('and')
        and_conditions = [cond.strip() for cond in and_conditions]
        parsed_conditions = []
        for condition in and_conditions:
            if '>=' in condition:
                key, value = condition.split('>=')
                parsed_conditions.append((key.strip(), '>=', value.strip()))
            elif '<=' in condition:
                key, value = condition.split('<=')
                parsed_conditions.append((key.strip(), '<=', value.strip()))
            elif '!=' in condition:
                key, value = condition.split('!=')
                parsed_conditions.append((key.strip(), '!=', value.strip().strip('"').strip("'")))
            elif '=' in condition:
                key, value = condition.split('=')
                parsed_conditions.append((key.strip(), '=', value.strip().strip('"').strip("'")))
            elif '>' in condition:
                key, value = condition.split('>')
                parsed_conditions.append((key.strip(), '>', value.strip()))
            elif '<' in condition:
                key, value = condition.split('<')
                parsed_conditions.append((key.strip(), '<', value.strip()))
            elif 'like' in condition:
                key, value = condition.split('like')
                parsed_conditions.append((key.strip(), 'like', value.strip().strip('"').strip("'")))
        all_conditions.append(parsed_conditions)
    return all_conditions


def match_condition(item, key, op, value):
    if key not in item:
        return False
    if op == '=':
        return str(item[key]) == value
    elif op == '!=':
        return str(item[key]) != value
    elif op == '>':
        return item[key] > int(value)
    elif op == '<':
        return item[key] < int(value)
    elif op == '>=':
        return item[key] >= int(value)
    elif op == '<=':
        return item[key] <= int(value)
    elif op == 'like':
        return value in item[key]
    else:
        raise ValueError(f"Unsupported operator: {op}")


def filter_data(data, conditions) -> list[dict]:
    filtered_data = []
    for item in data:
        for and_conditions in conditions:
            if all(match_condition(item, key, op, value) for key, op, value in and_conditions):
                filtered_data.append(item)
                break
    return filtered_data


class Collection:
    name: str
    coll: collection

    def __init__(self, nameCollection: str):
        collist = db.list_collection_names()
        self.name = nameCollection
        if nameCollection in collist:
            print(f"The collection {nameCollection} exists.")
        else:
            print(f"The collection {nameCollection} created.")
        self.coll = db[nameCollection]

    def insert(self, data: dict | list[dict]):
        if type(data) is dict:
            self.coll.insert_one(data)
        else:
            self.coll.insert_many(data)

    def show(self):
        dct = self.coll.find()
        table = PrettyTable()
        try:
            if dct:
                headers = dct[0].keys()
                table.field_names = headers
                for row in dct:
                    table.add_row(row.values())
            print(table)
        except IndexError:
            print("Table is empty")

    def showWith(self, filter_string: str):
        data = self.coll.find()
        conditions = parse_conditions(filter_string)
        filtered_data = filter_data(data, conditions)

        # Create PrettyTable
        table = PrettyTable()
        if filtered_data:
            headers = filtered_data[0].keys()
            table.field_names = headers
            for row in filtered_data:
                table.add_row(row.values())
        print(table)

    def delByData(self, data: dict | list[dict]):
        if type(data) is dict:
            self.coll.delete_one(data)
        else:
            for i in data:
                self.coll.delete_one(i)

    def dell(self, filter_string: str):
        data = self.coll.find()
        conditions = parse_conditions(filter_string)
        filtered_data = filter_data(data, conditions)

        self.delByData(filtered_data)
        print(f"Delited {len(filtered_data)}")

    @abc.abstractmethod
    def insertTestData(self):
        pass
