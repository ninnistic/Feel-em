<template>
<div>
  <div class="video"> 
    <VideoCard /> 
  </div>
  <div class="d-flex m-1 container">
    <b-container class="mb-1">
      <b-row cols="5">
    <router-link
      v-for="movie in movieList"
      :key="movie.movie_num"
      :to="'movie-detail/' + movie.id"
    >
      <MovieCard :movie="movie" />
    </router-link>

    <router-link
      v-for="feelog in feelogList"
      :key="feelog.id"
      :to="'feelog-detail/' + feelog.id"
    >
      <FeelogCard
        :feelog="feelog"
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
  },
  created() {
    this.$store.dispatch("fetchMovieList");
    this.$store.dispatch("fetchFeelogList");
  },
};
</script>

<style scoped>
.container{
  display: flex;
  justify-content: center;
  align-items : center;
  flex-direction: column;
  margin : 1rem;
}

.video{
  position: relative;
  top:0px;
  width:100%;
}
</style>
