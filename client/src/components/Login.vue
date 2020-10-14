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
export default {
  props: ["loginmsg"],
  data: function () {
    return {
      username: "",
      password: "",
    };
  },

  methods: {
    process: function () {
      // https://forum.vuejs.org/t/passing-data-back-to-parent/1201
      //console.log("username " + this.username + "pass " + this.password);
      //this.$emit("clicked", this.username); //{ username: username, password: password });
      event.preventDefault();
      this.$emit("clicked", {
        username: this.username,
        password: this.password,
      });
    },
  },
};
</script>