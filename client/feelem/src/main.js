import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import vuetify from './plugins/vuetify'
// Buefy
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
// BootstrapVue
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VModal from 'vue-js-modal';


Vue.config.productionTip = false

Vue.use(BootstrapVue)
Vue.use(Buefy)
Vue.use(VModal)

new Vue({
  store,
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')