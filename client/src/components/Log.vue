
        <template>
  <div>
    <b-table
      v-if="$store.getters.nb_session_expenses > 0"
      table-variant="info"
      ref="report_tab2"
      responsive
      id="report-table"
      :items="session_expenses"
      :fields="session_expense_fields"
      small
      caption-top
    >
      <template #table-caption>Session log:</template></b-table
    >
    <div v-else>
      <b-alert show variant="warning"
        >Log empty, no operations done during the session.</b-alert
      >
    </div>
    <!-- BUTTONS -->
    <div align="center">
      <b-button size="sm" variant="warning" v-b-toggle.log>Close</b-button>
    </div>

    <!-- BUTTONS END -->
  </div>
</template>

<script>
//import { mapState } from "vuex";

export default {
  data() {
    return {
      session_expense_fields: [
        { key: "id", class: "small" },
        { key: "action", class: "small" },
        { key: "timestamp", class: "small" },
        { key: "date", class: "small" },
        { key: "name", label: "Expense name", class: "small" },
        { key: "categoryName", label: "Category", class: "small" },
        { key: "cost", class: "text-right", class: "small" },
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

    session_expenses() {
      var it = [];
      this.$store.state.session_expenses.forEach((el) => {
        el.categoryName = this.categories[el.category];
      });
      return this.$store.getters.session_expenses;
    },
  },
};
</script>