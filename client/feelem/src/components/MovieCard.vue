<template>
  <div class="card">
    <div class="card-body">
      <img :src="posterPath" alt="posterImage">
      <p>{{movie.title}}</p>
      <p v-if="showsVote"> 평점 : {{movie.vote_average}}</p>
      <p v-if="showsOverview">{{movie.overview}}</p>
    
    </div>

   
  </div>
</template>

<script>
export default {
  name : 'MovieCard', 
  props : {
    movie : Object,
    showsVote: Boolean,
    showsOverview: Boolean,
  },
  computed : {
    posterPath() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    }
  },
  methods : {
  }
}
</script>

<style>

</style>