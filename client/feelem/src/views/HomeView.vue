<template>
  <div>
    메인 홈홈홈
    <MovieCard v-for="(movie, index) in movieList" :key="index" :movie = movie />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name : 'HomeView',
  components : {
    MovieCard,
  },
  data() {
    return {
      
    }
  }

}
</script>

<style>

</style>