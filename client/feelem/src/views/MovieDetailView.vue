<template>
  <div>
   <h1>영화 상세</h1>
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
  }

}
</script>

<style>

</style>