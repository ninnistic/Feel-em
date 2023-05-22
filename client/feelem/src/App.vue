<template>
<div class="main">
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
<router-view @Login="isLogin=true" class="main-view"/>      
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
/* http://meyerweb.com/eric/tools/css/reset/ 
   v2.0 | 20110126
   License: none (public domain)
*/

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
@import url("https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.6/dist/web/static/pretendard.css");
* {
  font-family: 'Pretendard'
  background-color: #f4f3ee;
}
.main{
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.main-view{
  align-self: center;
}


</style>