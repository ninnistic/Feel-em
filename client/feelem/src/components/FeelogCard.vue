<template>
  <div v-if="feelog">
    <p>title : {{feelog.title}}</p>
    <p v-if="showsContent">content : {{feelog.content}}</p>
  </div>
</template>

<script>
export default {
  name : 'FeelogCard',
  props : {
    feelog : Object,
    showsContent: Boolean
  }

}
</script>

<style>

</style>