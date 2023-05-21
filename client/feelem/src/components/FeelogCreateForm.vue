<template>
<div class="card">
  <form class="card-body" @submit.prevent="create">
    <textarea v-model="feelog.content" placeholder="How was this shit?"></textarea>
    <select v-model="feelog.mood">
      <option value="1">Happy</option>
      <option value="2">Sad</option>
      <option value="3">Angry</option>
      <option value="4">Inspiring</option>
      <option value="5">Moody</option>
      <option value="6">Lethargic</option>
      <option value="7">Energetic</option>
    </select>
    <input type="submit" value="Post" />
  </form>
  </div>
</template>

<script>
export default {
  name : 'FeelogCreateForm',
  data() {
    return {
      feelog: {
        mood: null,
        content: null
      }
    }
  },
  props : {
  
  },
  methods: {
    create() {
      console.log(this.feelog)
    }
  },
}
</script>

<style>

</style>