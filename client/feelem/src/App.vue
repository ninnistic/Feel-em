<template>
  <div class="main">
    <nav class="navbar" style="background-color: transparent; width: 100%;" id="myNav">
      <ul>
        <li>
          <router-link to="/movielist">Movies</router-link> 
        </li>
        <li>
          <router-link to="/home"><img src="@/assets/logo-black.png" alt="" style="width:150px;"></router-link>
        </li>
        
        <!-- <li>
          <router-link to="/movie-detail/:id">영화상세</router-link>
        </li> -->
        <li v-if="isLoggedIn" class="nav-login">
          <span>
            <a @click="logout" style="color:black;">Logout</a>
          </span>
          <span>
            <router-link :to="'/account/' + nickname">{{ nickname }}</router-link>
          </span>
        </li>

        <li v-else class="nav-login">
          
        <span>
          <router-link to="/login">Login</router-link>
        </span>
        <span>
          <router-link to="/signup">Sign Up</router-link>
        </span>
        
      </li>
        
      </ul>
    </nav>
    <router-view class="main-view" />
    <FooterCard />
  </div>
</template>

<script>
import FooterCard from "@/components/FooterCard";
export default {
  name: 'App',
  components:{
    FooterCard,
  },
  methods : {
    logout: function() {
      this.$store.dispatch("signOut")
      this.$router.push(`login`) 
    }
  },
  
  created() {
    this.$store.actions.checkForLogin();
  },
  computed:{
    isLoggedIn() {
      return this.$store.getters.isSignedIn;
    },
    nickname(){
      return this.$store.state.nickname;
    }
  },
}

</script>

<style scoped>
* {
  font-family: 'Pretendard';
  text-decoration: none;
  
}
.main{
  display: flex;
  justify-content: center;
  flex-direction: column;
  background-color: #f4f3ee;
}
/* 
.main-view{
  align-self: center;
  background-color: #f4f3ee;
} */

nav{
  background-color: transparent;
	vertical-align: baseline;
  /* background-color: #f4f3ee; */
}
.navbar {
  /* background-color: #f4f3ee; */
  padding: 10px;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
  display: flex;
  justify-content: space-between;
  background-color: transparent;

}

body.fixed-nav .navbar {
  position: fixed;
  top: 0;
  opacity: 1;
  backdrop-filter: blur(10px);
  mask: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 1) 45%,
    rgba(0, 0, 0, 0) 100%
  );
} 

.nav-login{
  display: flex;
  flex-direction: row;
  justify-content:space-evenly;
}
.navbar ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  /* background-color: #f4f3ee; */
  width:100%;
  justify-content: space-around;
  align-items: start;
  
}

.navbar li {
  font-size: large;
  text-align: center;
  padding: 10px;
  margin:10px;
  font-weight: 500;
  width:200px;
}

a{
  text-decoration: none;
} 
.navbar a {
  text-decoration: none;
  padding: 5px;
  border-radius: 5px;
  /* background-color: #f4f3ee; */
  color:black;
}

.navbar a:hover {
  background-color: #8DDCA4;
  color:black;
}


/* 
.nav-colored { background-color:#000; }
.nav-transparent { background-color:transparent;} */

</style>