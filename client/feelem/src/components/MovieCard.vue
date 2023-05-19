<template>
  <div class="card">
    <div class="card-body">
      <img :src="posterPath" alt="posterImage" @click="movieDetail">
      <p>{{movie.title}}</p>
      <p> 평점 : {{movie.vote_average}}</p>
      <p>{{movie.movie_id}}</p>
    </div>

   
  </div>
</template>

<script>
export default {
  name : 'MovieCard', 
  props : {
    movie : Object,
  },
  data() {
    return {
      id : this.movie.movie_id
    }
    
  },
  computed : {
    posterPath() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    }
  },
  methods : {
    movieDetail(){
      console.log(this.movie)
      return this.$router.push(`movie-detail/` + this.id)
    }
  }
}
</script>

<style>

</style>