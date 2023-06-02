<template>
  <aside
    id="sidenav-main"
    class="my-3 overflow-auto border-0 sidenav navbar navbar-vertical navbar-expand-xs border-radius-xl"
    :class="isRTL ? 'me-3 rotate-caret' : 'ms-3'"
  >
    <div class="sidenav-header">
      <i
        id="iconSidenav"
        class="top-0 p-3 cursor-pointer fas fa-times text-secondary opacity-5 position-absolute end-0 d-none d-xl-none"
        aria-hidden="true"
      ></i>
      <router-link class="m-0 navbar-brand" to="/">
        <img src="https://qny.littlexi.love/Fmw-Fk-A7NQfUnMwKEdch9Bma7I0" class="navbar-brand-img h-100" alt="main_logo" />
        <span class="ms-1 font-weight-bold">文渊</span>
      </router-link>
    </div>

    <hr class="mt-0 horizontal dark" />
    <sidenav-list :card-bg="customClass" />
  </aside>
</template>
<script>
import SidenavList from "./SidenavList.vue";
import logo from "@/assets/img/logo-ct.png";
import { mapState } from "vuex";
export default {
  name: "Index",
  components: {
    SidenavList,
  },
  props: {
    customClass: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      logo,
    };
  },
  computed: {
    ...mapState(["isRTL"]),
  },
};
</script>

<style scoped>
  .font-weight-bold{
    display: inline-block;
    margin-left: 20px;
    font-size: 25px;
  }
</style>