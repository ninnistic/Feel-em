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
  },
  methods : {
    getMovieDetail(){
      const id = this.$route.params.id
      this.$store.dispatch('getMovieDetail', id)
    }
  },
  computed : {
    getImageUrl() {
      return `https://image.tmdb.org/t/p/w500`+ this.$store.state.movie.data.poster_path
    },
    getMovieInfo(){
      return this.$store.state.movie.data
    }
  },

}
</script>

<style>

</style>