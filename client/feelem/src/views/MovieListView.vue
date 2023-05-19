<template>
  <div>
    <MovieCard v-for="(movie, index) in movieList" :key="index" :movie = movie />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name : 'MovieListView',

  components : {
    MovieCard,
  },
  computed : {
    movieList(){
      return this.$store.state.movies
    }

  },
  created() {
    this.getMovieList()
  },
  methods : {
    getMovieList(){
      this.$store.dispatch('getMovieList')
    }
  }
}
</script>

<style>

</style>