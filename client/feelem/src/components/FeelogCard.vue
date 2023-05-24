<template>
<div>

<div v-if="homeFeelog" class="container">  
<div class="profile-container image">
  <img src="/profile/profile1.png" alt="IMG" >
  <router-link :to="'/account/' + feelog.username "> {{feelog.username}}</router-link>
</div>
<div class="feelog-container" style="overflow: hidden;">
<p style="font-size : 23px;	font-weight: 600;">{{movie_title.title}}</p>
<p style="font-size : 20px;	font-weight: 300;">{{feelog.title}}</p>
<i @click="like" v-if="islike" style="color:red;" class="bi bi-heart-fill"></i>
<i @click="like" v-else style="color:red;" class="bi bi-heart"></i>

<p v-if="showsContent">{{feelog.content}}</p>
</div>
</div>

<div v-if="detailFeelog" class="form-group">
<div class="user-card">
  <img src="/profile/profile1.png" alt="IMG" >
<router-link :to="'/account/' + feelog.username "><div class="card-user-name">{{feelog.username}}</div></router-link>
</div>
<div class="card-info">
<p class="card-title">"{{feelog.title}}"</p>
<p class="card-date">{{feelog.created_at}}</p>
<i @click="like" v-if="islike" style="color:red;" class="bi bi-heart-fill like-heart"></i>
<i @click="like" v-else style="color:red;" class="bi bi-heart like-heart"></i>
</div>
</div>
</div>

</template>

<script>
export default {
  name : 'FeelogCard',
  props : {
    feelog : Object,
    showsContent: Boolean,
    account:Boolean,
    homeFeelog: Boolean,
    detailFeelog: Boolean,
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
.card-info {
  font-size: 1.5em;
}

.user-card{
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.form-group{
  padding-top: 3rem;
  margin: 3em 10em;
  display: flex;
  gap : 30px;
  border-top : 1px solid black;
}

.card-user-name{
  font-size: 20px;
}

.account-container{
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
  align-items: center;
}
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
  align-items: center;
}

.profile-container{
  display: flex;
  justify-content:center;
  flex-direction: column;
  align-items: center;
  
}

.feelog-container{
  display: flex;
  /* justify-content:space-between; */
  flex-direction: column;
  align-items:baseline;
  width:60%;
  
}

.feelog-container-account{
  display: flex;
  /* justify-content:space-between; */
  flex-direction: column;
  align-items:center;
  justify-content: center;
  width:100px;
  
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
  text-align: center;
}

.card-title {
  font-weight: 900;
  padding: 20px 0px;
  font-size: 1.2em;
}

.card-date{
  font-weight: 300;
  font-size: 0.8em;
  color: #627278;
}

.like-heart{
  padding-left: 90rem;
}
</style>