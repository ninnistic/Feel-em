<template>
  <div v-if="feelog">
    <p>title : {{feelog.title}}</p>
    <router-link :to="'mypage/' + feelog.username "> <p>user : {{feelog.username}}</p> </router-link>
    <p v-if="showsContent">content : {{feelog.content}}</p>
  </div>
</template>

<script>
export default {
  name : 'FeelogCard',
  props : {
    feelog : Object,
    showsContent: Boolean,
    showsUsername : Boolean
  }

}
</script>

<style>

</style>