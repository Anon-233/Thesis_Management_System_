<template>
  <div class="card">
    <div class="card-header pb-0">
      <div class="d-flex">
        <p>{{ title }}</p>
        <div :class="isRTL ? 'me-auto' : 'ms-auto'">
          <soft-badge :color="badge.color">{{ badge.text }}</soft-badge>
        </div>
      </div>
    </div>
    <div class="card-body pt-0">
      <p class="mb-0">{{ description }}</p>
    </div>
  </div>
</template>

<script>
import SoftBadge from "@/components/SoftBadge.vue";
import { mapState } from "vuex";
export default {
  name: "InfoCard",
  components: {
    SoftBadge,
  },
  props: {
    title: {
      type: String,
      default: "",
    },
    badge: {
      type: Object,
      default: () => ({
        color: "success",
        text: "Moderate",
      }),
      text: String,
      color: String,
    },
    description: {
      type: String,
      default: "",
    },
  },
  computed: {
    ...mapState(["isRTL"]),
  },
};
</script>
