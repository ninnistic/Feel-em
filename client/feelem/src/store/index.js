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
    nickname: null,
    profile: [],
    moods: [],
    isMovieSaved: false,
    genres: [],
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
    },
    isMovieSaved(state){
      return state.isMovieSaved
    }
  },
  mutations: {
    SET_PROFILE(state, res){
      state.profile = res
    },
    SET_MOVIES(state, res){
      state.movies = res.data
    },
    SAVE_TOKEN(state,token) {
      state.token = token
      router.push(`home`) 
    },
    // TODO : router store에다 쓰지 말 것...
    SET_SIGNUP() {
      router.push(`login`) 
    },
    SET_LOGIN() {
      router.push(`home`) 
    },
    SET_NICKNAME(state, nickname){
      state.nickname = nickname
    },
    SET_SINGLE_MOVIE(state, res) {
      state.movies = [res.data]
    },
    SET_FEELOGS(state, data) {
      // 전체 리뷰 가져오기
      if (Array.isArray(data)) {
        state.feelogs = data
      // 한 영화에 대한 리뷰 전체 가져오기
      } else if (typeof data === "object") {
        state.feelogs = data.feelogs
      } else {
        console.warn("Invalid feelog data")
      }
    },
    SET_SINGLE_FEELOG(state, res){
      state.feelogs = [res.data]
    },
    SET_MOODS(state, data){
      state.moods = data
    },
    SAVE_MOVIE(state){
      state.isMovieSaved = !state.isMovieSaved
    },
    SET_GENRES(state, data){
      state.genres = data
    },
  },
  actions: {
    // Consider renaming to fetchAllMovies
    fetchProfile(context,nickname){
      axios({
        method : 'get',
        url : `${BASE_URI}/accounts/${nickname}`,
        headers: authHeaders()
      })
      .then(res => {
        context.commit('SET_PROFILE', res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    fetchMovieList(context){
      axios({
        method : 'get',
        url : `${BASE_URI}/movies`,
        // headers: authHeaders()
      })
      .then(res => {
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
        headers: authHeaders()
      })
      .then(res => {
        context.commit('SET_SINGLE_MOVIE', res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    fetchFeelogList(context){
      axios({
        method : 'get',
        url : `${BASE_URI}/feelogs`,
        headers: authHeaders()
      })
      .then(res => {
        context.commit('SET_FEELOGS', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    fetchFeelogsForMovieId(context, id){
      axios({
        method : 'get',
        url : `${BASE_URI}/feelogs/by-movie/${id}/`,
        headers: authHeaders()
      })
      .then(res => {
        context.commit('SET_FEELOGS', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    fetchSingleFeelog(context, id){
      axios({
        method : 'get',
        url : `${BASE_URI}/feelogs/${id}/`,
        headers: authHeaders()
      })
      .then(res => {
        context.commit('SET_SINGLE_FEELOG', res)
      })
      .catch(err=> {
        console.log(err)
      })
    },
    fetchMoods(context){
      axios({
        method : 'get',
        url : `${BASE_URI}/feelogs/moods/`,
        headers: authHeaders()
      })
      .then(res => {
        console.log(res.data)
        context.commit('SET_MOODS', res.data)
      })
      .catch(err => {
        console.log(err)
      })
    },
    fetchGenres(context){
      axios({
        method: 'get',
        url : `${BASE_URI}/movies/all/genres`,
      })
      .then((res) => {
        context.commit('SET_GENRES', res.data)
      
      })
      .catch(err => {
        console.log(err)
      })
    },
    createFeelog(context, newFeelog){
      const id = newFeelog.id
      const title = newFeelog.title
      const content = newFeelog.content
      const mood = newFeelog.mood
      axios({
        method : 'post',
        url : `${BASE_URI}/feelogs/by-movie/${id}/`,
        headers : authHeaders(),
        data : {
          title, content, mood
        }
      })
      .then(() => {
        console.log(context)
      })
      .catch(err => {
        console.log(err)

      })
    },
    checkForLogin(context) {
      const nickname = localStorage.getItem("nickname")
      // jwt는 store에 저장되어있어야 한다. localStorage가 아니라 
      const jwt = localStorage.getItem("jwt")

      if (nickname === null || jwt === null)
        // not logged in; nothing to do
        return

      console.debug(`User is logged in as ${nickname}`)
      context.commit('SET_NICKNAME', nickname)
    },
    login(context, payload){
      // 이름을 통일해야할 필요가 있다 -> 헷갈림 username이거나 nickname이거나  
      const nickname = payload.username
      const password = payload.password
        axios({
          method: "POST", 
          url: "http://127.0.0.1:8000/api/token/",
          data: {
            username: nickname, password
          },
          headers: authHeaders()
        })
        .then((response) => {
          context.commit('SET_NICKNAME', nickname)
          localStorage.setItem("jwt", response.data.access)
          localStorage.setItem("nickname", nickname)

          //this.$emit('login')
          // 로그인 성공하면, todo list로 이동하기
          context.commit('SET_LOGIN')
  
        })
        .catch((error) => {
          console.log(error)
        })
      },
    signUp(context, payload){
      const username = payload.username
      const email = payload.email
      const password = payload.password
      const passwordConfirm = payload.passwordConfirm
      const favorite_genre = payload.favorite_genre
      const goal_of_month = payload.goal_of_month

      axios({
        method:'post',
        url:`${BASE_URI}/accounts/signup`,
        data:{
          username, password, passwordConfirm, email, favorite_genre, goal_of_month
        }
      })
      .then(() =>{
        console.log(favorite_genre)
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
    follow(context, nickname){
      axios({
        method:'post',
        url:`${BASE_URI}/accounts/${nickname}/follow`,
        headers: authHeaders()
      })
      .then(() =>{
        console.log('팔로우')
      })  
      .catch((err) => {
        console.log(err)
        
      }) 
    },
    like(context, id){
      axios({
        method:'post',
        url:`${BASE_URI}/feelogs/${id}/like/`,
        headers: authHeaders()
      })
      .then(() =>{
        console.log('like')
      })  
      .catch((err) => {
        console.log(err)
        
      }) 
    },
    saveMovie(context, id){
      axios({
        method:'post',
        url:`${BASE_URI}/movies/${id}/save-movie/`,
        headers: authHeaders()
      })
      .then((res) =>{
        console.log('save', res.data)
        context.commit('SAVE_MOVIE')
      })  
      .catch((err) => {
        console.log(err)
        
      }) 
    }

  },
  modules: {
  },

})

function authHeaders() {
  const token = localStorage.getItem("jwt")
  return {
    Authorization: "Bearer " + token
  }
}
