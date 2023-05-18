import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '@/views/SignupView'
import HomeView from '@/views/HomeView'
import LoginView from '@/views/LoginView'
import MovieListView from '@/views/MovieListView'
import MovieDetailView from '@/views/MovieDetailView'
import FeelogDetailView from '@/views/FeelogDetailView'
import MyPageView from '@/views/MyPageView'

Vue.use(VueRouter)

const routes = [
  {
    path : '/',
    name : 'HomeView',
    component : HomeView

  },
  {
    path: '/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path : '/login',
    name : 'LoginView',
    component : LoginView
  },
  {
    path : '/movielist',
    name : 'MovieListView',
    component : MovieListView,
  },
  {
    path : '/movie-detail',
    name : 'MovieDetailView',
    component : MovieDetailView,
  },
  {
    path : '/feelog-detail',
    name : 'FeelogDetailView',
    component : FeelogDetailView,
  },
  {
    path : '/mypage',
    name : 'MyPageView',
    component : MyPageView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
