<template>
  <div class="container">
    <SignupForm />
  </div>
</template>

<script>
import SignupForm from '@/components/SignupForm.vue'

export default {
  name : 'SignupView',
  components : {
    SignupForm,
  },
  data() {
    return {
      
    }
  },


}
</script>

<style scoped>
/* .container{
  position: relative;
  top:200px;
} */
</style>