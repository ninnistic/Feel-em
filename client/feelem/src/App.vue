<template>
<div>
App.vue 입니다.

<nav>
  <router-link to="/signup">회원가입</router-link> |
  <router-link to="/home">Home</router-link> |
  <router-link to="/login">로그인</router-link> |
  <router-link to="/movielist">전체</router-link> |
  <router-link to="/movie-detail/:id">영화상세</router-link> |
  <router-link to="/feelog-detail }">리뷰상세</router-link> |
  <router-link to="/mypage">마이페이지</router-link>
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