import Vue from 'vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue) // Install BootstrapVue
Vue.use(IconsPlugin) // Optionally install the BootstrapVue icon components plugin

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import axios from "axios";

Vue.prototype.$BASE_API_URL = "http://127.0.0.1:8000/api/v1/";

/*
Vue.prototype.$LoadCategories = function (username, password) {
  var categories = {}
  axios.get(this.$BASE_API_URL + "categories", {
    auth: {
      username: this.username,
      password: this.password,
    },
  }).then((res) => {
    res.data.forEach((el) => (categories[el.id] = el.name));
  });
  return categories;;
}
*/
new Vue({
  el: '#app',
  render: h => h(App)
})
