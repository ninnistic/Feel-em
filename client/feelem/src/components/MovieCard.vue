<template>
  <div class="card">
    <div class="card-body">
      <img :src="posterPath" alt="posterImage">
      <p>{{movie.title}}</p>
      <p> 평점 : {{movie.vote_average}}</p>
    </div>

   
  </div>
</template>

<script>
export default {
  name : 'MovieCard', 
  props : {
    movie : Object,
  },
  computed : {
    posterPath() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    }
  }
}
</script>

<style>

</style>