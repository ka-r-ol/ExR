<template>
  <div class="overflow-auto">
    <p id="welcome">Hello, {{ username }}.</p>
    <b-collapse id="report" class="mt-2">
      <template> Report </template>
    </b-collapse>
    <div align="right">
      <b-button-group>
        <b-button variant="info" v-b-toggle.report> Toggle Report</b-button>
        <b-button variant="warning" v-b-toggle.filter-sidebar
          >Toggle Filter</b-button
        >
        <b-button variant="secondary" @click="logout"> Logout </b-button>
      </b-button-group>
    </div>

    <b-sidebar
      id="filter-sidebar"
      aria-labelledby="sidebar-no-header-title"
      no-header
      shadow
    >
      <template v-slot:default="{ hide }">
        <div class="p-3">
          <h4 id="sidebar-no-header-title">Custom header sidebar</h4>
          <p>
            Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
            dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta
            ac consectetur ac, vestibulum at eros.
          </p>
          <nav class="mb-3">
            <b-nav vertical>
              <b-nav-item active @click="hide">Active</b-nav-item>
              <b-nav-item href="#link-1" @click="hide">Link</b-nav-item>
              <b-nav-item href="#link-2" @click="hide">Another Link</b-nav-item>
            </b-nav>
          </nav>
          <b-button variant="primary" block @click="hide"
            >Close Filter</b-button
          >
        </div>
      </template>
    </b-sidebar>
    <b-pagination
      align="right"
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>

    <p class="mt-3" align="right">
      Current Page: {{ currentPage }} out of {{ numPages }}
    </p>
    <!--    ITEMS PER PAGE -->
    <div class="mb-3" align="right">
      Items per Page:
      <select v-model="pageSize" @change="handlePageSizeChange($event)">
        <option v-for="size in pageSizes" :key="size" :value="size">
          {{ size }}
        </option>
      </select>
    </div>
    <!--    -->

    <b-table
      id="my-table"
      :items="provideExpenses"
      :per-page="perPage"
      :current-page="currentPage"
      :fields="fields"
      :hover="true"
      small
    ></b-table>
  </div>
</template>

<script>
//import { BASE_API_URL, LoadCategories } from "../settings";
import axios from "axios";

export default {
  props: ["username", "password", "categories"],
  data() {
    return {
      currentPage: 1,
      count: 0,
      pageSize: 3,
      perPage: 20,
      pageSizes: [20, 5, 10, 50, 100],
      // https://bootstrap-vue.org/docs/components/table#comp-ref-b-table
      // https://bootstrap-vue.org/docs/components/table#items-record-data
      // https://bootstrap-vue.org/docs/components/table#using-items-provider-functions
      fields: [
        {
          key: "date",
          sortable: false,
          class: "small",
        },
        {
          key: "name",
          label: "Expense name",
        },
        {
          key: "categoryName",
          label: "Category",
          //sortable: true,
          //variant: "info",
        },
        {
          key: "cost",
          sortable: true,
          class: "text-right",
          //variant: "danger",
        },
      ],
    };
  },
  computed: {
    rows() {
      return this.count;
    },
    numPages() {
      return Math.ceil(this.count / this.perPage);
    },
  },
  methods: {
    handlePageSizeChange: function ($event) {
      this.perPage = event.target.value;
      this.currentPage = 1;
    },
    logout: function () {
      event.preventDefault();
      this.$emit("clicked", {
        // authorized: false,
      });
    },
    provideExpenses: function (ctx) {
      //this.items[2]._rowVariant = "danger";
      // http://127.0.0.1:8000/api/v1/expenses?limit=12&offset=1
      //
      let limit = ctx.perPage;
      let offset = (ctx.currentPage - 1) * limit;
      let url_expenses =
        this.$BASE_API_URL + "expenses?limit=" + limit + "&offset=" + offset;
      const promise = axios.get(url_expenses, {
        auth: {
          username: this.username,
          password: this.password,
        },
      });

      // Must return a promise that resolves to an array of items
      return promise.then((res) => {
        // Pluck the array of items off our axios response
        this.items = res.data.results;
        this.count = res.data.count;
        this.items.forEach(
          (el) => (el.categoryName = this.categories[el.category])
        );
        // Must return an array of items or an empty array if an error occurred
        return this.items || [];
      });
    },
    /*
    fetchExpenses: function () {
      var url = BASE_API_URL + "expenses";
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
        })
        .catch((error) => {
          this.authorized = false;
          this.loginmsg = "Access denied. " + error;
          console.log(error);
        });

    },
    */
  },
};
</script>