import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)
const BASE_URI = 'http://127.0.0.1:8000'
export default new Vuex.Store({
  state: {
    movies : null,
    movie : null,
  },
  getters: {
    
  },
  mutations: {
    SET_MOVIES(state, res){
      state.movies = res.data
    },
    SET_MOVIE_DETAIL(state, res){
      state.movie = res.data
    },
    SAVE_TOKEN(state,token) {
      state.token = token
      router.push(`home`) 
    },
    SET_SIGNUP() {
      router.push(`login`) 
    }
  },
  actions: {
    getMovieList(context){
      axios({
        method : 'get',
        url : `${BASE_URI}/movies`
      })
      .then(res => {
        console.log(res)
        context.commit('SET_MOVIES', res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getMovieDetail(context, id){
      axios({
        method : 'get',
        url : `${BASE_URI}/movies/${id}`,
      })
      .then(res => {
        console.log(res)
        context.commit('SET_MOVIE_DETAIL', res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    getFeelogDetail(context, id){
      axios({
        method : 'get',
        url : `${BASE_URI}/feelogs/${id}`
      })
      .then(res => {
        console.log(context, res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    signup(context, payload){
      const username = payload.username
      const email = payload.email
      const password = payload.password
      const passwordConfirm = payload.passwordConfirm
      const favorite_genre = [payload.favorite_genre]
      const goal_of_month = payload.goal_of_month

      axios({
        method:'post',
        url:`${BASE_URI}/accounts/signup`,
        data:{
         username, password,passwordConfirm, email, favorite_genre, goal_of_month
        }
      })
      .then(() =>{
        context.commit('SET_SIGNUP')
      })  
       .catch((err) => {
        console.log(err)
        console.log(payload)
      }) 
    }
  },
  modules: {
  }
})
