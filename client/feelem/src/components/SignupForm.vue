<template>
  <div>
    <form @submit.prevent="signup">
    <label for="username" >username : </label>
    <input type="text" v-model="username" id="username">
    <label for="email">email : </label>
    <input type="text" v-model="email" id="email">
    <label for="passowrd">password : </label>
    <input type="password" v-model="passowrd" id="password">
    <label for="passowrd2">password check : </label>
    <input type="password" v-model="password2" id="password2">   
    <button>어쩌라고</button>
    </form>
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
      password2 : null,
    }
  },
  methods : {
    singup(){
      const username = this.username
      const email = this.email
      const password = this.password
      const password2 = this.password2
    
      const payload = {
        username, email, password, password2
      }

      this.$store.dispatch('signup', payload)
    }
  }

}
</script>

<style>

</style>