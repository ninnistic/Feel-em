<template>
  <div>
    메인 홈홈홈
    <router-link
      v-for="movie in movieList"
      :key="movie.id"
      :to="'movie-detail/' + movie.id"
    >
      <MovieCard :movie="movie" />
    </router-link>

    <FeelogCard
      v-for="feelog in feelogList"
      :key="feelog.id"
      :feelog="feelog"
    />
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard";
import FeelogCard from "@/components/FeelogCard";

export default {
  name: "HomeView",
  components: {
    MovieCard,
    FeelogCard,
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

<style>
</style>