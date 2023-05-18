<template>
<div>
App.vue 입니다.
<nav>
  <router-link :to="{ name : 'SignupView'}">회원가입</router-link>
  <router-link :to="{ name : 'HomeView' }">Home</router-link>
  <router-link :to="{ name : 'LoginView' }">로그인</router-link>
  <router-link :to="{ name : 'MovieListView' }">전체</router-link>
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

  },
};
</script>

<style>

</style>