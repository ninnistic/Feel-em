<template>
  <div>
    <button @click="like" :class="{ like_status : islike}">좋아요</button>
    <!-- STOPPED HERE!! : 홈에서 feelog title클릭시 feelog 상세로 넘어가는거 만들기!!!!!!!!!!!!!!!!!-->
    <FeelogCard :feelog = feelog showsUsername/>
  </div>
</template>

<script>
import FeelogCard from "@/components/FeelogCard"

export default {
  name : 'FeelogDetailView',
  components : {
    FeelogCard
  },
  data(){
    return{
      islike:false
    }
  },
  created(){
    const id = this.$route.params.id
    this.$store.dispatch("fetchSingleFeelog", id)
  },
  methods:{
    like() {
      this.islike = !this.islike
      const id = this.$route.params.id
      this.$store.dispatch('like',id)
    }
  },
  computed : {
     feelog() {
      const id = this.$route.params.id
      return this.$store.state.feelogs.find(feelog => feelog.id == id)
    },
  }

}
</script>

<style>

.like_status{
  background-color: blue;
  color: beige;
}
</style>