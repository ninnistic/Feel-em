import Vue from 'vue'
import VueRouter from 'vue-router'


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
    path : '/movie-detail/:id',
    component : () => import('@/views/MovieDetailView.vue')
  },
  {
    path : '/feelog-detail/:id',
    component : () => import('@/views/FeelogDetailView.vue')
  },
  {
    path : '/account/:nickname',
    component : () => import('@/views/AccountView.vue')
  },
  {
    path : '*',
    component : () => import('@/views/NotFoundPage.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  scrollBehavior() { 
    return { x: 0, y: 0 }
  },
  base: process.env.BASE_URL,
  routes
})

export default router
