<template>
  <div class="card blur shadow-blur">
    <div class="card-body">
      <div class="d-flex">
        <p class="mb-0" :class="isRTL ? 'ms-5' : 'me-5'">
          {{ controllerIs }}
        </p>
        <soft-switch :id="id" :name="text" checked />
      </div>
      <img
        class="img-fluid pt-3 pb-2"
        src="../../../assets/img/small-logos/icon-bulb.svg"
        alt="bulb_icon"
      />
      <p class="mb-0">{{ text }}</p>
    </div>
  </div>
</template>

<script>
import SoftSwitch from "@/components/SoftSwitch.vue";
import { mapState } from "vuex";
export default {
  name: "ControllerCard",
  components: {
    SoftSwitch,
  },
  props: {
    id: {
      type: String,
      default: "",
    },
    controllerIs: {
      type: String,
      default: "On",
    },
    text: {
      type: String,
      default: "Lights",
    },
  },
  computed: {
    ...mapState(["isRTL"]),
  },
};
</script>
