<template>
  <!-- <div class="card" v-if="movie">
    <div class="card-body">
      <img :src="posterPath" alt="posterImage">
      <p>{{movie.title}}</p>
      <button @click="save_movie" :class="{ save_status : issaved}">follow</button>
      <p v-if="showsVote"> 평점 : {{movie.vote_average}}</p>
      <p v-if="showsOverview">{{movie.overview}}</p>
    </div>
  </div> -->

  <b-col class="card-container"  v-if="movie">
      <b-card :img-src="posterPath" img-alt="Image" img-top style="max-width:20rem" class="card h-100">
        <b-card-title class="card-title">{{movie.title}}</b-card-title>
      <b-card-text class="overview" >
        {{ movie }}
        {{ movie.overview }}
      </b-card-text>
      <p v-if="showsVote"> 평점 : {{movie.vote_average}}</p>
      <button @click="saveMovie" v-if="isMovieSaved" >♥</button>
      <button @click="saveMovie" v-else >♡</button>
      <!-- <template #footer>
        <small class="text-muted" > {{movie.id}} 명의 사람이 추천했어요</small>
      </template> -->
    </b-card>
  </b-col>

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
      isMovieSaved:false
    }
  },
  computed : {
    posterPath() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    },
  },
  methods:{
    saveMovie() {
          this.isMovieSaved = !this.isMovieSaved
          const id = this.$route.params.id 
          this.$store.dispatch('saveMovie',id )
    }
  },
}
</script>

<style>


img{
  width: 200px;
}

.card-container{
  margin-bottom: 30px;
}

.overview {
  line-height: 21px;
  height: calc(2 * 21px);
  overflow : hidden;
}

.overview::after {
  content : '';
  
  position : absolute;
  bottom: 0;
  right: 0;
  height: 2px;
  width: 75%;

  background: linear-gradient(90deg, transparent, white);
}

</style>