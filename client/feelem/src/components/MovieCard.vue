<template>
  <div>
    <div v-if="showsHome" class="cards">
      <b-col class="card-container">
        <b-card
          :img-src="posterPath"
          img-alt="Image"
          img-top
          style="max-width: 20rem; min-height: 470px"
          class="card h-100"
        >
          <b-card-title class="card-title">{{ movie?.title }} </b-card-title>
          <b-card-text class="overview">
            {{ movie?.overview }}
          </b-card-text>
        </b-card>
      </b-col>
    </div>

    <div v-if="showsDetail && movie" class="detail-group">
      <p data-scroll="out" class="detail-title">{{ movie.title }}</p>
      <p data-scroll="out" class="detail-overview">{{ movie.overview }}</p>
      <section class="detail-info">
        <img :src="backdropPath" alt="backdrop" class="backdrop" />
        <div class="detail-description">
          <p class="desc">
            평점 <span class="desc-tag">{{ movie.vote_average }}</span>
          </p>
          <p class="desc">
            개봉일 <span class="desc-tag">{{ movie.release_date }}</span>
          </p>
          <span class="genre-tag"> {{ movie.genres[0]?.name }} </span>
          <span class="genre-tag"> {{ movie.genres[1]?.name }} </span>
          <div data-scroll class="desc likes">
            <span class="popularity"> {{ movie.popularity }}</span
            >명의 사람이 이 영화를 좋아해요!
          </div>
        </div>
      </section>
    </div>
  </div>
</template>
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
  updated() {
    if (this.so) return;
    this.so = ScrollOut({
      scope: this.$el.querySelector(".detail-group")
    });
  },
  destroyed() {
    this.so.teardown();
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

<style scoped>
.detail-description {
  padding: 10px;
  animation: fadein 3s;
  -moz-animation: fadein 3s; /* Firefox */
  -webkit-animation: fadein 3s; /* Safari and Chrome */
  -o-animation: fadein 3s; /* Opera */
}
@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.likes {
  padding-top: 11rem;
}

.genre-tag {
  width: 50px;
  padding: 10px 20px;
  border-radius: 26px;
  border: 2px solid #627278;
  background-color: #627278;
  margin: 5px;
  font-size: 20px;
  color: white;
}

.popularity {
  font-size: 1.5em;
  font-weight: 700;
  color: #8ddca4;
}
.desc {
  font-size: 2em;
  margin-bottom: 1em;
  color: #3b322c;
}
.desc-tag {
  font-size: 1.5em;
  font-weight: 900;
  color: #8ddca4;
}

.detail-group {
  margin: 10em;
}

.detail-info {
  display: flex;
  gap: 30px;

  padding-top: 30px;
}

div.cards img {
  min-height: 380px;
}

img {
  filter: grayscale(30);
  transition: filter 0.5s;
}

img:hover {
  filter: grayscale(0);
}

.card-container {
  margin-bottom: 30px;
}

.overview {
  line-height: 21px;
  height: calc(2 * 21px);
  overflow: hidden;
}

.card-title {
  overflow: hidden;
  height: 60px;
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
  text-decoration: none;
  font-size: 7em;
  font-weight: 600;
  font-family: "Nanum Myeongjo", serif;
  color: #3b322c;
}
.detail-overview {
  font-size: 3em;
  font-family: "Nanum Myeongjo", serif;
  color: #627278;
}
.detail-overview::first-line {
  font-size: 1.2em;
  font-family: "Nanum Myeongjo", serif;
  color: #8ddca4;
  font-weight: 700;
}

html[data-scroll-dir-y="0"] .detail-overview {
  transition-delay: 1s;
}

/* TODO: make global */
[data-scroll] {
  transition-property: transform opacity;
  transition-duration: 2s;
  transition-timing-function: cubic-bezier(0.165, 0.84, 0.44, 1);
}

[data-scroll="in"] {
  opacity: 1;
  transform: translateX(0) scale(1) rotate(0);
}

[data-scroll="out"] {
  opacity: 0;
  transform: translateX(6rem) scale(0.92) rotate(6deg);
}

.backdrop {
  width: 50%;
}
</style>