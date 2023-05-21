<template>
  <div>
    <p>title : {{feelog.title}}</p>
    <p>content : {{feelog.content}}</p>
  </div>
</template>

<script>
export default {
  name : 'FeelogCard',
  props : {
    feelog : Object,
  }

}
</script>

<style>

</style>