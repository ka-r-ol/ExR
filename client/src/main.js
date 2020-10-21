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

//Vue.prototype.$BASE_API_URL = "http://127.0.0.1:8000/api/v1/";

const store = new Vuex.Store({
  state: {
    BASE_API_URL: "http://127.0.0.1:8000/api/v1/",
    user_id: 0,
    username: "",
    password: "",
    categories_raw: [],
    session_expenses: [],
    stats: {},
    message_add_danger: "",
    message_add_success: "",
    paramFilter: {
      cost_min: "",
      cost_max: "",
      date_before: "",
      date_after: "",
      name: "",
      category__name: "",
    }
  },
  getters: {
    get_message_add_danger: state => { return state.message_add_danger },
    get_message_add_success: state => { return state.message_add_success },
    get_filter_url_suffix: state => {
      var url = "";
      if (state.paramFilter.cost_min != "") {
        url += "&cost_min=" + state.paramFilter.cost_min;
      }
      if (state.paramFilter.cost_max != "") {
        url += "&cost_max=" + state.paramFilter.cost_max;
      }
      // date_after=2020-09-25&date_before=2020-09-28&name=e&
      if (state.paramFilter.date_before != "") {
        url +=
          "&date_before=" + state.paramFilter.date_before;
      }
      if (state.paramFilter.date_after != "") {
        url +=
          "&date_after=" + state.paramFilter.date_after;
      }
      if (state.paramFilter.name != "") {
        url += "&name=" + state.paramFilter.name;
      }
      if (state.paramFilter.category__name != "") {
        url +=
          "&category__name=" + state.paramFilter.category__name;
      }

      return url;
    },
    stats: state => { return state.stats },
    username: state => { return state.username },
    password: state => { return state.password },
    session_expenses: state => { return state.session_expenses },
    nb_session_expenses: state => { return state.session_expenses.length }
  },
  mutations: {
    // this.$store.commit("register_patch_session_expense", expense)
    register_patch_session_expense(state, expense) {
      expense.action = "Update";
      expense.timestamp = (new Date()).toLocaleString();
      state.session_expenses.push(expense);
    },
    // this.$store.commit("register_add_session_expense", expense)
    register_add_session_expense(state, expense) {
      expense.action = "Add";
      expense.timestamp = (new Date()).toLocaleString();
      state.session_expenses.push(expense);
    },
    register_delete_session_expense(state, expense) {
      expense.action = "Delete";
      expense.timestamp = (new Date()).toLocaleString();
      state.session_expenses.push(expense);
      console.log("DELETE", getter.nb_session_expenses, state.session_expenses);
    },
    // this.$store.commit("set_filter", Filter)
    set_filter(state, Filter) {
      for (var i in Filter) {
        state.paramFilter[i] = Filter[i];
      }
    },
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
    set_stats(state, stats) {
      state.stats = stats;
    }
  },
  actions: {
    loadStats({ commit, state, getters }) {
      // https://dev.to/ljnce/how-to-call-api-from-axios-in-vuex-store-2m3g
      console.log("PASS&USER", state.username, state.password)
      let url = state.BASE_API_URL + "stats";
      if (getters.get_filter_url_suffix != "") {
        url += "?" + getters.get_filter_url_suffix.slice(1);
      }
      axios
        .get(url, {
          auth: {
            username: state.username,
            password: state.password,
          }
        })
        .then(res => res.data)
        .then(stats => {
          console.log(stats);
          commit('set_stats', stats)
        })
    }
  },
})


new Vue({
  store,
  el: '#app',
  render: h => h(App)
})
