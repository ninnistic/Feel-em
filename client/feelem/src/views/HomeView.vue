<template>
  <div>
    메인 홈홈홈
    <MovieCard v-for="(movie) in movieList" :key="movie.id" :movie = movie />
    <FeelogCard v-for="(feelog) in feelogList" :key="feelog.id" :feelog = feelog />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import FeelogCard from '@/components/FeelogCard'

export default {
  name : 'HomeView',
  components : {
    MovieCard,
    FeelogCard,
  },
  computed: {
    movieList() {
      return this.$store.getters.getRecommendedMovies
    },
    feelogList() {
      return this.$store.getters.getRecommendedFeelogs

    }
  },
  created(){
    this.$store.dispatch('fetchMovieList')
    this.$store.dispatch('fetchFeelogList')
  }
}
</script>

<style>

</style>