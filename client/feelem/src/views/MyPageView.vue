<template>
  <div>
    <img src="@/assets/emotion/mood (1).png" alt="">
    <img src="@/assets/profile/OBJECTS_03.png" alt="">
  <div v-if="profile.username != login_user">
    <button @click="follow" :class="{ following_status : isfollowed}" >follow</button>
  </div>

  <span>내 이름은 {{ profile.username }}!</span><br>
  <span>이번달은 {{ profile.goal_of_month}}개의 영화를 볼거야!</span><br>
  <div v-if="profile.username == login_user">
    <span>나는 {{ profile.favorite_genre[0].name }}같은 장르들을 좋아해!</span><br> <!--숫자로 뜬다-->
    <span>특히 {{ profile.save_movies[0].title }}가 보고 싶더라.</span><br><!--movie가 pk로 뜬다.-->
    <span>관심가는 feelmers는 
    <span v-for="feelmer in profile.followings" :key="feelmer.id"> {{ feelmer.username }},</span>야.</span><br> <!--user.pk로 뜬다. -->
  </div>
  <span>내가 쓴 feelog</span>
  <span>{{ feelogs }}</span>

  </div>
</template>

<script>


export default {
  name : 'MyPageView',
  components : {

  },
  data(){
    return{
      isfollowed:false
    }
  },
  created(){
    const nickname = this.$route.params.nickname
    this.$store.dispatch("fetchProfile", nickname)
  },
  methods:{
    follow() {
          // follow 메서드 구현 (버튼을 클릭했을 때 호출될 동작)
          this.isfollowed = !this.isfollowed
          const nickname = this.$route.params.nickname 
          this.$store.dispatch("follow", nickname)
          this.$forceUpdate()
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
      
    login_user(){
      return localStorage.getItem("nickname")
    }
  
  },

}
</script>

<style>

.following_status{
  background-color: blue;
  color: beige;
}

</style>

