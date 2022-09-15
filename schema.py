"""
Functions for dealing with schemas
"""
import csv

def load_schema(name):
    schema_list = __import__("schema_list")
    schema = getattr(schema_list, name, None)

    return schema

def get_schema_from_file(location, delimiter = ","):
    header = None

    with open(location, encoding = "utf-8") as file:
        handler = csv.reader(file, delimiter = delimiter)
        header = next(handler)

    return header
