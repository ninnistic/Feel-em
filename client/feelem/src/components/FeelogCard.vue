<template>
<div>

<div v-if="homeFeelog" class="container">  
<div class="profile-container image">
  <img src="/profile/profile1.png" alt="IMG" >
  <router-link :to="'/account/' + feelog.username" class="home-a"> {{feelog.username}}</router-link>
</div>
<div class="feelog-container" style="overflow: hidden;">
<p style="font-size : 23px;	font-weight: 600;" class="home-title">{{movie_title.title}}</p>
<p style="font-size : 20px;	font-weight: 300;" >{{feelog.title}}</p>
<i @click="like" v-if="islike" style="color:red;" class="bi bi-heart-fill"></i>
<i @click="like" v-else style="color:red;" class="bi bi-heart"></i>

<p v-if="showsContent">{{feelog.content}}</p>
</div>
</div>

<div v-if="detailFeelog" class="form-group">
<div class="user-card">
  <img src="/profile/profile1.png" alt="IMG" >
<router-link :to="'/account/' + feelog.username" class="detail-a"><div class="card-user-name">{{feelog.username}}</div></router-link>
</div>
<div class="card-info">
<p class="card-title">"{{feelog.title}}"</p>
<p class="card-content">{{feelog.content}}</p>
<p class="card-date">{{feelog.created_at}}</p>

<i @click="like" v-if="islike" style="color:#f58080;" class="bi bi-heart-fill like-heart"></i>
<i @click="like" v-else style="color:#f58080;" class="bi bi-heart like-heart"></i>
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

.card-content{
  color: #627278;
  font-weight: 500;
  overflow: hidden;
}
.home-a{
  font-size: 20px;
  font-weight: 500;
  color: #1d2b30;
  transition: 0.1s;
}

.home-a:hover{
  background-color:  #627278;
  color: #ffeaea;
  padding: 0px 10px;
  border-radius : 10px;
}
.home-title{
  transition: 0.2s;
}

.home-title:hover{
  background-color: #f58080;
  padding: 0px 10px;
  border-radius : 10px;
}
.detail-a{
  color : #3b322c;
  font-weight: 500;
  background-color: #ffeaea;
  margin-top: 5px;
  border-radius: 20px;
}
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
  background-color: #a2ccae;
  padding: 30px;
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
  color : #ffeaea;
}

.card-date{
  margin-top: 30px;
  font-weight: 500;
  font-size: 0.8em;
  color: #627278;
}

.like-heart{
  padding-left: 80rem;
}
</style>