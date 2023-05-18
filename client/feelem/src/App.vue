<template>
<div>
App.vue 입니다.
<nav>
  <router-link :to="{ name : 'AboutView'}">AboutView</router-link>
</nav>
<router-view />      
</div>
</template>

<script>
export default {
  name: 'App',

  data() {
    return {
  
    }
  },
  methods : {

  }
};
</script>

<style>

</style>