<template>
  <div class="account-container mx-5 px-5">
      <p class="feelmo"><span>{{profile.username}}</span>'s feelmography</p>
    <div class="clipboard">
      <div class="binder">
        <div class="profile-card mx-5">
          <img :src="profile_pics" alt="profile_imgs" />
          <div>
            <div class="username-tag">
              {{ profile.username }}
              <b-button
                v-if="!isCurrentUser"
                @click="follow"
                variant="primary"
                size="xs"
                :class="{ following_status: isfollowed }"
                style="width:50px;height:20px;"
              >
              <span style="font-size:10px; " v-if="isfollowed">Unfollow</span>
              <span style="font-size:10px; " v-else>Follow</span>
                <!-- {{ isfollowed ? "Unfollow" : "Follow" }} -->
              </b-button>
              <!-- <b-button v-else variant="primary" size="sm">
                프로필 수정
              </b-button> -->
            </div>
            <div class="nickname-tag">
              <span><span class="fav-genre">{{ profile.favorite_genre[0]?.name }}</span> 장르 애호가 </span>
            </div>
            <div class="name-tag">
              Following <span> {{ profile.followings_count }} </span>
            </div>
            <span>이 달의 Feelog 작성 목표 : {{ profile.goal_of_month}}</span>
          </div>
        </div>
        <br />
        <div>
        
          <div>
            <div class="d-flex my-3" style="align-self: self-start">
              <h1 class="fw-bold username" style="align-self: self-start">
                {{ profile.username }}
                
              </h1>
              <h1 class="description">님의 선호 장르</h1>
            </div>

            <div class="genre_icon_container">
              <div style="color:white"
                v-for="genres in profile.favorite_genre"
                :key="genres.id"
                class="genre_icon"
              >
                <span>{{ genres.name }} </span>
              </div>
            </div>
            <br />
            <br />
            <div class="d-flex my-3" style="align-self: self-start">
              <h1 class="fw-bold username" style="align-self: self-start">
                {{ profile.username }}
              </h1>
              <h1 class="description">님이 찜한 영화</h1>
            </div>
            <div class="genre_icon_container">
              <div
              style="color:white"
                v-for="movies in profile.save_movies"
                :key="movies.id"
                class="movie_icon"
              >
                <span>{{ movies.title }} </span>
              </div>
            </div>
            <br />
          </div>
          <div class="d-flex my-3" style="align-self: self-start">
            <h1 class="fw-bold username" style="align-self: self-start;">
              {{ profile.username }}
            </h1>
            <h1 class="description">님의 Feelmers</h1>
          </div>
         

          <div class="genre_icon_container">
            <router-link
              v-for="otherfeelmer in profile.followings"
              :key="otherfeelmer.id"
              :to="'/account/' + otherfeelmer.username"
            >
              <div style="color:white;" class="genre_icon">{{ otherfeelmer.username }}</div>
            </router-link>
          </div>
        </div>
      </div>
      
      <div class="feelog-card m-5 p-5">
        <div class="moods mb-5 pb-5">
          <div><h1 class="fw-bold username" style="width:198px;">이 달의 감정</h1></div>
          <br>
          <div style="display:flex;" >
            <h3 class="fw-bold" style="padding-left:10px;"># {{currentUserFeelogs[0].mood?.title}}:{{currentUserFeelogs[0].mood?.title_count}}</h3>
            <h3 class="fw-bold" style="padding-left:10px;"># {{currentUserFeelogs[1].mood?.title}}:{{currentUserFeelogs[1].mood?.title_count}}</h3>
            <h3 class="fw-bold" style="padding-left:10px;">#{{currentUserFeelogs[2].mood?.title}}:{{currentUserFeelogs[2].mood?.title_count}}</h3>

            </div>
            <br>
            <br>
        </div>
        <div class="d-flex my-3" style="align-self: self-start">
          <h1 class="fw-bold username" style="align-self: self-start">
            {{ profile.username }}
          </h1>
          <h1 class="fw-bold">님의 Feelog</h1>
        </div>
        <br />

        <router-link
          v-for="feelog in feelogs"
          :key="feelog.id"
          :to="'/feelog-detail/' + feelog.id"
        >
          <FeelogCard
            :feelog="feelog"
            class="feelog-container-account my-5"
            homeFeelog
          />
        </router-link>
      </div>
    </div>
  </div>
