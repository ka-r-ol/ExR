<template>
  <div id="app">
    <div v-if="!authorized">
      <Login @clicked="onAuthorized" :loginmsg="loginmsg" />
    </div>
    <div v-if="authorized">
      <p id="welcome">Witaj, {{ username }}</p>
    </div>
  </div>
</template>

<script>
const BASE_URL = "http://127.0.0.1:8000/api/v1/";
import Login from "./components/Login.vue";
import axios from "axios";

export default {
  name: "app",
  components: {
    Login,
  },
  data() {
    return {
      authorized: false,

      username: "",
      password: "",
      loginmsg: "", // message displayed in case of login failure

      expenses: [],
      expenses_next: "",
      expenses_previous: "",

      categories: [],
    };
  },
  created() {},
  methods: {
    onAuthorized(value) {
      this.authorized = true;
      this.username = value.username;
      this.password = value.password;
      this.fetchExpenses();
    },

    fetchExpenses: function () {
      var url = BASE_URL + "expenses";
      axios
        .get(url, {
          auth: {
            username: this.username,
            password: this.password,
          },
        })
        .then((res) => {
          this.expenses = res.data.results;
          this.expenses_next = res.data.next;
          this.expenses_previous = res.data.previous;
          console.log(
            "Expenses",
            this.expenses,
            this.expenses_next,
            this.expenses_previous
          );
        })
        .catch((error) => {
          this.authorized = false;
          this.loginmsg = "Access denied. " + error;
          console.log(error); //Logs a string: Error: Request failed with status code 404
        });

      //  fetch categories

      var url = BASE_URL + "categories";
      axios
        .get(url, {
          auth: {
            username: this.username,
            password: this.password,
          },
        })
        .then((res) => {
          this.categories = res.data;
          console.log("Categories", this.categories);
        })
        .catch((error) => {
          this.authorized = false;
          this.loginmsg = "Access denied. " + error;
          console.log(error); //Logs a string: Error: Request failed with status code 404
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