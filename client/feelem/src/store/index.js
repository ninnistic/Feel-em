import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const BASE_URI = 'http://127.0.0.1:8000'
export default new Vuex.Store({
  state: {
    movies : [],
    feelogs : [],
  },
  getters: {
    getRecommendedMovies(state) {
      // For now, just return the first five movies.
      // TODO: actually get reccomendations for the current user
      return state.movies.slice(0, 5);
    },
    getRecommendedFeelogs(state){
      return state.feelogs.slice(0, 5);
    }
  },
  mutations: {
    SET_MOVIES(state, res) {
      state.movies = res.data
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
    //,
    // SET_MOVIE_DETAIL(state, res){
    //   state.movie = res.data
    // }
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
    }
  },
  modules: {
  }
})
