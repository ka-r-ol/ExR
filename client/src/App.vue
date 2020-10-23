<template>
  <div id="app">
    <div v-if="!authorized">
      <Login @clicked="onLogIn" />
    </div>
    <div v-if="authorized">
      <ExpenseGrid @clicked="onLogOut" />
    </div>
  </div>
</template>

<script>
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
    };
  },
  created() {},
  methods: {
    onLogIn(value) {
      this.authorized = true;
    },
    onLogOut(value) {
      this.authorized = false;
      this.$store.commit("set_username_and_password", {
        username: "",
        password: "",
      });
      this.$store.commit("set_statsLoad_status", false);
      this.$store.commit("set_filter", {
        cost_min: "",
        cost_max: "",
        date_before: "",
        date_after: "",
        name: "",
        category__name: "",
      });
      this.$store.commit("set_user_id", 0);
      this.$store.commit("set_categories", []);
      this.$store.commit("set_stats", {});

      this.$store.state.session_expenses = [];
      this.$store.state.message_add_danger = "";
      this.$store.state.message_add_success = "";
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