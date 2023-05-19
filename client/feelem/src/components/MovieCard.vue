<template>
  <div>
    <p>{{movie.title}}</p>
    <img :src= alt="">
  </div>
</template>

<script>
export default {
  name : 'MovieCard', 
  props : {
    movie : Object,
  },
  computed :{
    posterPath() {
      return "https://image.tmdb.org/t/p/w400"+this.movie.poster_path
    }
  }
}
</script>

<style>

</style>