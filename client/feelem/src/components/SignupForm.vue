<template>
  <div class="card">
    <div class="card-body">
      <div class="form-group" v-if="genres">
        <form @submit.prevent="signUp">
          <div>
            <label for="username">username:</label>
            <input type="text" v-model="username" id="username">
          </div>
          <div>
            <label for="email">email:</label>
            <input type="text" v-model="email" id="email" autocomplete="off">
          </div>
          <div>
            <label for="password">password:</label>
            <input type="password" v-model="password" id="password">
          </div>
          <div>
            <label for="passwordConfirm">password check:</label>
            <input type="password" v-model="passwordConfirm" id="passwordConfirm">
          </div>
          <label for="favorite_genre">장르 선택:</label>
          <div v-for="genre in genres" :key="genre.id">
            <span :value="genre.id" @click="saveGenre(genre.id)" :class="{ selected: isSelected(genre.id) }" class="genre-btn" >{{ genre.name }}</span>
          </div>
          <div>
            <label for="goal_of_month">월별 목표:</label>
          <div>
            <b-form-select v-model="goal_of_month" :options="options" :select-size="4"></b-form-select>
            <div class="mt-3">Selected: <strong>{{ goal_of_month }}</strong></div>
          </div>

          </div>
          <input type="submit" value="signup">
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupForm',
  data() {
    return {
      username: null,
      email: null,
      password: null,
      passwordConfirm: null,
      goal_of_month: 1,
      favorite_genre: [],
        options: [
          { value: 1, text: '1' },
          { value: 2, text: '2' },
          { value: 3, text: '3' },
          { value: 4, text: '4' },
          { value: 5, text: '5' },
          { value: 6, text: '6' },
          { value: 7, text: '7' },
          { value: 8, text: '8' },
          { value: 9, text: '9' },
          { value: 10, text: '10' }
        ]
    };
  },
  created() {
    this.fetchGenres();
  },
  computed: {
    genres() {
      return this.$store.state.genres;
    },
  },
  methods: {
    signUp() {
      const username = this.username;
      const email = this.email;
      const password = this.password;
      const passwordConfirm = this.passwordConfirm;
      const goal_of_month = this.goal_of_month;
      const favorite_genre = this.favorite_genre;

      const payload = {
        username,
        password,
        passwordConfirm,
        email,
        goal_of_month,
        favorite_genre,
      };
      this.$store.dispatch('signUp', payload);
    },

    fetchGenres() {
      this.$store.dispatch('fetchGenres');
    },

    saveGenre(genre_id) {
      const index = this.favorite_genre.indexOf(genre_id);
      if (index === -1) {
        console.log(this.favorite_genre)
        this.favorite_genre.push(genre_id);
        if(this.favorite_genre.length > 5){
          alert('장르는 5개까지만 선택할 수 있습니다!')
          this.favorite_genre.splice(index, 1);
        }
      } else {
        this.favorite_genre.splice(index, 1);
      }
    },

    isSelected(genre_id) {
      return this.favorite_genre.includes(genre_id);
    },
  },
};
</script>

<style>
.selected {
  background-color: #3B322C;
  color : #F4F3EE
}

.genre-btn{
  display: inline-block;
  border : solid #3B322C 2.5px;
  border-radius: 10px;
  padding : 6px; 
  margin: 5px;
  cursor : pointer;
}
.genre-btn:hover{
  background-color: #8DDCA4;
  transition: 0.1s;
}
</style>