<template>
  <div class="card">
    <div class="card-body">
      <div class="form-group">
        <form @submit.prevent="signup">
        <div>
        <label for="username" >username : </label>
        <input type="text" v-model="username" id="username">
        </div>
        <div>
        <label for="email">email : </label>
        <input type="text" v-model="email" id="email">
        </div>
        <div>
        <label for="password">password : </label>
        <input type="password" v-model="password" id="password">
        </div>
        <div>
        <label for="passwordConfirm">password check : </label>
        <input type="password" v-model="passwordConfirm" id="passwordConfirm">
        </div>
        <div>
        <label for="favorite_genre">장르 선택 : </label>
        <input type="text" v-model="favorite_genre" id="favorite_genre">
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
        goal_of_month:null,
        favorite_genre: null,      
    }
  },
  methods : {
    signup() {
      const username = this.username
      const email = this.email
      const password = this.password
      const passwordConfirm = this.passwordConfirm
      const goal_of_month = this.goal_of_month
      const favorite_genre = this.favorite_genre

      const payload = {
        username, password, passwordConfirm, email, goal_of_month, favorite_genre
      }
      this.$store.dispatch('signup', payload)
    }
  }

}
</script>

<style>

</style>