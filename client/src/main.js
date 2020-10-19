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
    username: "",
    password: "",
    categories_raw: [],
    stats: {},
  },
  mutations: {
    // this.$store.commit("set_user_id", user_id)
    set_user_id(state, user_id) {
      state.user_id = user_id;
    },
    // this.$store.commit("set_username_and_password",{username:username, password:password})
    set_username_and_password(state, user) {
      state.username = user.username;
      state.password = user.password;
    },
    // this.$store.commit("set_categories",categories_raw)
    set_categories(state, categories_raw) {
      state.categories_raw = categories_raw
    },
  }
})


new Vue({
  store,
  el: '#app',
  render: h => h(App)
})
