import Vue from 'vue'
import VueRouter from 'vue-router'
// import SignupView from '@/views/SignupView'
// import HomeView from '@/views/HomeView'
// import LoginView from '@/views/LoginView'
// import MovieListView from '@/views/MovieListView'
// import MovieDetailView from '@/views/MovieDetailView'
// import FeelogDetailView from '@/views/FeelogDetailView'
// import MyPageView from '@/views/MyPageView'

Vue.use(VueRouter)

const routes = [
  {
    path : '/',
    redirect: '/home'
  },
  {
    path : '/home',
    component : () => import('@/views/HomeView.vue')
  },
  {
    path: '/signup',
    component: () => import('@/views/SignupView.vue')
  },
  {
    path : '/login',
    component : () => import('@/views/LoginView.vue')
  },
  {
    path : '/movielist',
    component : () => import('@/views/MovieListView.vue')
  },
  {
    path : '/movie-detail',
    component : () => import('@/views/MovieDetailView.vue')
  },
  {
    path : '/feelog-detail',
    component : () => import('@/views/FeelogDetailView.vue')
  },
  {
    path : '/mypage',
    component : () => import('@/views/MyPageView.vue')
  },
  {
    path : '*',
    component : () => import('@/views/NotFoundPage.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
