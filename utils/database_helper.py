from datetime import datetime

import pymongo
from pymongo.errors import PyMongoError
import os
import dotenv
from pymongo.server_api import ServerApi

class DatabaseIO:
    def __init__(self, db_name=None, collection_name=None):
        dotenv.load_dotenv()

        mongo_username = os.environ['MONGO_USERNAME']
        mongo_password = os.environ['MONGO_PASSWORD']
        client_url = os.environ['MONGO_CLIENT_URL_DEV']
        uri  = f"mongodb+srv://{mongo_username}:{mongo_password}@{client_url}/?retryWrites=true&w=majority"

        if not db_name:
            db_name = os.environ['MONGO_DATABASE_NAME']
        if not collection_name:
            collection_name = os.environ['MONGO_COLLECTION']

        self.client = pymongo.MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_document(self, article, collection=None, unique_on='_id', upsert=False):

        if not collection:
            collection = self.collection

        article['date_modified'] = datetime.now().utcnow()
        existing_document = collection.find_one({unique_on: article[unique_on]})
        if existing_document:
            # there is something like with the reddit id already

            if upsert:
                collection.update_one({unique_on: article[unique_on]}, {"$set": article})
        else:
            article['date_created'] = datetime.now().utcnow()
            collection.insert_one(article)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            self.client.close()
        except PyMongoError as e:
            print(f"An error occurred while closing the database connection: {e}")
            raise

    def __del__(self):
        try:
            self.client.close()
        except Exception as e:
            print(e)

    def read_documents(self, query=None, sort_by=None, sort_order=None):
        if query is None:
            query = {}
        try:
            if sort_by:
                if not sort_order or sort_order not in [1, -1]:
                    sort_order= 1
                for article in self.collection.find(query).sort(sort_by, sort_order):
                    yield article
            else:
                for article in self.collection.find(query):
                    yield article
        except Exception as e:
            print(e)

    def count_documents(self, query=None):
        if query is None:
            query = {}
        try:
            return self.collection.count_documents(query)
        except Exception as e:
            print(e)

    def update_documents(self, query, update, upsert=True):
        try:
            self.collection.update_one(query, update, upsert=upsert)
        except Exception as e:
            print(e)

    def delete_document(self, query):
        try:
            self.collection.delete_one(query)
        except Exception as e:
            print(e)
