<template>
  <div>
  <div class="profile-card">
    <div class="profile-greet">
    <p>Hello <br>
    {{ profile.username }}!
    </p>
    </div>
    <div class="profile-pic">
    <!-- <img src="@/assets/emotion/mood (1).png" alt=""> -->
    <img src="@/assets/profile/OBJECTS_03.png" alt="">
    </div>
  <div v-if="!isCurrentUser">
    <button @click="follow" :class="{ following_status : isfollowed}">follow</button>
  </div>
  </div>
  <div class="name-tag"><span>{{profile.favorite_genre[0]?.name}} 장르 애호가 </span></div>


  <div>이번달은 {{ profile.goal_of_month}}개의 영화를 볼거야!</div>
  <div v-if="isCurrentUser">
    <div>나는 {{ profile.favorite_genre[0]?.name }}같은 장르들을 좋아해!</div> 
    <div>특히 {{ profile.save_movies[0]?.title }}가 보고 싶더라.</div>
    <div>관심가는 feelmers는 <span v-for="feelmer in profile.followings" :key="feelmer.id"> {{ feelmer.username }},</span>야.</div>
  </div>
  <span>내가 쓴 feelog는 : </span>
    <router-link
      v-for="feelog in feelogs"
      :key="feelog.id"
      :to="'/feelog-detail/' + feelog.id"
    >{{ feelog.title }}</router-link>

  </div>
</template>

<script>


export default {
  name : 'AccountView',
  components : {

  },
  data(){
    return{
      isfollowed: false
    }
  },
  created(){
    const nickname = this.$route.params.nickname
    this.$store.dispatch("fetchProfile", nickname)
  },
  mounted(){
  
  },
  methods:{
    follow() {
          // follow 메서드 구현 (버튼을 클릭했을 때 호출될 동작)
          this.isfollowed = !this.isfollowed
          const nickname = this.$route.params.nickname 
          this.$store.dispatch("follow", nickname)
          // 새로고침
          this.$router.go()
        }
  },
  computed: {
    profile(){
      return this.$store.state.profile
    },
    feelogs() {
      // const nickname = this.$route.params.nickname
      // return this.$store.state.feelogs.filter(feelog => feelog.username == nickname)
      const nickname = this.$route.params.nickname
      return this.$store.getters.getUserFeelogsByName(nickname)
    },
    isCurrentUser(){
      const currentUsername = this.$store.state.nickname;
      return this.$route.params.nickname === currentUsername;
    }
  },

}
</script>

<style scoped>

.following_status{
  background-color: blue;
  color: beige;
}
.container{
  position: relative;
  top:200px;
}
.profile-card{
  display: flex;
  justify-content: space-between;
}
.profile-greet {
  color: #3B322C;
  font-size: 4em;
  font-weight: 700;
}
.name-tag{
  font-size : 1.5em;
  font-weight: 200;
  color : #627278;
}

</style>

