<template>
<div class="account-container mx-5 px-5">
  <div class="clipboard">
    <div class= "binder">
          <div class="profile-card mx-5">
          <img :src="profile_pics" alt="profile_imgs">
              <div>
                    <div class="username-tag">{{ profile.username }}
                      <b-button v-if="!isCurrentUser" @click="follow" variant="primary" size="sm" :class="{ following_status: isfollowed }">
                    {{ isfollowed ? "Unfollow" : "Follow" }}
                  </b-button>
                  <b-button v-else  variant="primary" size="sm" >
                    프로필 수정
                  </b-button>
                    </div>
                <div class="nickname-tag">
                <span>{{ profile.favorite_genre[0]?.name }} 장르 애호가 </span>
                </div>
                <div class="name-tag">
                Following <span> 50 </span> | Followers <span> 100 </span>
                </div>
              <!-- <span>
                월별 Feelog표 횟수: {{ profile.goal_of_month }}
              </span> -->
              <div class="progress my-2">
                <div class="progress-bar" role="progressbar" style="width: 100%; background-color:#8DDCA4;" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" >Feelog 1/1</div>
              </div>
              </div>
              <!-- <div v-for="(mood, index) in currentUserFeelogs" :key=mood.id>
                {{mood.id}}
                <p>index : {{index}}</p>
              </div> -->
            
          </div>
            <br>
    <div>

    <!-- <div>이번달은 {{ profile.goal_of_month }}개의 영화를 볼거야!</div> -->

        <div v-if="isCurrentUser">
              <div class="d-flex my-3" style="align-self: self-start;">
                <h1 class="fw-bold username" style="align-self: self-start;">{{ profile.username }}</h1>
                <h1 class="fw-bold">님의 선호 장르</h1>
              </div>
              
              <div class="genre_icon_container">
                  <div v-for="genres in profile.favorite_genre" :key="genres.id" class="genre_icon">
                    <span>{{genres.name}} </span>
                  </div>
              </div>
              <br>
              <br>
              <div class="d-flex my-3" style="align-self: self-start;">
                <h1 class="fw-bold username" style="align-self: self-start;">{{ profile.username }}</h1>
                <h1 class=" description">님이 찜한 영화 </h1>
              </div>
              <div class="genre_icon_container">
                  <div v-for="movies in profile.save_movies" :key="movies.id" class="movie_icon">
                    <span>{{movies.title}} </span>
                  </div>
              </div>
              <br>
              
              <!-- <div class="d-flex my-3" style="align-self: self-start;">
                  <h1 class="fw-bold username" style="align-self: self-start;">{{ profile.username }}</h1>
                  <h1 class="fw-bold">님이 찜한 영화</h1>

                </div> -->
        </div> <!--iscurrent-->
              <div class="d-flex my-3" style="align-self: self-start;">
                <h1 class="fw-bold username" style="align-self: self-start;">{{ profile.username }}</h1>
                <h1 class=" description">님의 Follow</h1>
              </div>

              <div class="genre_icon_container">
                <router-link v-for="otherfeelmer in profile.followings" :key="otherfeelmer.id" :to="'/account/' + otherfeelmer.username">
                  <div class="genre_icon">{{ otherfeelmer.username }}</div>
                </router-link>
              </div>
      




        </div>

    <!-- <router-link
      v-for="feelog in feelogs"
      :key="feelog.id"
      :to="'/feelog-detail/' + feelog.id"
      >{{ feelog.title }}</router-link
    > -->
      

  </div>
  <!-- <div class="feelog-container"> -->
      <div class="feelog-card m-5 p-5">
        <div style="border-radius: 10px; background-color: #F58080; color:white; text-align: center; height: 25px; width:150px;"><span class="m-2">월별 목표 달성!</span></div>
              <div class="d-flex my-3" style="align-self: self-start;">
                <h1 class="fw-bold username" style="align-self: self-start;">{{ profile.username }}</h1>
                <h1 class="fw-bold">님의 Feelog</h1>
              </div>
              <br>
              
                <router-link
                  v-for="feelog in feelogs"
                  :key="feelog.id"
                  :to="'/feelog-detail/' + feelog.id">
                  <FeelogCard
                    :feelog="feelog" 
                  class="feelog-container-account my-5" homeFeelog/>
                </router-link>
              </div>
      <!-- </div> -->
  </div>
