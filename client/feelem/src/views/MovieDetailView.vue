<template>
  <div>
   <h1>영화 상세</h1>
   <div>

    <!-- {{getMovieInfo.title}}
    <img :src="getImageUrl" alt="posterImage"> -->
    <MovieCard :movie = movie showsOverview showsVote/>
  </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name : 'MovieDetailView',
  components : {
    MovieCard,
  },
  data() {
    return {
      
    }
  },
  created(){
    const id = this.$route.params.id
    this.$store.dispatch("fetchSingleMovie", id)
    this.$store.dispatch('fetchFeelogDetail', id)
  },
  computed : {
    movie() {
      const id = this.$route.params.id
      return this.$store.state.movies.find(movie => movie.id == id)
    }
  },

}
</script>

<style>

</style>