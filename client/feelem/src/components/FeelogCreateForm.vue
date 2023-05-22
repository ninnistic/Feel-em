<template>
<div class="card" v-if="moods">
  <form class="card-body" @submit.prevent="create">
    <div>
    <input type="text" placeholder="한줄 감상평을 작성하세요" v-model="feelog.title">
    </div>
    <div>
    <textarea v-model="feelog.content" placeholder="더 자세히 작성하세요"></textarea>
    </div>
    <div> Mood : 
    <select>
      <option value="mood.title" v-for="mood in moods" :key="mood.id" >{{mood.title}}</option>
    </select>
    </div>
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
        title : null,
        mood: null,
        content: null
      }
    }
  },
  props : {

  },
  created() {
    this.$store.dispatch('fetchMoods')
  },

  methods: {
  
  },
  computed: {
    moods(){
      return this.$store.state.moods
    }
  }
}
</script>

<style>

</style>