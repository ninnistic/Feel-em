import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vuetify from './plugins/vuetify'
// Buefy
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
// BootstrapVue
import 'bootstrap';
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { CarouselPlugin } from 'bootstrap-vue'
// axios
import axios from 'axios'
import VModal from 'vue-js-modal'

Vue.prototype.$http = axios

Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(CarouselPlugin)
Vue.use(Buefy)
Vue.use(VModal, { dynamic: true })

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
