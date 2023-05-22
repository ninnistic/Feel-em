<template>
  <div>
    <FeelogCard :feelog = feelog />
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

</style>