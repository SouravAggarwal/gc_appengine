<template>
  <div id="app">
    <img src="./assets/logo.png">
    <Firedb/>
    <!--router-view/-->
  </div>
</template>

<script>
import Firedb from './components/Firedb'
export default {
  name: 'App',
  components:{
    Firedb,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
