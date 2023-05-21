<template>
  <div class="card">
    <div class="card-body">
      <div class="form-group">
        <form @submit.prevent="login">
        <div>
        <label for="username">username : </label>
        <input type="text" v-model="userdata.username" id="username">
        </div>
        <div>
        <label for="password">password : </label>
        <input type="password" v-model="userdata.password" id="password">
        </div>  
        <button type="submit">로그인하세용</button>
        </form>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'SignupForm',
  data() {
    return {
      userdata:{
        username: null,
        password : null,
    }}

  },
  methods : {
    login(){
      axios({
        method: "POST", 
        url: "http://127.0.0.1:8000/api/token/",
        data: this.userdata  
      })
      .then((response) => {
        // console.log(response)
        localStorage.setItem("jwt", response.data.access)
        this.$emit('login')
        
        // 로그인 성공하면, todo list로 이동하기
        this.$router.push(`home`)

      })
      .catch((error) => {
        console.log(error)
      })
    }
  }

}
</script>

<style>

</style>