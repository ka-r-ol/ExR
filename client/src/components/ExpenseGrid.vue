<template>
  <div class="overflow-auto">
    <!--   NAVBAR -->
    <div>
      <b-navbar fixed="top" toggleable="sm" type="dark" variant="secondary">
        <b-navbar-brand href="#">Expenses</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="#" v-b-toggle.filter-sidebar>Filter</b-nav-item>
            <b-nav-item href="#" v-b-toggle.report>Report</b-nav-item>
            <b-nav-item href="#" v-b-toggle.add-expense>Add</b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <em>{{ $store.state.username }}</em>
              </template>
              <b-dropdown-item @click="logout" href="#"
                >Sign Out</b-dropdown-item
              >
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
      <br />
      <br />
      <br />
    </div>
    <!--  NAVBAR END -->
    <div>
      <!--   REPORT -->
      <b-collapse id="report">
        <b-card class="mb-2" header-tag="header1">
          <template #header>
            <h6 class="mb-0">Report</h6>
          </template>
          <Report ref="report" />
        </b-card>
      </b-collapse>
      <!--   REPORT END -->

      <!--   ADD EXPENSE  -->
      <b-collapse id="add-expense" class="mb-3">
        <b-card class="mb-2" header-tag="header2">
          <template #header>
            <h6 class="mb-0">Add expense</h6>
          </template>
          <AddExpense @clicked="onAddExpense" />
        </b-card>
      </b-collapse>
      <!--   ADD EXPENSE END -->

      <!--   FILTER -->
      <b-sidebar
        id="filter-sidebar"
        title="Filter"
        aria-labelledby="sidebar-no-header-title"
        backdrop="backdrop"
        shadow
      >
        <ExpenseFilter @clicked="onExpenseFilter" />
      </b-sidebar>
      <!--   FILTR END -->

      <b-pagination
        align="right"
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
      ></b-pagination>

      <!--    ITEMS PER PAGE -->
      <div class="mb-3" align="right">
        Items per Page:
        <select v-model="pageSize" @change="handlePageSizeChange($event)">
          <option v-for="size in pageSizes" :key="size" :value="size">
            {{ size }}
          </option>
        </select>
        <span class="ml-3">Pages: {{ numPages }} </span>
      </div>
      <!--    ITEMS PER PAGE END -->

      <div class="mb-3" align="right">
        {{ messageFiltered }}
      </div>

      <!--    Expense LIST -->
      <b-table
        id="my-table"
        ref="ExpenseGrid"
        :items="provideExpenses"
        :per-page="perPage"
        :current-page="currentPage"
        :fields="fields"
        :hover="true"
        small
      ></b-table>
      <!--    Expense LIST END -->
    </div>
  </div>
</template>

<script>
//import { BASE_API_URL, LoadCategories } from "../settings";
import axios from "axios";
import ExpenseFilter from "./ExpenseFilter.vue";
import AddExpense from "./AddExpense.vue";
import Report from "./Report.vue";

