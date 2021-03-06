from pymongo import MongoClient

""" Data Access Layer

    self.db_conn            => client.api
    self.db_conn.users      => users collection
    self.db_conn.admin      => admin collection
    self.db_conn.categories => categories collection

    self.db_conn.products   => products collection
"""

client = MongoClient('mongodb:27017')
db_conn = client.api