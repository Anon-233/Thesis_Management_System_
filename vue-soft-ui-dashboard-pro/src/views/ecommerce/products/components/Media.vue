<template>
  <div
    class="p-3 bg-white card multisteps-form__panel border-radius-xl"
    data-animation="FadeIn"
  >
    <h5 class="font-weight-bolder">文献库证书</h5>
    <div class="multisteps-form__content">
      <!-- <div class="mt-3 row">
        <div class="col-12">
          <label>certificate</label>
          <form
            id="dropzone"
            action="/file-upload"
            class="form-control dropzone"
          >
            <div class="fallback">
              <input name="file" type="file" multiple @click="handleFileUpload"  />
            </div>
          </form>
        </div>
      </div> -->
      <input id="inputField" name="inputField" type="file" placeholder="ds" @change="handleFileUpload">
      <!-- <input name="file" type="file" multiple @click="handleFileUpload"  /> -->
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
          @click="nextclk"
          >下一步</soft-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import SoftButton from "@/components/SoftButton.vue";
import Dropzone from "dropzone";
import {message} from "ant-design-vue";
import axios from 'axios';

export default {
  name: "Media",
  components: {
    SoftButton,
  },
  data(){
    return{
      file: null,
      uploadUrl: 'https://upload.qiniup.com', // 替换为实际的上传地址
      token: this.$store.state.token,
    }
  },
  mounted() {
    Dropzone.autoDiscover = false;
    // var drop = document.getElementById("dropzone");
    // new Dropzone(drop, {
    //   url: "/file/post",
    //   addRemoveLinks: true,
    // });
  },

  methods: {
    nextclk() {
      this.$parent.nextStep();

    },
    handleFileUpload(event) {
      this.file = event.target.files[0];
      this.uploadFile();
    },
    uploadFile() {
      const formData = new FormData();
      formData.append('file', this.file);
      formData.append('token', this.token);
      console.log("upload")
      console.log(formData)
      axios
        .post(this.uploadUrl, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then(response => {
          // console.log
          message.success("文件上传成功");
          this.$store.state.library.certificate = "https://qny.littlexi.love/"+response.data.key;
          console.log(this.$store.state.library.certificate)
          console.log('文件上传成功', response.data);
        })
        .catch(error => {
          console.error('文件上传失败', error);
        });
    },
  },
};
</script>
