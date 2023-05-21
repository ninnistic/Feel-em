<template>
  <div>
   <h1>영화 상세</h1>
   <div>
    {{getMovieInfo.title}}
    <img :src="getImageUrl" alt="posterImage">
  </div>
  </div>
</template>

<script>


export default {
  name : 'MovieDetailView',
  components : {

  },
  data() {
    return {
    }
  },
  created(){
    this.getMovieDetail()
    this.getFeelogDetail()
  },
  methods : {
    getMovieDetail(){
      const id = this.$route.params.id
      this.$store.dispatch('getMovieDetail', id)
    },
    getFeelogDetail() {
      const id = this.$route.params.id
      this.$store.dispatch('getFeelogDetail', id)
    }

  },
  computed : {
    getImageUrl() {
      return `https://image.tmdb.org/t/p/w500`+ this.$store.state.movie.poster_path
    },
    getMovieInfo(){
      return this.$store.state.movie
    }
  },

}
</script>

<style>

</style>