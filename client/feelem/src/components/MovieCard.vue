<template>
  <div class="card" v-if="movie">
    <div class="card-body">
      <img :src="posterPath" alt="posterImage">
      <p>{{movie.title}}</p>
      <button @click="save_movie" :class="{ save_status : issaved}">follow</button>
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
  data(){
    return{
      issaved:false
    }
  },
  computed : {
    posterPath() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    }
  },
  methods:{
    save_movie() {
          this.issaved = !this.issaved
          const id = this.$route.params.id 
          this.$store.dispatch('save',id)
        }
  },
}
</script>

<style>
.save_status{
  background-color: blue;
  color: beige;
}
</style>