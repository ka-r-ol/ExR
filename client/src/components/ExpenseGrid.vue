<template>
  <div class="overflow-auto">
    <!--   NAVBAR -->
    <div>
      <b-navbar fixed="top" toggleable="sm" type="dark" variant="secondary">
        <b-navbar-brand @click="$bvModal.show('bv-modal-Expenses')" href="#"
          >Expenses</b-navbar-brand
        >

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="#" v-b-toggle.filter-sidebar>Filter</b-nav-item>
            <b-nav-item href="#" v-b-toggle.report>Report</b-nav-item>
            <b-nav-item href="#" v-b-toggle.log>Log</b-nav-item>

            <b-nav-item href="#" v-b-toggle.add-expense>Add</b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <em>{{ $store.state.username }}</em>
              </template>
              <b-dropdown-item @click="logout" href="#">
                <b-icon icon="power" aria-hidden="true"></b-icon> Sign Out
              </b-dropdown-item>
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
      <!--   ABOUT Modal -->
      <div>
        <b-modal id="bv-modal-Expenses" hide-footer>
          <template #modal-title> About </template>
          <div class="d-block text-center">
            <h4>Simple Expense Report</h4>
            <h5>v.01</h5>
            <h6>by Karol Lemański, 2020 Oct</h6>
          </div>
          <b-button
            class="mt-3"
            block
            @click="$bvModal.hide('bv-modal-Expenses')"
            >Close</b-button
          >
        </b-modal>
      </div>
      <!--  ABOUT Modal END -->
      <!--   REPORT -->
      <b-collapse id="report">
        <b-card class="mb-2">
          <!-- header-tag="header1"> -->
          <template #header>
            <h6 class="mb-0">Report</h6>
          </template>
          <Report ref="report" />
        </b-card>
      </b-collapse>
      <!--   REPORT END -->

      <!--   LOG -->
      <b-collapse id="log">
        <b-card class="mb-2">
          <!-- header-tag="header1"> -->
          <template #header>
            <h6 class="mb-0">Session log</h6>
          </template>
          <Log ref="log" />
        </b-card>
      </b-collapse>
      <!--   LOG END -->

      <!--   ADD EXPENSE  -->
      <b-collapse id="add-expense" class="mb-3">
        <b-card class="mb-2">
          <!-- header-tag="header2"> -->
          <template #header>
            <h6 class="mb-0">Add expense</h6>
          </template>
          <AddUpdateExpense
            :operation="'Add'"
            :item="{ id: '', date: '', name: '', cost: '', category_id: '' }"
            @clicked="onAddExpense"
          />
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

      <!-- PAGINATION -->
      <b-pagination
        align="right"
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
      ></b-pagination>
      <!-- PAGINATION END -->

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

      <!--  AXIOS MSG SUCCESS/ FAILURE MODAL END -->

      <b-modal ref="axiosMsgModal" hide-footer :title="axiosStatusMsgTitle">
        <div class="d-block text-center">
          <h3>{{ axiosContentMsg }}</h3>
        </div>
        <b-button
          class="mt-3"
          variant="outline-success"
          block
          @click="hideAxiosMsgModal"
          >Close
        </b-button>
      </b-modal>
      <!-- AXIOS MSG SUCCESS/ FAILURE MODAL END -->

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
      >
        <template #cell(actionDelete)="row">
          <div align="right">
            <b-icon
              class="mr-3"
              @click="delete_modal(row.item, row.item.id, $event.target)"
              v-b-popover.hover.topleft="{
                variant: 'danger',
                content: 'Delete expense',
              }"
              icon="trash"
              font-scale="1"
            ></b-icon>
          </div>
        </template>
        >
        <template #cell(actionUpdate)="row">
          <div align="right">
            <b-icon
              icon="pencil-square"
              v-b-popover.hover.topleft="{
                variant: 'info',
                content: 'Update expense',
              }"
              @click="row.toggleDetails"
              font-scale="1"
            ></b-icon>
          </div>
        </template>
        <!-- -->
        <template #row-details="row">
          <b-card>
            <b-button
              variant="warning"
              size="sm"
              block
              @click="row.toggleDetails"
            >
              Cancel Update
            </b-button>
          </b-card>
        </template>
        <!-- -->
        <template #row-details="row">
          <!-- <b-collapse id="update-expense-1" class="mb-3"> -->
          <b-card class="mb-2">
            <!-- header-tag="header2"> -->
            <template #header>
              <h6 class="mb-0">Update expense</h6>
            </template>
            <AddUpdateExpense
              :operation="'Update'"
              :item="{
                id: row.item.id,
                date: row.item.date,
                name: row.item.name,
                cost: row.item.cost,
                category_id: row.item.category,
              }"
              @clicked="onUpdateExpense"
            />
          </b-card>
          <!--          </b-collapse> -->
          <!--
          <b-card>
            <b-button
              variant="danger"
              size="sm"
              block
              @click="removeExpense(row.item)"
              >Click to remove the above expense (id:{{ row.item.id }}) from
              database</b-button
            >
            <b-button
              variant="warning"
              size="sm"
              block
              @click="row.toggleDetails"
            >
              Cancel
            </b-button>
          </b-card>
          -->
        </template>
        <!-- -->
      </b-table>
      <!------ Delete Expense modal -->
      <!--        @ok="executeDeleteModal" 
        @hide="resetDeleteModal" -->
      <b-modal
        :id="deleteModal.id"
        :title="deleteModal.title"
        ref="deleteModal"
        @hide="resetDeleteModal"
        @ok="executeDeleteModal(deleteModal.id)"
      >
        <div align="center">
          <pre>{{ deleteModal.content }}</pre>
        </div>
      </b-modal>
      <!--
      <b-modal
        ref="deleteModal"
        :id="deleteModal.id"
        §hide-footer
        :title="deleteModal.title"
      >
        <div class="d-block text-center">
          <pre>{{ deleteModal.content }}</pre>
        </div>
        <b-button
          class="mt-3"
          variant="outline-success"
          block
          @click="executeDeleteModal"
          >OK
        </b-button>
        <b-button
          class="mt-3"
          variant="outline-danger"
          block
          @click="resetDeleteModal"
          >Cancel
        </b-button>
      </b-modal> -->
      <!--
      <b-modal hide-footer :id="deleteModal.id" :title="deleteModal.title">
        <div class="d-block text-center">
          <pre>{{ deleteModal.content }}</pre>
        </div>
        <div align="center">
          <b-button
            align="right"
            class="mt-3"
            variant="outline-success"
            @click="executeDeleteModal"
            >OK
          </b-button>
          <b-button
            align="right"
            class="mt-3"
            variant="outline-danger"
            @click="resetDeleteModal"
            >Cancel
          </b-button>
        </div>
      </b-modal> -->

      <!------ Delete Expense modal end -->
      <!--    Expense LIST END -->
    </div>
  </div>
