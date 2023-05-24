<template>
  <div>
    <!-- STOPPED HERE!! : 홈에서 feelog title클릭시 feelog 상세로 넘어가는거 만들기!!!!!!!!!!!!!!!!!-->
    <FeelogCard :feelog = feelog showsUsername showsContent detailFeelog />
  </div>
</template>

<script>
import FeelogCard from "@/components/FeelogCard"

export default {
  name : 'FeelogDetailView',
  components : {
    FeelogCard
  },
 
  created(){
    const id = this.$route.params.id
    this.$store.dispatch("fetchSingleFeelog", id)
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
a{
  text-decoration: none;
} 

</style>