</div> 
</template>

<script>
import FeelogCard from "@/components/FeelogCard";

export default {
  name: "AccountView",
  components: {
    FeelogCard,
  },
  data() {
    return {
      isfollowed: false,
      account:true,
    }
  },
  created() {
    const nickname = this.$route.params.nickname;
    this.$store.dispatch("fetchProfile", nickname);
    this.$store.dispatch("fetchFeelogsByName", nickname);
    
  },
  mounted() {},
  methods: {
    follow() {
      console.log(this.$store.state.profile)
      // follow 메서드 구현 (버튼을 클릭했을 때 호출될 동작)
      this.isfollowed = !this.isfollowed;
      const nickname = this.$route.params.nickname;
      this.$store.dispatch("follow", nickname);
      // // 새로고침
      // this.$router.go();
    },
  },
  computed: {
    profile() {
      return this.$store.state.profile
    },
    currentUserFeelogs(){
      return this.$store.state.currentUserFeelogs
    },
    profile_pics() {
      return this.profile.profile_pic.image
    },
    profile_genre() {
      return this.profile.favorite_genre.name
    },
    feelogs() {
      // const nickname = this.$route.params.nickname
      // return this.$store.state.feelogs.filter(feelog => feelog.username == nickname)
      const nickname = this.$route.params.nickname;
      return this.$store.getters.getUserFeelogsByName(nickname);
    },

    feelogcnt(){
      return length(this.feelog)
    },
    isCurrentUser() {
      const currentUsername = this.$store.state.nickname;
      return this.$route.params.nickname === currentUsername;
    },
  },
};
</script>

<style scoped>

.feelog-card{
  width:100%;
}
.genre_icon_container{
  display: flex;
}
.username{
  text-decoration: none;
    display: inline;
    box-shadow: inset 0 -15px 0 #8DDCA4; 
}
.binder{
  background-image: url("@/assets/clipboard.png");
  width:900px;
  height:1000px;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  
}
.following_status {
  background-color: blue;
  color: beige;
  flex-direction: row;
}

.profile-card {
  width:450px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  margin:10px;
  padding:20px;
  border: 10px solid rgba(black, .1);
  background-color: #ffffff;
  border-radius:30px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}

.profile-card img{
  width: 150px;
  height: 150px;
  
}

.username-tag{
  font-size:40px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: space-between;

}
.name-tag {
  font-size: 15px;
  font-weight: 200;
}
.nickname-tag {
  font-size: 20px;
  font-weight: 400;
  color: #627278;
}
.genre_icon{
  max-width: 80px;
  background-color: #8DDCA4;
  border-radius:5px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  padding: 5px;
  margin: 5px;
  color: #3b322c;
  font-weight: 600;
  text-align: center;
  display: flex;
  min-width: 80px;
  justify-content: center;
  
}
.movie_icon{
  max-width: 80px;
  background-color: #8DDCA4;
  border-radius:5px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  padding: 5px;
  margin: 5px;
  color: #3b322c;
  font-weight: 600;
  text-align: center;
  display: flex;
  min-width: 230px;
  justify-content: center;
  
}
.feelog-container{ 
  display: flex;
  justify-content: center ;
 } 
@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translate3d(0, 100%, 0);
    }
    to {
        opacity: 1;
        transform: translateZ(0);
    }
}

.clipboard{
  display: flex;
  justify-content: space-between;
  width: 5000px;
  animation: fadeInUp 1s;
}

a{
  text-decoration: none;
}

.name-tag > span{
  color : #F58080;
  font-weight: 500;
}
</style>
