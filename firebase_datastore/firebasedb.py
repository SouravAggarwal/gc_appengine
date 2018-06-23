
import pyrebase


config = {
    "apiKey": "AIzaSyDNfd01cbAeUabo21bCo4MJPiWbqSkaxTo",
    "authDomain": "firstdemo-207206.firebaseapp.com",
    "databaseURL": "https://firstdemo-207206.firebaseio.com",
    "projectId": "firstdemo-207206",
    "storageBucket": "firstdemo-207206.appspot.com",
    "messagingSenderId": "384333440646"

}


# https://github.com/thisbejim/Pyrebase/blob/master/README.md
firebase = pyrebase.initialize_app(config)

db = firebase.database()
db = db.child("books")


def getdata():
    return db.get().val()
