<template>
<div>
<div v-if="feelog" class="container">
<div class="profile-container image">
  <img src="@/assets/profile/OBJECTS_07.png" alt="IMG" >
  <router-link :to="'/mypage/' + feelog.username "> {{feelog.username}}</router-link>
</div>
<div class="feelog-container" style="overflow: hidden;">
<p style="font-size : 23px;	font-weight: 600;">{{movie_title.title}}</p>
<p style="font-size : 20px;	font-weight: 300;">{{feelog.title}}</p>
<i @click="like" v-if="islike" style="color:red;" class="bi bi-heart-fill"></i>
<i @click="like" v-else style="color:red;" class="bi bi-heart"></i>

<p v-if="showsContent">{{feelog.content}}</p>

</div>
</div>
  <!-- <div v-if="feelog">
    <router-link :to="'/mypage/' + feelog.username "> <p>user : {{feelog.username}}</p> </router-link>
    <p>title : {{feelog.title}}</p>
    <p v-if="showsContent">content : {{feelog.content}}</p> -->
    <!-- <p>좋아요 수 : {{feelog.likeCount}}</p> -->
  <!-- </div> -->
  </div>
</template>

<script>
export default {
  name : 'FeelogCard',
  props : {
    feelog : Object,
    showsContent: Boolean,
  },
  data(){
    return{
      islike:false
    }
  },
  computed : {
     movie_title() {
      const movie_id = this.feelog.movie
      return this.$store.state.movies.find(movie => movie.id == movie_id)
    },
  },
  methods:{
    like() {
      this.islike = !this.islike
      const id = this.$route.params.id
      this.$store.dispatch('like',id)
    }
  },

}
</script>

<style scoped>

.container{
  display: flex;
  justify-content:space-evenly;
  flex-direction: row;
  font-weight: bold;
  color: #000000; 
  background: #ffffff;
  box-shadow: 0px 0px 0px 10px #ffeaea;
  width:650px;
  border-radius: 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  min-height: 180px;
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
  
}

.profile-container{
  display: flex;
  justify-content:center;
  flex-direction: column;
  align-items: center;
  
}

.feelog-container{
  display: flex;
  justify-content:space-between;
  flex-direction: column;
  align-items:baseline;
  width:60%;
  
}

.image{
  position: relative;
  top:-25px;
  right:27px;
  width:150px;
}

.like_status{
  background-color: blue;
  color: beige;
}

a{
  text-decoration: none;
} 
</style>