"""
Main conversor file
"""
import json
import csv
from schema import load_schema

INPUT_FILE = "input/crawler-v10.csv"
OUTPUT_FILE = "output/crawler-json-20220912.json"
OUTPUT_SCHEMA = "output/crawler-json-schema-20220912.json"
SCHEMA_NAME = "crawler_schema"

schema = load_schema(SCHEMA_NAME)
output_header = []

def columns_to_split(schema):
    columns = []

    for column in schema:
        if "mode" in column and column["mode"] == "REPEATED":
            columns.append(column["name"])

    return columns

for row in schema:
    output_header.append(row["name"])

with open(OUTPUT_SCHEMA, "w", encoding = "utf-8") as json_file:
    json_file.write(json.dumps(schema))

with open(INPUT_FILE, encoding = "utf-8") as csv_file:
    csv_handler = csv.DictReader(csv_file, fieldnames = output_header)

    next(csv_handler)

    with open(OUTPUT_FILE, "w", encoding = "utf-8") as json_file:
        columns = columns_to_split(schema)
        print(columns)
        for csv_line in csv_handler:
            row = {}
            headers = csv_line.keys()

            for header in headers:
                if header in columns:
                    row[header] = csv_line[header].split(";")
                else:
                    row[header] = csv_line[header]

            json_file.write(json.dumps(row) + "\n")
