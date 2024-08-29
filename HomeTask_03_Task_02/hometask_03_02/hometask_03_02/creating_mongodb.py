from pymongo import MongoClient
from pymongo.server_api import ServerApi
from context_manager import file_manager
import json
import os

client = MongoClient('mongodb+srv://akovalenko881:dUeIEVRaoSupgCTT@cluster0.c0ovf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&appName=Cluster0', server_api = ServerApi('1'))

db = client.my_hometask

# Construct the path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

authors_file_path = os.path.join(parent_dir, 'authors.json')
quotes_file_path = os.path.join(parent_dir, 'quotes.json')

#getting the context from the json file, loading it to the context variable and inserting the data into data base.
with file_manager(authors_file_path, 'r') as f:
    if f:
        print(f"Processing {authors_file_path}")
        context = json.load(f)
        result_1 = db.authors.insert_many(context)
        print(result_1.inserted_ids)

with file_manager(quotes_file_path, 'r') as f:
    if f:
        print(f"Processing {quotes_file_path}")
        context = json.load(f)
        result_2 = db.qoutes.insert_many(context)
        print(result_2.inserted_ids)