<template>
<div>
App.vue 입니다.
<div v-if="isLogin">
<span>안녕하세요, {{ getNickname }}님!</span>
<button @click="logout">로그아웃</button>
</div>


<nav>
  <router-link to="/signup">회원가입</router-link> |
  <router-link to="/home">Home</router-link> |
  <router-link to="/login">로그인</router-link> |
  <router-link to="/movielist">전체</router-link> |
  <!-- <router-link to="/movie-detail/:id">영화상세</router-link> | -->
  <router-link to="/feelog-detail }">리뷰상세</router-link> |
  <router-link :to="`/mypage/`+getNickname">마이페이지</router-link>
</nav>
<router-view @Login="isLogin=true"/>      
</div>
</template>

<script>
export default {
  name: 'App',
  methods : {
    logout: function() {
      this.$store.dispatch("signOut");
      this.$router.push(`login`) 
    }
  },
  mounted() {
   const token = localStorage.getItem('jwt')
    if(token) {
      this.isLogin = true
    }
    this.getNickname
  },
  
  computed:{
    isLogin() {
      console.log( this.$store.getters.isSignedIn);
      console.log("computed:isLogin", this.$store.getters.isSignedIn);
     return this.$store.getters.isSignedIn;
    },
   getNickname(){
    return this.$store.state.nickname;
   }
  },
}
</script>

<style>
@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.6/dist/web/static/pretendard.css");
* {
font-family: 'Pretendard'

}
</style>