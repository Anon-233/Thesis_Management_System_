<template>
  <div class="card">
    <div class="card-body">
      <p>{{ title }}</p>
      <h3>{{ count }}</h3>
      <soft-badge :color="badge.color">{{ badge.label }}</soft-badge>
    </div>
  </div>
</template>

<script>
import SoftBadge from "@/components/SoftBadge.vue";

export default {
  name: "StepsCard",
  components: {
    SoftBadge,
  },
  props: {
    title: {
      type: String,
      default: "Steps",
    },
    count: {
      type: String,
      default: "11.4K",
    },
    badge: {
      type: Object,
      label: String,
      color: String,
      default: () => ({
        color: "success",
      }),
    },
  },
};
</script>
