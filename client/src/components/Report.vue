
        <template>
  <div>
    <b-table
      table-variant="secondary"
      ref="report_tab1"
      responsive
      id="report-table"
      :items="items"
      small
      caption-top
    >
      <template #table-caption
        >Filtered expenses sub-totals by category:</template
      ></b-table
    >

    <b-table
      table-variant="secondary"
      ref="report_tab2"
      responsive
      id="report-table"
      :items="totals"
      small
      caption-top
    >
      <template #table-caption>Filtered totals:</template></b-table
    >
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
    <!-- BUTTONS -->
    <div align="center">
      <b-button size="sm" variant="warning" v-b-toggle.report>Close</b-button>
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
  mounted() {
    this.$store.dispatch("loadStats");
  },
  computed: {
    categories() {
      var categories_conv = {};
      this.$store.state.categories_raw.forEach(
        (el) => (categories_conv[el.id] = el.name)
      );
      return categories_conv;
    },
    items() {
      //this.$store.dispatch("loadStats");
      var it = [{ categories: "Number" }, { categories: "Total Cost" }];
      for (let i in this.$store.state.stats) {
        console.log(i, i.number, i.cost);
        it[0][i] = this.$store.state.stats[i]["number"];
        it[1][i] = this.$store.state.stats[i]["cost"];
      }
      return it;
    },
    totals() {
      var it = [{ "Total number": 0, "Total cost": 0 }];
      for (let i in this.$store.state.stats) {
        //        console.log(i, i.number, i.cost);
        it[0]["Total number"] += this.$store.state.stats[i]["number"];
        it[0]["Total cost"] += this.$store.state.stats[i]["cost"];
      }
      return it;
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