export default {
  props: [],
  components: { ExpenseFilter, AddExpense, Report },
  mounted() {
    this.$store.dispatch("loadStats");
  },
  data() {
    return {
      backdrop: true,
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
          //sortable: true,
          class: "text-right",
          //variant: "danger",
        },
      ],
    };
  },
  computed: {
    categories() {
      var categories_conv = {};
      this.$store.state.categories_raw.forEach(
        (el) => (categories_conv[el.id] = el.name)
      );
      return categories_conv;
    },
    rows() {
      return this.count;
    },
    numPages() {
      return Math.ceil(this.count / this.perPage);
    },
    messageFiltered() {
      var message = this.$store.getters.get_filter_url_suffix.replace(
        /&/g,
        " "
      );
      /*
      if (this.$store.state.paramFilter.cost_min != "") {
        message += "min cost " + this.$store.state.paramFilter.cost_min + "; ";
      }
      if (this.$store.state.paramFilter.cost_max != "") {
        message += "max cost " + this.$store.state.paramFilter.cost_max + "; ";
      }
      // date_after=2020-09-25&date_before=2020-09-28&name=e&
      if (this.$store.state.paramFilter.date_before != "") {
        message +=
          "date before " + this.$store.state.paramFilter.date_before + "; ";
      }
      if (this.$store.state.paramFilter.date_after != "") {
        message +=
          "date after " + this.$store.state.paramFilter.date_after + "; ";
      }
      if (this.$store.state.paramFilter.name != "") {
        message += "name includes " + this.$store.state.paramFilter.name + "; ";
      }
      if (this.$store.state.paramFilter.category__name != "") {
        message +=
          "category includes " +
          this.$store.state.paramFilter.category__name +
          "; ";
      }
      */
      if (message != "") {
        message = "Filter: " + message;
      }
      return message;
    },
  },
  methods: {
    onAddExpense: function (value) {
      event.preventDefault();
      var url = this.$store.state.BASE_API_URL + "expense/new";
      axios
        .post(url, value.data, {
          auth: {
            username: this.$store.state.username,
            password: this.$store.state.password,
          },
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((res) => {
          this.provideStats();
          //this.$store.dispatch("loadStats");
          this.$store.state.message_add_success = "Expense added successfully";
          this.$store.state.message_add_danger = "";
          this.$refs.report.$refs.report_tab1.refresh();
          this.$refs.report.$refs.report_tab2.refresh();
          this.$refs.ExpenseGrid.refresh();
          console.log("REFFF", this.$refs);
        })
        .catch((error) => {
          this.$store.state.message_add_success = "";
          this.$store.state.message_add_danger = "Error: " + error;
          console.log(error); //Logs a string: Error: Request failed with status code 404
        });

      console.log("REFS", this.$refs);
    },
    provideStats: function () {
      //return;
      this.$store.dispatch("loadStats");
      this.$refs.report.$refs.report_tab1.refresh();
      this.$refs.report.$refs.report_tab2.refresh();
      this.$refs.ExpenseGrid.refresh();
      /*
      let url_stats = this.$store.state.BASE_API_URL + "stats";
      if (this.$store.getters.get_filter_url_suffix != "") {
        url_stats += "?" + this.$store.getters.get_filter_url_suffix.slice(1);
      }

      const promise = axios.get(url_stats, {
        auth: {
          username: this.$store.state.username,
          password: this.$store.state.password,
        },
      });
      return promise.then((res) => {
        this.$store.state.stats = res.data;
        this.$refs.report.$refs.report_tab1.refresh();
        this.$refs.report.$refs.report_tab2.refresh();
        this.$refs.ExpenseGrid.refresh();
      });
      */
      /*
      axios
        .get(url_stats, {
          auth: {
            username: this.$store.state.username,
            password: this.$store.state.password,
          },
        })
        .then((res) => {
          // Pluck the array of items off our axios response
          this.$store.state.stats = res.data;
          this.$refs.report.$refs.report_tab1.refresh();
          this.$refs.report.$refs.report_tab2.refresh();
          this.$refs.ExpenseGrid.refresh();
          console.log("STAT RES.DATA", res.data);
        })
        .catch((error) => {
          console.log(error); //Logs a string: Error: Request failed with status code 404
        });
        */
    },
    onExpenseFilter: function (value) {
      event.preventDefault();
      //this.$store.dispatch("loadStats");
      this.provideStats();
    },
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
        this.$store.state.BASE_API_URL +
        "expenses?limit=" +
        limit +
        "&offset=" +
        offset;
      url_expenses += this.$store.getters.get_filter_url_suffix;

      console.log("URL_EXPENSES", url_expenses);
      const promise = axios.get(url_expenses, {
        auth: {
          username: this.$store.state.username,
          password: this.$store.state.password,
        },
      });

      // Must return a promise that resolves to an array of items
      return promise.then((res) => {
        // Pluck the array of items off our axios response
        this.items = res.data.results;
        this.count = res.data.count;
        this.items.forEach(
          //(el) => (el.categoryName = this.categories[el.category])
          (el) => (el.categoryName = this.categories[el.category])
        );
        // Must return an array of items or an empty array if an error occurred
        return this.items || [];
      });
    },
  },
};
</script>