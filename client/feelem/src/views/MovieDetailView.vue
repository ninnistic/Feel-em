<template>
  <div>
  <div class="items">
    <MovieCard :movie = movie showsDetail/>
    <FeelogCard v-for="feelog in feelogs" :feelog = feelog :key="feelog.id"  detailFeelog />
    <FeelogCreateForm :movie_id = movie_id />
  </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
import FeelogCard from '@/components/FeelogCard'
import FeelogCreateForm from '@/components/FeelogCreateForm'

export default {
  name : 'MovieDetailView',
  components : {
    MovieCard,
    FeelogCard,
    FeelogCreateForm
  },
  data() {
    return {
      movie_id : this.$route.params.id
    }
  },
  created(){
    const id = this.$route.params.id
    this.$store.dispatch("fetchSingleMovie", id)
    this.$store.dispatch('fetchFeelogsForMovieId', id)
  },
  computed : {
    movie() {
      
      const id = this.$route.params.id
      console.log(this.$store.state.movies.find(movie => movie.id == id))
      return this.$store.state.movies.find(movie => movie.id == id)
    },
    feelogs() {
      const id = this.$route.params.id
      return this.$store.state.feelogs.filter(feelog => feelog.movie == id)
      
    }
  },

}


</script>

<style scoped>

.loading {
  z-index: 2;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: rgba(0, 0, 0, 0.1) 0 0 0 9999px;
}


</style>

