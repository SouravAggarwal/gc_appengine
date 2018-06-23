import os
import time
import json
from google.cloud import datastore


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./firstdemo-a214cb88e8b0.json"


dbclient = datastore.Client(project='firstdemo-207206')
kind = "Books"

def get_data(id):
    '''Get data by Id'''
    key = dbclient.key(kind, str(id))
    return (dbclient.get(key))

def get_completedata():
    query = dbclient.query(kind=kind)
    results = list(query.fetch())
    return results

def add_data(id, data):
    key=dbclient.key(kind, id)
    entity = datastore.Entity(key=key,)


    entity["book_name"] = data
    dbclient.put(entity)


if __name__ == "__main__":
    print( get_completedata() )
