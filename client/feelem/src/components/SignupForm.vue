<template>
  <div>
    <div>
      <div class="form-group" v-if="genres">
        <form @submit.prevent="signUp">
          <div>
            <label for="username" class="title-tag">* Username</label>
            <input type="text" v-model="username" id="username">
          </div>
          <div>
            <label for="email" class="title-tag">* Email</label>
            <input type="text" v-model="email" id="email" autocomplete="off">
          </div>
          <div>
            <label for="password" class="title-tag">* Password</label>
            <input type="password" v-model="password" id="password">
          </div>
          <div>
            <label for="passwordConfirm" class="title-tag">* Password check</label>
            <input type="password" v-model="passwordConfirm" id="passwordConfirm">
          </div>
          <p class="title-tag">* 선호하는 장르 </p>
          <section class="genre-card">
          <div v-for="genre in genres" :key="genre.id" class="genre">
            <span :value="genre.id" @click="saveGenre(genre.id)" :class="{ selected: isSelected(genre.id) }" class="genre-btn" >{{ genre.name }}</span>
          </div>
          </section>
          <div>
            <label for="goal_of_month" class="title-tag">월별 목표</label>
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

<style scoped>
.title-tag{
  font-size: 1.7em;
  font-weight: 700;
  color :  #3B322C;
}
.genre-card{
  display : flex;
  flex-wrap: wrap;
  gap: 20px 2%;
  width: 50%;
  margin-bottom : 2em;
}

.genre-btn{
  background-color: #8DDCA4;
  color: #3B322C;
  display: inline-block;
  border : solid 1px white;
  border-radius: 20px;
  padding : 10px 20px; 
  cursor : pointer;
}


.selected {
  background-color: #3B322C;
  color : #F4F3EE;
}
.genre-btn:hover{
  background-color: #3B322C;
  color : #F4F3EE;
  transition: 0.1s;
}

input[type=text], input[type=password]{
  width : 100%;
  height: 50px;
  font-size: 1.5em;
  outline : none;
  padding-left : 20px;
  color : #627278;
  border-bottom: 1px solid #627278;
  margin-bottom : 20px;
}
</style>