</template>

<script>
//import { BASE_API_URL, LoadCategories } from "../settings";
import axios from "axios";
import ExpenseFilter from "./ExpenseFilter.vue";
import AddUpdateExpense from "./AddUpdateExpense.vue";
import Report from "./Report.vue";
import Log from "./Log.vue";

export default {
  props: [],
  components: { ExpenseFilter, AddUpdateExpense, Report, Log },
  mounted() {
    this.$store.dispatch("loadStats");
  },
  data() {
    return {
      axiosContentMsg: "axiosContentMsg",
      axiosStatusMsgTitle: "axiosStatusMsgTitle",
      deleteModal: {
        id: "delete-modal",
        title: "",
        content: "",
        item: null,
      },
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
          key: "id",
          sortable: false,
          class: "small",
        },
        {
          key: "date",
          sortable: false,
          class: "small",
        },
        {
          key: "name",
          label: "Expense name",
          class: "small",
        },
        {
          key: "categoryName",
          label: "Category",
          class: "small",
          //sortable: true,
          //variant: "info",
        },
        {
          key: "cost",
          //sortable: true,
          class: "small text-right",
          //variant: "danger",
        },
        {
          key: "actionDelete",
          class: "text-right",
          label: "",
          class: "small",
        },
        {
          key: "actionUpdate",
          class: "text-right",
          label: "",
          class: "small",
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
      if (message != "") {
        message = "Filter: " + message;
      }
      return message;
    },
  },
  methods: {
    showAxiosMsgModal(axiosStatusMsgTitle, axiosContentMsg) {
      this.axiosContentMsg = axiosContentMsg;
      this.axiosStatusMsgTitle = axiosStatusMsgTitle;
      //console.log("showAxiosMsgMoal");
      this.$refs["axiosMsgModal"].show();
    },
    hideAxiosMsgModal() {
      this.$refs["axiosMsgModal"].hide();
    },
    delete_modal(item, index, button) {
      this.deleteModal.title = `Expense ID: ${index}`;
      this.deleteModal.item = item;
      this.deleteModal.content =
        "Expense name: " +
        item.name +
        "\nCategory: " +
        item.categoryName +
        "\nCost: " +
        item.cost +
        "\n\nDelete?";
      //JSON.stringify(item, null, 2);
      this.$root.$emit("bv::show::modal", this.deleteModal.id, button);
    },
    resetDeleteModal() {
      //event.preventDefault();
      this.$refs["deleteModal"].hide();
      this.deleteModal.title = "";
      this.deleteModal.content = "";
      this.deleteModal.item = null;
    },
    executeDeleteModal(id) {
      //event.preventDefault();
      //this.$refs["deleteModal"].hide();
      this.$bvModal.hide(id);
      //console.log("executeDeleteModal", this.deleteModal);
      this.removeExpense(this.deleteModal.item);
    },
    removeExpense(item) {
      let url = this.$store.state.BASE_API_URL + "expense/" + item.id;
      axios
        .delete(url, {
          auth: {
            username: this.$store.state.username,
            password: this.$store.state.password,
          },
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((res) => {
          //this.showAxiosMsgModal("Success", "Expense deleted");
          this.provideStats();
          this.$store.commit("register_delete_session_expense", item);
          //this.$store.dispatch("loadStats");
          this.$refs.report.$refs.report_tab1.refresh();
          this.$refs.report.$refs.report_tab2.refresh();
          this.$refs.ExpenseGrid.refresh();
        })
        .catch((error) => {
          //this.showAxiosMsgModal("Deletion failure", error);
          console.log(error); //Logs a string: Error: Request failed with status code 404
        });
    },
    onUpdateExpense: function (value) {
      event.preventDefault();
      var url = this.$store.state.BASE_API_URL + "expense/" + value.data.id;
      //console.log("Placeholder onUpdateExpense", value, url);
      axios
        .patch(url, value.data, {
          auth: {
            username: this.$store.state.username,
            password: this.$store.state.password,
          },
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((res) => {
          //this.showAxiosMsgModal("Success", "Expense updated");
          this.provideStats();
          this.$store.commit("register_patch_session_expense", res.data);
          //this.$store.dispatch("loadStats");
          this.$store.state.message_add_success =
            "Expense patched successfully";
          this.$store.state.message_add_danger = "";
          this.$refs.report.$refs.report_tab1.refresh();
          this.$refs.report.$refs.report_tab2.refresh();
          this.$refs.ExpenseGrid.refresh();
        })
        .catch((error) => {
          this.showAxiosMsgModal("Update failure", error);

          this.$store.state.message_add_success = "";
          this.$store.state.message_add_danger = error;
          console.log(error); //Logs a string: Error: Request failed with status code 404
        });
    },
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
          this.showAxiosMsgModal("Success", "Expense added");

          this.provideStats();
          this.$store.commit("register_add_session_expense", res.data);
          //this.$store.dispatch("loadStats");
          this.$store.state.message_add_success = "Expense added successfully";
          this.$store.state.message_add_danger = "";
          this.$refs.report.$refs.report_tab1.refresh();
          this.$refs.report.$refs.report_tab2.refresh();
          this.$refs.ExpenseGrid.refresh();
        })
        .catch((error) => {
          this.showAxiosMsgModal("Failure", error);

          this.$store.state.message_add_success = "";
          this.$store.state.message_add_danger = "Error: " + error;
          console.log(error); //Logs a string: Error: Request failed with status code 404
        });
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

      //console.log("URL_EXPENSES", url_expenses);
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
        //console.log("ITEMS:", this.items);
        return this.items || [];
      });
    },
  },
};
</script>