<template>
<div class="card" v-if="moods">
  <form class="card-body" @submit.prevent="createFeelog">
    <div>
    <input type="text" placeholder="한줄 감상평을 작성하세요" v-model="feelog.title">
    </div>
    <div>
    <textarea v-model="feelog.content" placeholder="더 자세히 작성하세요"></textarea>
    </div>
    <div> Mood : 
    <select v-model="feelog.mood">
      <!--option에서 value를 동적으로 연결해주면서 mood.id를 보내는걸 잊지 말자! -->
      <option :value="mood.id" v-for="mood in moods" :key="mood.id" >{{mood.title}}</option>
    </select>
    </div>
    <input type="submit" value="Post" @click="$router.go()"/>
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
    movie_id : Number,
  },
  created() {
    this.$store.dispatch('fetchMoods')
  },

  methods: {
    createFeelog(){
      const movie_id = parseInt(this.movie_id)
      const newFeelog = {
        id : movie_id,
        title : this.feelog.title,
        mood : this.feelog.mood,
        content : this.feelog.content
      }
      this.$store.dispatch('createFeelog', newFeelog)
    }
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