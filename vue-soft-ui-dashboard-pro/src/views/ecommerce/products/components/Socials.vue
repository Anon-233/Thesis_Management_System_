<template>
  <div
    class="p-3 bg-white card multisteps-form__panel border-radius-xl"
    data-animation="FadeIn"
  >
    <h5 class="font-weight-bolder">机构/组织</h5>
    <div class="multisteps-form__content">
      <div class="mt-3 row">
        <div class="col-12">
          <label>机构/组织名称</label>
          <input
            v-model=library.orgnization_name
            class="form-control"
            type="text"
            placeholder="复旦大学"
          />
        </div>

        <div class="col-12">
          <label>机构/组织类型</label>
          <input
            v-model=library.orgnization_type
            class="form-control"
            type="text"
            placeholder="科研机构"
          />
        </div>

        <div class="col-12">
          <label>机构/组织官网链接</label>
          <input
            v-model=library.orgnization_url
            class="form-control"
            type="text"
            placeholder="https://..."
          />
        </div>

        <!-- <div class="col-12">
          <label>机构/组织类型</label>
          <soft-input
            v-model=library.orgnization_type
            class="form-control"
            type="text"
            placeholder="科研机构"
          />
        </div> -->
        <!-- <div class="col-12">
          <label>机构/组织官网链接</label>
          <soft-input
            v-model="library.orgnization_url"
            class="form-control"
            type="text"
            placeholder="https://..."
          />
        </div> -->
      </div>
      <div class="row">
        <div class="mt-4 button-row d-flex col-12">
          <!-- <soft-button
            color="secondary"
            variant="gradient"
            class="mb-0 js-btn-prev"
            title="Prev"
            @click="this.$parent.prevStep"
            >上一步</soft-button
          > -->
          <soft-button
            type="button"
            color="dark"
            variant="gradient"
            class="mb-0 ms-auto js-btn-next"
            title="Next"
            @click="submit"
            >提交</soft-button
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import SoftInput from "@/components/SoftInput.vue";
import SoftButton from "@/components/SoftButton.vue";
import axios from "axios";
import {message} from "ant-design-vue";
export default {
  name: "Socials",
  components: {
    // SoftInput,
    SoftButton,
  },
  data() {
    return {
      library:this.$store.state.library,
    };
  },
  methods: {
    submit() {
      // 发送提交的axios请求
      this.library.creater_id=this.$store.state.user.id;
      console.log(this.library)
      this.$store.state.library=this.library;
      
      axios.post("http://43.143.73.132:8000/api/library/", this.library).then((res) => {
        console.log(res);
        if (res.data.code == 200) {
          // this.$store.state.logined = true;
          // this.$store.state.user = res.data.data; 
          message.success("创建成功");
          this.$router.push({ name: "Products List" });
        } else {
          message.error("创建成功");
        }
      }).catch((err) => {
        message.error('创建失败');
        console.log(err);
      });
      // axios
      //   .post("http://43.143.73.132:8000/api/library", this.library)
      //   .then((res) => {
      //     console.log(res);
      //     if(res.status == 200)
      //     {
      //       message.success('提交成功');
      //     }
      //     else
      //     {
      //       message.error('提交失败');
      //     }
      //   })
      //   .catch((err) => {
      //     console.log(err);
      //   });
    },
  },
};
</script>
