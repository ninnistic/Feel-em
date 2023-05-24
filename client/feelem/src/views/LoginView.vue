<template>
  <div class="container">
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm'
export default {
  name : 'LoginView',
  components : {
    LoginForm,
  },
  data() {
    return {
      
    }
  }

}
</script>

<style scoped>
*{
  background-color: #f4f3ee;
}
/* .container{
  height: 100vh;
  position: relative;
  top:200px;
} */
</style>