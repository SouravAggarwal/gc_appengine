import time
import json
from firebasedb import getdata
from gcdatastore import add_data,get_completedata

def migrate_data():
    '''
    It fetched data from firebase and update the same on datasote
    '''
    id = str(int(time.time()))
    data = (json.dumps(getdata()))
    add_data(id, data)


def show_firebase_data():
    '''It return the firebase snapshot'''
    return getdata()

def show_datastore_data():
    '''Return complete data from datastor'''
    return get_completedata()


if __name__ =="__main__":
    #print(show_firebase_data())
    print(show_datastore_data())
    #print(migrate_data())
