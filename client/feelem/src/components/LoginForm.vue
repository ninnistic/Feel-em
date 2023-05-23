<template>
  <div class="card">
    <div class="card-body">
      <div class="form-group">
        <form @submit.prevent="login">
        <div>
        <label for="username">username : </label>
        <input type="text" v-model="userdata.username" id="username" autocomplete="id">
        </div>
        <div>
        <label for="password">password : </label>
        <input type="password" v-model="userdata.password" id="password" autocomplete="password">
        </div>  
        <button type="submit">로그인하세용</button>
        </form>
    </div>
    </div>
  </div>
</template>

<script>

export default {
  // signupform이 아님 
  name : 'LoginForm',
  data() {
    return {
      userdata:{
        username: null,
        password : null,
    }}

  },
  methods : {
    login(){
      const payload = this.userdata
      this.$store.dispatch('login', payload)
    }
  }

}
</script>

<style>

</style>