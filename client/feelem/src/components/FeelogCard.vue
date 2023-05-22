<template>
  <div v-if="feelog">
    <router-link :to="'/mypage/' + feelog.username "> <p>user : {{feelog.username}}</p> </router-link>
    <p>title : {{feelog.title}}</p>
    <p v-if="showsContent">content : {{feelog.content}}</p>
  </div>
</template>

<script>
export default {
  name : 'FeelogCard',
  props : {
    feelog : Object,
    showsContent: Boolean,
   
  }

}
</script>

<style>

</style>