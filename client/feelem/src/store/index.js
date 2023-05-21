import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)
const BASE_URI = 'http://127.0.0.1:8000'
export default new Vuex.Store({
  state: {
    movies: [],
    feelogs: [],
    nickname: null
  },
  getters: {
    getRecommendedMovies(state) {
      // For now, just return the first five movies.
      // TODO: actually get reccomendations for the current user
      return state.movies.slice(0, 5);
    },
    getRecommendedFeelogs(state){
      return state.feelogs.slice(0, 5);
    },
    isSignedIn(state) {
      return state.nickname != null
    }
  },
  mutations: {
    SET_MOVIES(state, res){
      state.movies = res.data
    },
    SAVE_TOKEN(state,token) {
      state.token = token
      router.push(`home`) 
    },
    SET_SIGNUP() {
      router.push(`login`) 
    },
    SET_NICKNAME(state, nickname){
      state.nickname = nickname
    },
    SET_SINGLE_MOVIE(state, res) {
      state.movies = [res.data]
    },
    SET_FEELOGS(state, res){
      state.feelogs = res.data
    },
    SET_SINGLE_FEELOGS(state, res){
      state.feelogs = [res.data]
    }
  },
  actions: {
    // Consider renaming to fetchAllMovies
    fetchMovieList(context){
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
    fetchSingleMovie(context, id){
      axios({
        method : 'get',
        url : `${BASE_URI}/movies/${id}`,
      })
      .then(res => {
        console.log(res)
        context.commit('SET_SINGLE_MOVIE', res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    fetchFeelogList(context){
      axios({
        method : 'get',
        url : `${BASE_URI}/feelogs`
      })
      .then(res => {
        console.log(context,res)
        context.commit('SET_FEELOGS', res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    fetchFeelogDetail(context, id){
      axios({
        method : 'get',
        url : `${BASE_URI}/feelogs/${id}/`
      })
      .then(res => {
        context.commit('SET_SINGLE_FEELOG', res)
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
    },
    signOut(context) {
      localStorage.removeItem('jwt')
      localStorage.removeItem('nickname')
      context.commit('SET_NICKNAME', null)
    },
    setusername(context, nickname){
      context.commit('SET_NICKNAME', nickname)
    }

  },
  modules: {
  },

})
