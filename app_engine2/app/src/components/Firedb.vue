<template>
<div>
  <h2> Add new Books</h2>

  <form id="form" v-on:submit.prevent="addBook">
    <div>
      <label for="bookTitle"> Title: </label>
      <input type='text' id="bookTitle" v-model="newBook.title">
    </div>
    <div>
      <label for="bookAuthor"> Author: </label>
      <input type='text' id="bookAuthor" v-model="newBook.author">
    </div>
    <div>
      <label for="bookUrl"> Url: </label>
      <input type='text' id="bookUrl" v-model="newBook.url">
    </div>
    <input type='submit' value="Add Book">

  </form>

  <tbody>
    <tr>
      <td>
        <h3> ==>   Firebase DB </h3>
        <h3>  &nbsp;&nbsp;&nbsp;Title &nbsp;  Author &nbsp; Url </h3>

      </td>
    </tr>

    <tr v-for="book in books" v-bind:key="book">
      <td>
        <!-- <a v-bind:href="book.url">  </a>-->
        {{book.title}}
      </td>
      <td>
        {{book.author}}
      </td>
      <td>
        {{book.url}}
      </td>
    </tr>
  </tbody>
 <!--button v-on:click="updateDatastore">Update Datastore</button-->
</div>


</template>

<script>
import firedbconfig from '../firedbconfig.js'

var booksRef = firedbconfig.ref;
export default {
  name: 'Firedb',

  firebase:{
      books: booksRef
    },

    data() {
      return {
        newBook: {
          title: "",
          author: "",
          url: "http://",
        }
      }
    },
    methods: {
      addBook() {
        //books.push("heel");
        booksRef.push(this.newBook);
        this.newBook.title="",
        this.newBook.author="",
        this.newBook.url="";

        //console.log("new book added");
      },
    

    }
  }
  </script>


<style>
</style>
