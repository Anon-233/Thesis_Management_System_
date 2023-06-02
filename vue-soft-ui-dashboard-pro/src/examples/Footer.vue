<template>
  <footer v-if="false" class="py-3 footer">
    <div class="container-fluid">
      <div class="row align-items-center justify-content-lg-between">
        <div class="mb-4 col-lg-6 mb-lg-0">
          <div
            class="text-sm text-center copyright text-muted"
            :class="this.$store.state.isRTL ? 'text-lg-end' : 'text-lg-start'"
          >
            ©
            {{ new Date().getFullYear() }}, made with
            <i class="fa fa-heart"></i> by
            <a
              href="https://www.littlexi.love/"
              class="font-weight-bold"
              target="_blank"
              >LittleXi</a
            >
            for 文渊智能管理系统
          </div>
        </div>
        <div class="col-lg-6">
          <ul
            class="nav nav-footer justify-content-center justify-content-lg-end"
          >
            <li class="nav-item">
              <a
                href="https://www.littlexi.love/"
                class="nav-link text-muted"
                target="_blank"
                >LittleXi</a
              >
            </li>
            <li class="nav-item">
              <a
                href="https://github.com/littlexi0"
                class="nav-link text-muted"
                target="_blank"
                >关于我</a
              >
            </li>
            <li class="nav-item">
              <a
                href="https://blog.csdn.net/qq_68591679?spm=1000.2115.3001.5343"
                class="nav-link text-muted"
                target="_blank"
                >博客</a
              >
            </li>
            <li class="nav-item">
              <a
                href="https://www.creative-tim.com/license"
                class="nav-link pe-0 text-muted"
                target="_blank"
                ></a
              >
            </li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "AppFooter",
};
</script>
