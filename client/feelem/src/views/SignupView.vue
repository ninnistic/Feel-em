<template>
  <div>
    <SignupForm />
    <button @click="testAxios">testAxios</button>
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
  methods : {
    testAxios() {
      const baseURI = 'http://127.0.0.1:8000';
      this.$http.get(`${baseURI}/movies/`)
      .then((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }

}
</script>

<style>

</style>