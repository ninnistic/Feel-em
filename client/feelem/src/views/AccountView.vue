<template>
  <div>
    <!--TODO: 나중에 ProfileCard 만들어서 다 옮기기... -->
    <div class="profile-card">
      <!-- <img src="@/assets/emotion/mood (1).png" alt=""> -->
      <img src="@/assets/profile/OBJECTS_03.png" alt="" />
      <h2>{{ profile.username }}</h2>
      <b-button v-if="!isCurrentUser" @click="follow" variant="primary" :class="{ following_status: isfollowed }">
        Follow
      </b-button>
      <ul>
        <li>Following: 50</li>
        <li>Followers: 100</li>
      </ul>
    </div>
    <div class="name-tag">
      <span>{{ profile.favorite_genre[0]?.name }} 장르 애호가 </span>
    </div>
    <div>이번달은 {{ profile.goal_of_month }}개의 영화를 볼거야!</div>
    <div v-if="isCurrentUser">
      <div>나는 {{ profile.favorite_genre[0]?.name }}같은 장르들을 좋아해!</div>
      <div>특히 {{ profile.save_movies[0]?.title }}가 보고 싶더라.</div>
      <div>
        관심가는 feelmers는
        <span v-for="feelmer in profile.followings" :key="feelmer.id">
          {{ feelmer.username }},</span
        >야.
      </div>
    </div>
    <span>내가 쓴 feelog는 : </span>
    <router-link
      v-for="feelog in feelogs"
      :key="feelog.id"
      :to="'/feelog-detail/' + feelog.id"
      >{{ feelog.title }}</router-link
    >
  </div>
</template>

<script>
export default {
  name: "AccountView",
  components: {},
  data() {
    return {
      isfollowed: false,
    };
  },
  created() {
    const nickname = this.$route.params.nickname;
    this.$store.dispatch("fetchProfile", nickname);
  },
  mounted() {},
  methods: {
    follow() {
      // follow 메서드 구현 (버튼을 클릭했을 때 호출될 동작)
      this.isfollowed = !this.isfollowed;
      const nickname = this.$route.params.nickname;
      this.$store.dispatch("follow", nickname);
      // 새로고침
      this.$router.go();
    },
  },
  computed: {
    profile() {
      return this.$store.state.profile;
    },
    feelogs() {
      // const nickname = this.$route.params.nickname
      // return this.$store.state.feelogs.filter(feelog => feelog.username == nickname)
      const nickname = this.$route.params.nickname;
      return this.$store.getters.getUserFeelogsByName(nickname);
    },
    isCurrentUser() {
      const currentUsername = this.$store.state.nickname;
      return this.$route.params.nickname === currentUsername;
    },
  },
};
</script>

<style scoped>
.following_status {
  background-color: blue;
  color: beige;
}
.container {
  position: relative;
  top: 200px;
}
.profile-card {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}

.profile-card button {
  grid-column: 2 / -1;
}

.profile-card ul {
  display: flex;
}
.profile-card li:not(:last-child):after {
  content: "\00a0|\00a0";
}
.profile-card button {
  background-color: var(--bs-blue);
}
/* .profile-card {
  display: flex;
  align-items: start;
}
.profile-greet {
  color: #3b322c;
  font-size: 4em;
  font-weight: 700;
  max-width: 300px;
  padding: 0;
  line-height: 1.25em;
} */
.name-tag {
  font-size: 1.5em;
  font-weight: 200;
  color: #627278;
}
</style>

