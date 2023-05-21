<template>
  <div>
  
   <span>내 이름은 {{ profile.data.username }}!</span><br>
   <span>이번달은 {{ profile.data.goal_of_month }}만큼의 영화를 볼거야!</span><br>
   <span>나는 {{ profile.data.favorite_genre }}같은 장르들을 좋아해!</span><br>
   <span>특히 {{ profile.data.save_movies }}가 보고 싶더라.</span><br>
   <span>관심가는 feelmers는 
   <span v-for="(feelmer,index) in profile.data.followings" :key="index">{{ feelmer }},</span>야.</span><br>

   <span>내가 쓴 feelog</span>
   <span>{{ feelogs }}</span>

  </div>
</template>

<script>


export default {
  name : 'MyPageView',
  components : {

  },
  created(){
    const nickname = this.$route.params.nickname
    this.$store.dispatch("fetchProfile",nickname)
  },
  computed: {
    profile(){
      return this.$store.state.profile
    },
    feelogs() {
      const nickname = this.$route.params.nickname
      const res = this.$store.state.feelogs.filter(feelog => feelog.username == nickname)
      const result = res.filter(res => {
        const create = new Date(res.created_at)
        return create.getMonth()===4
        // 0:12 범위로 날짜를 리턴함. 해당 숫자를 움직여서 월 별 필로그 보여주기.
      })
      return result
    }
  
  },

}
</script>

<style>

</style>