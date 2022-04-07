<script setup></script>

<template>
  <div class="find-me-outfit">
    <Nav />

    <main>
      <h1>Your Outfit Today</h1>
    </main>
    <form @submit.prevent="loadOutfit">
      <br />
      <h5>How hot (5) or cold (1): {{ howColdOrHot }}</h5>
      <br />
      <Slider v-model="howColdOrHot" :min="1" :max="5" :step="1" />
      <br />
      <div class="field col-12 md:col-4" style="margin-top: 5vh">
        <span class="p-float-label">
          <Dropdown
            id="dropdown"
            v-model="styleType"
            :options="style_types"
            optionLabel="name"
            style="width: 700px"
            placeholder="Style Type"
          />
        </span>
      </div>
      <br />

      <button class="btn-register-login" @click="$router.push('/outfit-found')">
        Find me outfit
      </button>
    </form>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/userStore";
import InputText from "primevue/inputtext";
import Password from "primevue/password";
import Image from "primevue/image";
import TabMenu from "primevue/tabmenu";
import Button from "primevue/button";
import Dropdown from "primevue/dropdown";
import InputNumber from "primevue/inputnumber";
import Slider from "primevue/slider";
import { ref } from "vue";
import Nav from "@/components/Nav.vue";

export default {
  components: {
    InputText,
    Password,
    Image,
    TabMenu,
    Button,
    Dropdown,
    InputNumber,
    Slider,
    Nav,
  },
  setup() {
    let howColdOrHot = ref(3);
    return { howColdOrHot };
  },
  data() {
    return {
      check: "check",
      how_cold_hot: null,
      style_types: [{ name: "Comfy" }, { name: "Casual" }, { name: "Elegant" }],
      styleType: null,
      userStore: useUserStore(),
    };
  },
  mounted() {
    console.log("hmm");
    console.log(this.userStore.user);
  },
  methods: {
    async loadOutfit() {},
  },
};
</script>

<style scoped>
.find-me-outfit {
  justify-content: center;
  justify-items: center;
  align-items: center;
  align-content: center;
  text-align: center;
}

.btn-register-login {
  margin-top: 15px;
  width: 280px;
  color: #fff;
  background-color: #171717;
  border: 1px solid #fff;
  border-radius: 10px;
  font-size: 28px;
  cursor: pointer;
  font-family: "Grape", "David";
  padding: 5px;
  align-self: center;
  justify-self: center;
}
</style>
