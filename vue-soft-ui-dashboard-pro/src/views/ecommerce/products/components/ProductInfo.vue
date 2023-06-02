<template>
  <div
    class="p-3 bg-white card multisteps-form__panel border-radius-xl"
    data-animation="FadeIn"
  >
    <h5 class="font-weight-bolder">文献库信息</h5>
    <div class="multisteps-form__content">
      <div class="mt-3 row">
        <div class="col-12 col-sm-6">
          <label>名称</label>
          <input
            v-model="library.title"
            class="multisteps-form__input form-control"
            type="text"
            placeholder="毕业论文"
          />
        </div>
        <div class="mt-3 col-12 col-sm-6 mt-sm-0">
          <label>主题</label>
          <input
            v-model="library.topic"
            class="multisteps-form__input form-control"
            type="text"
            placeholder="论文"
          />
        </div>
      </div>
      <div class="row">
        <div class="col-sm-6">
          <label class="mt-4">描述</label>
          <!-- <p class="text-xs form-text text-muted ms-1 d-inline">(可选)</p>
          <div id="edit-description" class="h-50">
          </div> -->
          <input
            v-model="library.description"
            class="multisteps-form__input form-control"
            type="text"
            placeholder="描述"
          />
        </div>
        <div class="mt-4 col-sm-6 mt-sm-0">
          <label class="mt-4">是否公开</label>
          <select
            id="choices-category"
            v-model="library.is_public"
            class="form-control"
            name="choices-category"
          >
            <option value="true" selected="">Yes</option>
            <option value="false">No</option>
          </select>
          <!-- <label>Sizes</label>
          <select id="choices-sizes" class="form-control" name="choices-sizes">
            <option value="Choice 1" selected="">Medium</option>
            <option value="Choice 2">Small</option>
            <option value="Choice 3">Large</option>
            <option value="Choice 4">Extra Large</option>
            <option value="Choice 5">Extra Small</option>
          </select> -->
        </div>
      </div>
      <div class="mt-4 button-row d-flex col-12">
        <soft-button
          type="button"
          color="dark"
          variant="gradient"
          class="mb-0 ms-auto js-btn-next"
          title="Next"
          @click="nextclk"
          >下一步</soft-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import Quill from "quill";
import Choices from "choices.js";
import SoftButton from "@/components/SoftButton.vue";

export default {
  name: "ProductInfo",
  components: {
    SoftButton,
  },
  data(){
    return {
      library:this.$store.state.library,
    }
  },
  mounted() {
    if (document.getElementById("edit-description")) {
      // eslint-disable-next-line no-unused-vars
      var quill = new Quill("#edit-description", {
        theme: "snow", // Specify theme in configuration
      });
    }
    if (document.getElementById("choices-category")) {
      var element = document.getElementById("choices-category");
      new Choices(element, {
        searchEnabled: false,
      });
    }

    if (document.getElementById("choices-sizes")) {
      let element = document.getElementById("choices-sizes");
      new Choices(element, {
        searchEnabled: false,
      });
    }
  },
  methods:{
    // @click="this.$parent.nextStep"
    nextclk(){
      this.$parent.nextStep();
      console.log(this.library);
      this.$store.state.library.title = this.library.title;
      this.$store.state.library.topic = this.library.topic;
      this.$store.state.library.description = this.library.description;
      if(this.library.is_public == "true")
        this.$store.state.library.is_public = true;
      else
        this.$store.state.library.is_public = false;
      // this.$store.state.library.is_public = this.library.is_public;
    }
  }
};
</script>
