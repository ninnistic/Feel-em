<template>
  <div v-if="feelog">
    <router-link :to="'/mypage/' + feelog.username "> <p>user : {{feelog.username}}</p> </router-link>
    <p>title : {{feelog.title}}</p>
    <p v-if="showsContent">content : {{feelog.content}}</p>
    <p>좋아요 수 : {{feelog.like_users_count}}</p>
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