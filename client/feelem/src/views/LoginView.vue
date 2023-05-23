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
.container{

  position: relative;
  top:200px;
}
</style>