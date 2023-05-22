<template>
  <div>
    <router-link v-for="(movie, index) in movieList" :key="index" :to="'/movie-detail/' + movie.id">
      <MovieCard :movie = movie showsVote />
    </router-link>
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
    this.$store.dispatch('fetchMovieList')
  },
  methods : {

  }
}
</script>

<style>

</style>