
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
  </div>
</template>

<script>
//import { mapState } from "vuex";

export default {
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("loadStats");
  },
  computed: {
    //   stats() {
    //    mapState(["stats"]);
    // },
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
      var it = [{ totals: "values", number: 0, cost: 0 }];
      for (let i in this.$store.state.stats) {
        //        console.log(i, i.number, i.cost);
        it[0]["number"] += this.$store.state.stats[i]["number"];
        it[0]["cost"] += this.$store.state.stats[i]["cost"];
      }
      return it;
    },
  },
};
</script>