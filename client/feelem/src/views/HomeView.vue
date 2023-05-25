<template>
  <div class="container">
    <div class="video">
      <VideoCard class="video" />
    </div>

    <div
      v-if="isLoggedIn"
      class="d-flex flex-column my-5 p-3"
      style="align-self: self-start"
    >
      <div class="d-flex">
        <h1 class="fw-bold username" style="align-self: self-start">
          지금 {{ nickname }}
        </h1>
        <h1 class="fw-bold">님께 딱 맞는 영화</h1>
        <br />
      </div>
      <div class="genre-recommend">
        <!-- {{ nickname }}님이 좋아하는 장르인 -->
        <!-- <span class="genre-point">{{ profile?.favorite_genre[0]?.name }}</span>
        <span class="genre-point">{{ profile?.favorite_genre[1]?.name }}</span>와 관련있는 영화들이예요! -->
      </div>
    </div>
    <div v-else class="d-flex my-5 p-3" style="align-self: self-start">
      <h1 class="fw-bold username" style="align-self: self-start">Feelmer</h1>
      <h1 class="fw-bold">님께 딱 맞는 영화</h1>
    </div>
    <div id="movie-containter" class="m-1 container">
      <b-container class="mb-1">
        <b-row cols="5">
          <router-link
            v-for="movie in movieList"
            :key="movie.movie_num"
            :to="'/movie-detail/' + movie.id"
          >
            <MovieCard :movie="movie" showsHome />
          </router-link>
        </b-row>
      </b-container>

      <div class="d-flex my-5 p-3" style="align-self: self-start">
        <h1 class="fw-bold username" style="align-self: self-start">
          Feelmer's PICK
        </h1>
      </div>
      <b-container class="mb-1">
        <b-row cols="2">
          <router-link
            v-for="feelog in feelogList"
            :key="feelog.id"
            :to="'/feelog-detail/' + feelog.id"
          >
            <FeelogCard
              :feelog="feelog"
              class="feelog-container m-3"
              homeFeelog
            />
          </router-link>
        </b-row>
      </b-container>
    </div>
  </div>
</template>


<script>
import MovieCard from "@/components/MovieCard";
import FeelogCard from "@/components/FeelogCard";
import VideoCard from "@/components/VideoCard";

export default {
  name: "HomeView",
  components: {
    MovieCard,
    FeelogCard,
    VideoCard,
  },
  computed: {
    movieList() {
      return this.$store.getters.getRecommendedMovies;
    },
    feelogList() {
      return this.$store.getters.getRecommendedFeelogs;
    },
    isLoggedIn() {
      return this.$store.getters.isSignedIn;
    },
    nickname() {
      return this.$store.state.nickname;
    },
    profile() {
      return this.$store.state.profile;
    },
  },
  created() {
    this.$store.dispatch("fetchMovieList");
    this.$store.dispatch("fetchRecommendedMovies");
    this.$store.dispatch("fetchFeelogList");
  },
  mounted() {
    document.body.classList.add("fixed-nav");
  },
  destroyed() {
    document.body.classList.remove("fixed-nav");
  },
};
</script>

<style scoped>
.genre-recommend {
  font-size: 20px;
}
.genre-point {
  font-weight: 500;
  background-color: #8ddca4;
  padding: 4px;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  position: relative;
  top: 30%;
  width: 100vw;
  margin-bottom: 100px;
}

a {
  text-decoration: none;
  transition: transform 0.5s;
}

.video {
  width: 100vw;
}

.username {
  text-decoration: none;
  display: inline;
  box-shadow: inset 0 -15px 0 #8ddca4;
}
a:hover {
  transform: scale(1.05);
}
</style>