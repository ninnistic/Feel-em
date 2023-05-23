<template>
  <div class="card">
    <div class="card-body">
      <div class="form-group">
        <form @submit.prevent="signUp">
        <div>
        <label for="username" >username : </label>
        <input type="text" v-model="username" id="username" >
        </div>
        <div>
        <label for="email">email : </label>
        <input type="text" v-model="email" id="email" autocomplete="off">
        </div>
        <div>
        <label for="password">password : </label>
        <input type="password" v-model="password" id="password" >
        </div>
        <div>
        <label for="passwordConfirm">password check : </label>
        <input type="password" v-model="passwordConfirm" id="passwordConfirm">
        </div>
        <div>
          <!--장르 선택 할 수 있도록 아아아아아아악~~~~~~~~~~~~~~ 수정하기 ~~~~~~~ 200에러~~~~~~~ 왜안떠? --> 
        <label for="favorite_genre">장르 선택 : </label>
        <select name="" id="">
          <option :value="genre.name" v-for="genre in genres" :key="genre.id">{{genre.name}}</option>
        </select>
        </div> 
        <div>
        <label for="goal_of_month">월별 목표: </label>
        <input type="text" v-model="goal_of_month" id="goal_of_month">
        </div> 
        <input type="submit" value="signup">
        </form>
    </div>
    </div>
  </div>
</template>

<script>


export default {
  name : 'SignupForm',
  data() {
    return {
        username : null,
        email: null,
        password : null,
        passwordConfirm : null,
        goal_of_month: null,
        favorite_genre: [],      
    }
  },
  created() {
    this.fetchGenres()
  },
  computed : { 
    genres(){
      return this.$store.store.genres
    }
  },
  methods : {
    signUp() {
      const username = this.username
      const email = this.email
      const password = this.password
      const passwordConfirm = this.passwordConfirm
      const goal_of_month = this.goal_of_month
      const favorite_genre = this.favorite_genre

      const payload = {
        username, password, passwordConfirm, email, goal_of_month, favorite_genre
      }
      this.$store.dispatch('signUp', payload)
    },
   
   fetchGenres(){
    this.$store.dispatch('fetchGenres')
   },
  }

}
</script>

<style>

</style>