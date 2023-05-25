<template>
  <div class="container">
  <div class="d-flex m-1 ">
    <b-container class="mb-1">
      <b-row cols="5">
    <router-link  v-for="(movie, index) in movieList" :key="index" :to="'/movie-detail/' + movie.id" >
      <MovieCard :movie = movie showsVote showsHome/>
    </router-link>
    </b-row>
  </b-container>

  </div>
</div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name : 'MovieListView',
  components : {
    MovieCard,
  },
  computed : {
    movieList(){
      return this.$store.state.movies
    }

  },
  created() {
    this.$store.dispatch('fetchMovieList')
  },
  methods : {

  }
}
</script>

<style>

</style>


<style scoped>
.link{
  text-decoration: none;
}
.container{
  display: flex;
  justify-content: center;
  align-items : center;
  flex-direction: row;
  margin : 1rem;
  align-self: center;
}
a {
  text-decoration: none;
  transition: transform .5s;
}

h1{
  font-weight: 800;
}

a:hover{
  transform: scale(1.05);
}
</style>
