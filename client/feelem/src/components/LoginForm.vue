<template>
  <div class="card">
    <div class="card-body">
      <div class="form-group">
        <form @submit.prevent="login">
        <div>
        <label for="email">email : </label>
        <input type="text" v-model="email" id="email">
        </div>
        <div>
        <label for="password">password : </label>
        <input type="password" v-model="passowrd" id="password">
        </div>  
        <button type="submit">로그인하세용</button>
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
      email: null,
      password : null,
    }
  },
  methods : {
    singup(){
      const email = this.email
      const password = this.password
    
      const payload = {
       email, password
      }

      this.$store.dispatch('login', payload)
    }
  }

}
</script>

<style>

</style>