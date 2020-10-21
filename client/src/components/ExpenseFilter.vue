 <template>
  <div class="p-3">
    <!--<h4 id="sidebar-no-header-title">FILTER:</h4> -->
    <div>
      <b-container fluid>
        <b-row class="my-1">
          <b-col sm="5">
            <label for="cost_min">Min Cost:</label>
          </b-col>
          <b-col sm="7">
            <b-form-input
              id="cost_min"
              size="sm"
              v-model="editFilter.cost_min"
              type="number"
              placeholder="Equal or higher than..."
            ></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="5">
            <label for="cost_max">Max Cost:</label>
          </b-col>
          <b-col sm="7">
            <b-form-input
              id="cost_max"
              size="sm"
              v-model="editFilter.cost_max"
              type="number"
              placeholder="Equal or less than..."
            ></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="4">
            <label for="date_before">Before:</label>
          </b-col>
          <b-col sm="8">
            <b-form-input
              id="date_before"
              size="sm"
              v-model="editFilter.date_before"
              type="date"
              placeholder="Date"
            ></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="4">
            <label for="date_after">After:</label>
          </b-col>
          <b-col sm="8">
            <b-form-input
              id="date_after"
              size="sm"
              v-model="editFilter.date_after"
              type="date"
              placeholder="Date"
            ></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="5">
            <label for="name">Name:</label>
          </b-col>
          <b-col sm="7">
            <b-form-input
              id="name"
              size="sm"
              v-model="editFilter.name"
              type="text"
              placeholder="(includes)"
            ></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1">
          <b-col sm="5">
            <label for="category__name-1">Category:</label>
          </b-col>
          <b-col sm="7">
            <b-form-input
              id="category__name-1"
              size="sm"
              v-model="editFilter.category__name"
              type="text"
              placeholder="(includes)"
            ></b-form-input>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <br />
    <b-button size="sm" variant="primary" block @click="onApply"
      >Apply</b-button
    >
    <b-button size="sm" variant="secondary" block @click="onClear"
      >Clear Form</b-button
    >
    <b-button size="sm" variant="secondary" block @click="onCopy"
      >Current to Form</b-button
    >
    <!--<b-button size="sm" variant="warning" v-b-toggle.filter-sidebar block
      >Toggle Filter</b-button
    > -->
    <b-container class="mt-3" fluid>
      <b-row class="my-1"> Current parameters: </b-row>
      <b-row class="my-1">
        <b-col sm="5"> Min Cost: </b-col>
        <b-col sm="7">
          {{ $store.state.paramFilter.cost_min }}
        </b-col>
      </b-row>
      <b-row class="my-1">
        <b-col sm="5"> Max Cost: </b-col>
        <b-col sm="7">
          {{ $store.state.paramFilter.cost_max }}
        </b-col>
      </b-row>
      <b-row class="my-1">
        <b-col sm="4"> Before: </b-col>
        <b-col sm="8">
          {{ $store.state.paramFilter.date_before }}
        </b-col>
      </b-row>
      <b-row class="my-1">
        <b-col sm="4"> After: </b-col>
        <b-col sm="8">
          {{ $store.state.paramFilter.date_after }}
        </b-col>
      </b-row>
      <b-row class="my-1">
        <b-col sm="5"> Name: </b-col>
        <b-col sm="7">
          {{ $store.state.paramFilter.name }}
        </b-col>
      </b-row>
      <b-row class="my-1">
        <b-col sm="5"> Category: </b-col>
        <b-col sm="7">
          {{ $store.state.paramFilter.category__name }}
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  props: [],
  data() {
    return {
      editFilter: {
        cost_min: "",
        cost_max: "",
        date_before: "",
        date_after: "",
        name: "",
        category__name: "",
      },
    };
  },
  methods: {
    onCopy: function () {
      for (var i in this.editFilter) {
        this.editFilter[i] = this.$store.state.paramFilter[i];
      }
    },
    onApply: function () {
      //this.paramFilter = this.editFilter;
      //  for (var i in this.paramFilter) {
      //   this.$store.state.paramFilter[i] = this.editFilter[i];
      // }

      this.$store.commit("set_filter", this.editFilter);
      //console.log("--paramFILTER--", this.$store.state.paramFilter);
      this.$emit("clicked", {
        //paramFilter: this.paramFilter,
      });
    },
    onClear: function () {
      this.editFilter = {
        cost_min: "",
        cost_max: "",
        date_before: "",
        date_after: "",
        name: "",
        category__name: "",
      };
    },
  },
};
</script>