<template>
  <div>
    <!-- STOPPED HERE!! : 홈에서 feelog title클릭시 feelog 상세로 넘어가는거 만들기!!!!!!!!!!!!!!!!!-->
    <FeelogCard />
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
  }

}
</script>

<style>

</style>