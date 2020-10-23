
        <template>
  <div>
    <div v-if="!$store.getters.get_statsLoad_status" class="text-center mb-3">
      <p>LOADING</p>
      <b-spinner
        style="width: 3rem; height: 3rem"
        wariant="primary"
      ></b-spinner>
    </div>
    <div v-show="$store.getters.get_statsLoad_status">
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
    </div>

    <!-- BUTTONS -->
    <div align="center">
      <b-button size="sm" variant="warning" v-b-toggle.report>Close</b-button>
    </div>

    <!-- BUTTONS END -->
  </div>
</template>

<script>
export default {
  data() {
    return {};
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
      var it = [{ categories: "Number" }, { categories: "Total Cost" }];
      for (let i in this.$store.state.stats) {
        it[0][i] = this.$store.state.stats[i]["number"];
        it[1][i] = this.$store.state.stats[i]["cost"];
      }
      return it;
    },
    totals() {
      var it = [{ "Total number": 0, "Total cost": 0 }];
      for (let i in this.$store.state.stats) {
        it[0]["Total number"] += this.$store.state.stats[i]["number"];
        it[0]["Total cost"] += this.$store.state.stats[i]["cost"];
      }
      return it;
    },
  },
};
</script>