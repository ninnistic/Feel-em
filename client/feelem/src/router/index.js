import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '@/views/SignupView'
import HomeView from '@/views/HomeView'

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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
