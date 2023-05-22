<template>
  <div>
   <h1>영화 상세</h1>
   <div>

    <!-- {{getMovieInfo.title}}
    <img :src="getImageUrl" alt="posterImage"> -->
    <MovieCard :movie = movie showsOverview showsVote/>
    <FeelogCard v-for="feelog in feelogs" :feelog = feelog :key="feelog.id" showsContent />
    <FeelogCreateForm />
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
      return this.$store.state.movies.find(movie => movie.id == id)
    },
    feelogs() {
      const id = this.$route.params.id
      const res = this.$store.state.feelogs.filter(feelog => feelog.movie == id)
      console.log(this.$store.state.feelogs)
      return res
    }
  },

}
</script>

<style>

</style>