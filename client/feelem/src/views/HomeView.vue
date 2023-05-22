<template>
  <div>
    메인 홈홈홈
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