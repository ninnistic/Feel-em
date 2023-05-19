import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

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
      state.movie = res
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
    }
  },
  modules: {
  }
})
