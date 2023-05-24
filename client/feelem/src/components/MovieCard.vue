<template>
  <div>
    <div v-if="showsHome">
      <b-col class="card-container" v-if="movie">
        <b-card
          :img-src="posterPath"
          img-alt="Image"
          img-top
          style="max-width: 20rem"
          class="card h-100"
        >
          <b-card-title class="card-title">{{ movie.title }} </b-card-title>
          <b-card-text class="overview">
            {{ movie.overview }}
          </b-card-text>
        </b-card>
      </b-col>
    </div>

    <div v-if="showsDetail">
      <div v-if="movie" class="detail-group">
        <div data-scroll>
        <p class="detail-title">{{ movie.title }}</p>
        <p class="detail-overview">{{ movie.overview }}</p>
        </div>
        <section class="detail-info">
        <img :src="backdropPath" alt="backdrop" class="backdrop" />
        <div class="detail-description">
        <p class="desc">평점 <span class="desc-tag">{{ movie.vote_average }}</span></p>
        <p class="desc">개봉일 <span class="desc-tag">{{ movie.release_date }}</span></p>
        <span class="genre-tag"> {{ movie.genres[0]?.name }} </span>
        <span class="genre-tag"> {{ movie.genres[1]?.name }} </span>
        
        </div>
        </section>
      </div>
    </div>
  </div>
</template>
<script src="https://unpkg.com/scroll-out/dist/scroll-out.min.js"></script>
<script>
import ScrollOut from "scroll-out";


export default {
  name: "MovieCard",
  props: {
    movie: Object,
    showsVote: Boolean,
    showsOverview: Boolean,
    showsHome: Boolean,
    showsDetail: Boolean,
  },
  data() {
    return {
      isMovieSaved: false,
    };
  },
  computed: {
    posterPath() {
      return "https://image.tmdb.org/t/p/w500" + this.movie.poster_path;
    },
    backdropPath() {
      return "https://image.tmdb.org/t/p/w500" + this.movie.backdrop_path;
    },
  },
  created(){
    
  },
  mounted() {
    ScrollOut({
      threshold : 0
    });
  },
  methods: {
    saveMovie() {
      this.isMovieSaved = !this.isMovieSaved;
      const id = this.$route.params.id;
      this.$store.dispatch("saveMovie", id);
    },
  },
};
</script>

<style>

.genre-tag{
  width: 50px;
  padding : 10px 20px;
  border-radius: 26px;
  border : 2px solid #8ddca4;
  background-color:  #8ddca4;
  margin: 5px;
  font-size: 20px;
  
}
.desc{
  font-size: 2em;
  margin-bottom: 1em;
  color : #3b322c;
}
.desc-tag {
  font-size: 1.5em;
  font-weight: 900;
  color : #8ddca4;
}

.detail-group{
  margin: 10em;
}

.detail-info{
  display: flex;
  gap: 30px;
  border-top: 1px solid black;
  padding-top: 30px;
}

img {
  width: 200px;
  filter: grayscale(30);
}

img:hover {
  filter: grayscale(0);
  transition: 0.5s;
}

.card-container {
  margin-bottom: 30px;
}

.overview {
  line-height: 21px;
  height: calc(2 * 21px);
  overflow: hidden;
}

.overview::after {
  content: "";

  position: absolute;
  bottom: 0;
  right: 0;
  height: 2px;
  width: 75%;

  background: linear-gradient(90deg, transparent, white);
}
.detail-title {
  font-size: 6em;
  font-weight: 600;
  font-family: "Nanum Myeongjo", serif;
  color : #3b322c;
}
.detail-overview {
  font-size: 3em;
  font-family: "Nanum Myeongjo", serif;
  color: #627278;
}

[data-scroll] {
  opacity: 0;
  will-change: transform, scale, opacity;
  transform: translateX(6rem) scale(0.92);
  transition: all 2s cubic-bezier(0.165, 0.84, 0.44, 1);
}

[data-scroll="in"] {
  opacity: 1;
  transform: translateX(0) scale(1);
}

[data-scroll="out"] {
  opacity: 0;
}

.backdrop {
  width: 50%;
}
</style>