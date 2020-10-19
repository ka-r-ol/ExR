<template>
  <div id="app">
    <div v-if="!authorized">
      <Login @clicked="onLogIn" />
    </div>
    <div v-if="authorized">
      <ExpenseGrid @clicked="onLogOut" :categories="categories" />
    </div>
  </div>
</template>

<script>
//import { BASE_API_URL } from "./settings";
import Login from "./components/Login.vue";
import ExpenseGrid from "./components/ExpenseGrid.vue";
import axios from "axios";

export default {
  name: "app",
  components: {
    Login,
    ExpenseGrid,
  },
  data() {
    return {
      authorized: false,
      categories: {},
    };
  },
  created() {},
  methods: {
    onLogIn(value) {
      this.authorized = true;
      this.categories = value.categories;
    },
    onLogOut(value) {
      this.authorized = false;
      this.$store.commit("set_username_and_password", {
        username: "",
        password: "",
      });
    },
  },
};
</script>

<style>
[v-cloak] {
  display: none;
}
#welcome {
  text-align: right;
  text-transform: capitalize;
}
</style>