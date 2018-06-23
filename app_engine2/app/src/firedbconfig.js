
import Firebase from 'firebase'

var config = {
  apiKey: "AIzaSyDNfd01cbAeUabo21bCo4MJPiWbqSkaxTo",
     authDomain: "firstdemo-207206.firebaseapp.com",
     databaseURL: "https://firstdemo-207206.firebaseio.com",
     projectId: "firstdemo-207206",
     storageBucket: "firstdemo-207206.appspot.com",
     messagingSenderId: "384333440646"
};

const app = Firebase.initializeApp(config);
const db = app.database();
const booksRef = db.ref('books');

//booksRef.push("hi");

export default {ref:booksRef };
