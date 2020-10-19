 <template>
  <div class="p-3">
    <!--<h4 id="sidebar-no-header-title">FILTER:</h4> -->
    <div>
      <b-container fluid>
        <!-- DATE  -->
        <b-row class="my-1">
          <b-col sm="3">
            <label for="date">Date:</label>
          </b-col>
          <b-col sm="4">
            <b-form-input
              id="date"
              size="sm"
              v-model="date"
              type="date"
              placeholder="Date"
            ></b-form-input>
          </b-col>
        </b-row>
        <!-- NAME -->
        <b-row class="my-1">
          <b-col sm="3">
            <label for="name-1">Name:</label>
          </b-col>
          <b-col sm="9">
            <b-form-input
              id="name-1"
              size="sm"
              v-model="name"
              type="text"
              placeholder=""
            ></b-form-input>
          </b-col>
        </b-row>

        <!-- CATEGORY  -->
        <b-row class="my-1">
          <b-col sm="3">
            <label for="category__name-3">Category:</label>
          </b-col>
          <b-col sm="9">
            <b-form-select
              v-model="category_id"
              :options="$store.state.categories_raw"
              value-field="id"
              text-field="name"
            ></b-form-select>
          </b-col>
        </b-row>

        <!-- COST  -->
        <b-row class="my-1">
          <b-col sm="3">
            <label for="cost">Cost:</label>
          </b-col>
          <b-col sm="4">
            <b-form-input
              id="cost"
              size="sm"
              v-model="cost"
              type="number"
              placeholder="currency"
            ></b-form-input>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <br />
    <!-- BUTTONS -->
    <div>
      <b-button size="sm" variant="success" block @click="onSubmit"
        >Submit</b-button
      >
      <b-button size="sm" variant="warning" block v-b-toggle.add-expense
        >Close</b-button
      >
      <b-button size="sm" variant="secondary" block @click="onClear"
        >Clear Form</b-button
      >
      <br />
    </div>
    <div class="text-success">
      {{ message_success }}
    </div>
    <div class="text-danger">
      {{ message_danger }}
    </div>
    <!-- BUTTONS END -->
    <!--<b-button size="sm" variant="warning" v-b-toggle.filter-sidebar block
      >Toggle Filter</b-button
    > -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: [],
  data() {
    return {
      date: new Date().toLocaleDateString("sv"), //trick: Sweden locale uses the ISO 8601 format
      name: "",
      category_id: "",
      cost: "",
      message_success: "",
      message_danger: "",
    };
  },
  computed: {},
  methods: {
    onSubmit: function () {
      //this.paramFilter = this.editFilter;
      console.log("PACZKA", this.date, this.name, this.category_id, this.cost);
      var url = this.$BASE_API_URL + "expense/new";
      var data = {
        name: this.name,
        cost: this.cost,
        date: this.date,
        category: this.category_id,
        owner: this.$store.state.user_id,
      };
      console.log("URL!!!", url);
      console.log("DATA!!!", data);
      console.log("USER-ID pre POST", this.$store.state.user_id, data.owner);
      axios
        .post(url, data, {
          auth: {
            username: this.$store.state.username,
            password: this.$store.state.password,
          },
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((res) => {
          this.message_success = "Expense added successfully";
          this.message_danger = "";
        })
        .catch((error) => {
          this.message_success = "";
          this.message_danger = "Error: " + error;
          console.log(error); //Logs a string: Error: Request failed with status code 404
        });
    },
    onClear: function () {
      console.log(
        "CAtegories_raw from store",
        this.$store.state.categories_raw
      );
      this.cost = 0;
      this.date = new Date().toLocaleDateString("sv"); //trick: Sweden locale uses the ISO 8601 format
      this.name = "";
      //this.category__name = "";
      this.message_success = "";
      this.message_danger = "";
    },
  },
};
</script>