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
        <label for="passowrd">password : </label>
        <input type="password" v-model="password" id="password">\
        </div>
        <div>
        <label for="passowrd2">password check : </label>
        <input type="password" v-model="password2" id="password2">
        </div>   
        <button type="submit">회원가입하쉐이</button>
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