</template>

<script scoped>
import FeelogCard from "@/components/FeelogCard";

export default {
  name: "AccountView",
  components: {
    FeelogCard,
  },
  data() {
    return {
      isfollowed: false,
      account: true,
    };
  },
  created() {
    const nickname = this.$route.params.nickname;
    this.$store.dispatch("fetchProfile", nickname);
    this.$store.dispatch("fetchFeelogsByName", nickname);
  },
  mounted() {},
  methods: {
    follow() {
      console.log(this.$store.state.profile);
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
      return this.$store.state.profile;
    },
    currentUserFeelogs() {
      return this.$store.state.currentUserFeelogs;
    },
    profile_pics() {
      return this.profile.profile_pic.image;
    },
    profile_genre() {
      return this.profile.favorite_genre.name;
    },
    feelogs() {
      // const nickname = this.$route.params.nickname
      // return this.$store.state.feelogs.filter(feelog => feelog.username == nickname)
      const nickname = this.$route.params.nickname;
      return this.$store.getters.getUserFeelogsByName(nickname);
    },

    feelogcnt() {
      return length(this.feelog);
    },
    isCurrentUser() {
      const currentUsername = this.$store.state.nickname;
      return this.$route.params.nickname === currentUsername;
    },
  },
};
</script>

<style scoped>
.fav-genre{
  background-color : #f58080;
  color : white;
  padding: 3px 5px;
  border-radius: 4px;
}
.moods{
  height: 50px;
  display:flex;
  flex-direction:column;
  position: relative;
  top:-50px;
  left: 5px;
}

.moods > p {
  font-size: 20px;
  color:#3b322c;
}
.feelmo{
  font-weight: 700;
  font-size: 3rem;
  text-align: center;
  height: 10rem;
  padding-bottom: 5em;
  padding-top: 1em;
}
.feelmo > span{
  font-size: 4rem; 
}
.feelog-card {
  width: 100%;
}
.genre_icon_container {
  display: flex;
}
.username {
  text-decoration: none;
  /* display: inline; */
  box-shadow: inset 0 -15px 0 #8ddca4;
}
.binder {
  background-image: url("@/assets/clipboard.png");
  width: 900px;
  height: 1000px;
  background-size: cover;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.following_status {
  background-color: #8ddca4;
  color: white;
  flex-direction: row;
}

.profile-card {
  width: 450px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  margin: 10px;
  padding: 20px;
  border: 10px solid rgba(black, 0.1);
  background-color: #ffffff;
  border-radius: 30px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
}

.profile-card img {
  width: 150px;
  height: 150px;
}

.username-tag {
  font-size: 40px;
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
.genre_icon {
  max-width: 80px;
  background-color: #8ddca4;
  border-radius: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  padding: 5px;
  margin: 5px;
  color: #3b322c;
  font-weight: 600;
  text-align: center;
  display: flex;
  min-width: 80px;
  justify-content: center;
}
.movie_icon {
  max-width: 80px;
  background-color: #8ddca4;
  border-radius: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24);
  padding: 5px;
  margin: 5px;
  color: #3b322c;
  font-weight: 600;
  text-align: center;
  display: flex;
  min-width: 230px;
  justify-content: center;
}
.feelmo{
  animation: fadeInUp 1s;
}

.feelog-container {
  display: flex;
  justify-content: center;
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

.clipboard {
  display: flex;
  justify-content: space-between;
  width: 5000px;
  animation: fadeInUp 1s;
}

a {
  text-decoration: none;
}

.name-tag > span {
  color: #f58080;
  font-weight: 700;
}

.name-tag{
  font-weight: 500;
}
</style>
