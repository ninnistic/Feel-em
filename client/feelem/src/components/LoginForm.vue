<template>
  <div class="form-group">
        <form @submit.prevent="login" class="login-form">
        <div>
        <label for="username" class="title-tag">• Username </label>
        <input type="text" v-model="userdata.username" id="username" autocomplete="id" required placeholder="Enter your username">
        </div>
        <div>
        <label for="password" class="title-tag">• Password </label>
        <input type="password" v-model="userdata.password" id="password" autocomplete="password" required placeholder="Enter your password">
        </div>  
        <button type="submit" class="login-btn">Login > </button>
        </form>
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

<style scoped>

.form-group {
  margin: 5em;
  min-height: 100vh;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.title-tag {
  font-size: 1.7em;
  font-weight: 700;
  color: #3b322c;
}

input[type="text"],
input[type="password"]{
  width: 100%;
  height: 50px;
  font-size: 1.5em;
  outline: none;
  padding-left: 20px;
  color: #627278;
  border-bottom: 1px solid #627278;
  transition: border-width 0.6s linear;
  margin-bottom: 20px;
}

input[type="text"]:focus,
input[type="password"]:focus
{
  animation-name: border-focus;
  animation-duration: 0.5s;
  animation-fill-mode: forwards;
}
@keyframes border-focus {
  from {
    border-bottom: 1px solid #627278;
  }
  to {
    border-bottom: 3px solid #f58080;
  }
}

.login-btn {
  display: block;
  font-size: 4em;
  font-weight: 600;
  color: #3b322c;
  align-self: flex-end;
  background: linear-gradient(to right, #f58080, #8ddca4);
  animation: rainbow 2s ease-in-out infinite;
  background-clip: text;
  -webkit-background-clip: text;
  transition: color 0.2s ease-in-out;
}
.login-btn:hover {
  color: rgba(0, 0, 0, 0);
}
@keyframes rainbow {
  0% {
    background-position: left;
  }
  50% {
    background-position: right;
  }
  100% {
    background-position: left;
  }
}

</style>