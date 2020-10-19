import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue) // Install Boot strapVue
Vue.use(IconsPlugin) // Optionally install the BootstrapVue icon components plugin
Vue.use(Vuex)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from "axios";

Vue.prototype.$BASE_API_URL = "http://127.0.0.1:8000/api/v1/";

const store = new Vuex.Store({
  state: {
    user_id: 0,
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++
    }
  }
})


new Vue({
  store,
  el: '#app',
  render: h => h(App)
})
