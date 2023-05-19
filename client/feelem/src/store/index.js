import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const BASE_URI = 'http://127.0.0.1:8000'
export default new Vuex.Store({
  state: {
    movies : null,
  },
  getters: {
  },
  mutations: {
    SET_MOVIES(state, res){
      state.movies = res.data

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
    }
  },
  modules: {
  }
})
