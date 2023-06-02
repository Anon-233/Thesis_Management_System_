<template>
  <div class="col-12 col-md-10">
    <div class="card" :class="$attrs.class">
      <div class="p-3 pb-0 card-header">
        <div class="d-flex justify-content-between">
          <h6 class="mb-2">{{ title }}</h6>
        </div>
      </div>
      <div class="table-responsive">
        <table class="table align-items-center">
          <tbody>
            <tr
              v-for="({ papertitle, author, publisher, bounce }, index) of rows"
              :key="index"
            >
              <td class="w-30">
                <div class="px-2 py-1 d-flex align-items-center">
                  <div class="ms-4">
                    <p class="mb-0 text-xs font-weight-bold">标题</p>
                    <h6 class="mb-0 text-sm" ><div style="overflow: hidden; width: 70px;float: left;">{{ papertitle }}</div></h6>
                  </div>
                </div>
              </td>
              <td>
                <div class="text-center">
                  <p class="mb-0 text-xs font-weight-bold">作者</p>
                  <h6 class="mb-0 text-sm">{{ author }}</h6>
                </div>
              </td>
              <td>
                <div class="text-center">
                  <p class="mb-0 text-xs font-weight-bold">出版社</p>
                  <h6 class="mb-0 text-sm">{{ publisher }}</h6>
                  <!-- <h6 class="mb-0 text-sm" ><div style="overflow: hidden; width: 70px;float: left;">{{ publisher }}</div></h6> -->
                </div>
              </td>
              <td class="text-sm align-middle">
                <div class="text-center col">
                  <p class="mb-0 text-xs font-weight-bold">点击量</p>
                  <h6 class="mb-0 text-sm">{{ bounce }}</h6>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "SalesTable",
  props: {
    title: {
      type: String,
      default: "",
    },
    rows: {
      type: Array,
      required: true,
      papertitle: String,
      author: String,
      publisher: String,
      bounce: String,

    },
  },
};
</script>
