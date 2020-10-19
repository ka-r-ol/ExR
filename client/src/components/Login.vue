<template>
  <div>
    <form>
      <h3>Sign In</h3>

      <div class="form-group">
        <label>Username</label>
        <input
          v-model="username"
          placeholder="username"
          class="form-control form-control-lg"
        />
        <!-- <input type="text" class="form-control form-control-lg" /> -->
      </div>

      <div class="form-group">
        <label>Password</label>
        <input
          v-model="password"
          :type="'password'"
          placeholder="password"
          class="form-control form-control-lg"
        />
        <!--<input type="password" class="form-control form-control-lg" /> -->
      </div>
      <button
        type="submit"
        @click="process"
        class="btn btn-dark btn-lg btn-block"
      >
        Sign In
      </button>
    </form>
    <br />
    <p class="text-danger">{{ loginmsg }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  //props: [],
  data: function () {
    return {
      username: "",
      password: "",
      loginmsg: "",
    };
  },

  methods: {
    process: function () {
      event.preventDefault();

      var categories = {};
      var categories_raw = [];

      var url = this.$BASE_API_URL + "me";
      axios
        .get(url, {
          auth: {
            username: this.username,
            password: this.password,
          },
        })
        .then((res) => {
          this.$store.state.user_id = res.data.id;
          console.log("USER_ID LOGIN", this.$store.state.user_id);
        })
        .catch((error) => {
          this.loginmsg = "Access denied. " + error;
        });

      url = this.$BASE_API_URL + "categories";

      axios
        .get(url, {
          auth: {
            username: this.username,
            password: this.password,
          },
        })
        .then((res) => {
          categories_raw = res.data;
          res.data.forEach((el) => (categories[el.id] = el.name));
          this.$store.state.count = 3;
          this.$emit("clicked", {
            username: this.username,
            password: this.password,
            categories: categories,
            categories_raw: categories_raw,
          });
        })
        .catch((error) => {
          this.loginmsg = "Access denied. " + error;
        });
    },
  },
};
</script>