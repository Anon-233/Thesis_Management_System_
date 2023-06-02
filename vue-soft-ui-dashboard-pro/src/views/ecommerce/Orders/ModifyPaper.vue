<template>
    <div class="container-fluid">
      <div
        class="mt-4 page-header min-height-300 border-radius-xl"
        :style="{
          backgroundImage:
            'url(' + require('@/assets/img/curved-images/curved14.jpg') + ')',
          backgroundPositionY: '50%',
          textAlign:center,
        }"
      >
        <h2 class="title">修改论文</h2>
        <span class="mask bg-gradient-success opacity-6"></span>
      </div>
      <div v-if="false" class="mx-4 overflow-hidden card card-body blur shadow-blur mt-n6">
        <div class="row gx-4">
          <div v-if="false" class="col-auto">
            <div class="avatar avatar-xl position-relative">
              <img
                src="../../../assets/img/bruce-mars.jpg"
                alt="profile_image"
                class="shadow-sm w-100 border-radius-lg"
              />
            </div>
          </div>
          <div class="col-auto my-auto">
            <div class="h-100">
              <h5 class="mb-1">Alec Thompson</h5>
              <p class="mb-0 text-sm font-weight-bold">CEO / Co-Founder</p>
            </div>
          </div>
          <div
            class="mx-auto mt-3 col-lg-4 col-md-6 my-sm-auto ms-sm-auto me-sm-0"
          >
            <div class="nav-wrapper position-relative end-0">
              <ul
                class="p-1 bg-transparent nav nav-pills nav-fill"
                role="tablist"
              >
                <li class="nav-item">
                  <a
                    class="px-0 py-1 mb-0 nav-link active"
                    data-bs-toggle="tab"
                    href="javascript:;"
                    role="tab"
                    aria-selected="true"
                  >
                    <svg
                      class="text-dark"
                      width="16px"
                      height="16px"
                      viewBox="0 0 42 42"
                      version="1.1"
                      xmlns="http://www.w3.org/2000/svg"
                      xmlns:xlink="http://www.w3.org/1999/xlink"
                    >
                      <g
                        stroke="none"
                        stroke-width="1"
                        fill="none"
                        fill-rule="evenodd"
                      >
                        <g
                          transform="translate(-2319.000000, -291.000000)"
                          fill="#FFFFFF"
                          fill-rule="nonzero"
                        >
                          <g transform="translate(1716.000000, 291.000000)">
                            <g transform="translate(603.000000, 0.000000)">
                              <path
                                class="color-background"
                                d="M22.7597136,19.3090182 L38.8987031,11.2395234 C39.3926816,10.9925342 39.592906,10.3918611 39.3459167,9.89788265 C39.249157,9.70436312 39.0922432,9.5474453 38.8987261,9.45068056 L20.2741875,0.1378125 L20.2741875,0.1378125 C19.905375,-0.04725 19.469625,-0.04725 19.0995,0.1378125 L3.1011696,8.13815822 C2.60720568,8.38517662 2.40701679,8.98586148 2.6540352,9.4798254 C2.75080129,9.67332903 2.90771305,9.83023153 3.10122239,9.9269862 L21.8652864,19.3090182 C22.1468139,19.4497819 22.4781861,19.4497819 22.7597136,19.3090182 Z"
                              />
                              <path
                                class="color-background"
                                d="M23.625,22.429159 L23.625,39.8805372 C23.625,40.4328219 24.0727153,40.8805372 24.625,40.8805372 C24.7802551,40.8805372 24.9333778,40.8443874 25.0722402,40.7749511 L41.2741875,32.673375 L41.2741875,32.673375 C41.719125,32.4515625 42,31.9974375 42,31.5 L42,14.241659 C42,13.6893742 41.5522847,13.241659 41,13.241659 C40.8447549,13.241659 40.6916418,13.2778041 40.5527864,13.3472318 L24.1777864,21.5347318 C23.8390024,21.7041238 23.625,22.0503869 23.625,22.429159 Z"
                                opacity="0.7"
                              />
                              <path
                                class="color-background"
                                d="M20.4472136,21.5347318 L1.4472136,12.0347318 C0.953235098,11.7877425 0.352562058,11.9879669 0.105572809,12.4819454 C0.0361450918,12.6208008 6.47121774e-16,12.7739139 0,12.929159 L0,30.1875 L0,30.1875 C0,30.6849375 0.280875,31.1390625 0.7258125,31.3621875 L19.5528096,40.7750766 C20.0467945,41.0220531 20.6474623,40.8218132 20.8944388,40.3278283 C20.963859,40.1889789 21,40.0358742 21,39.8806379 L21,22.429159 C21,22.0503869 20.7859976,21.7041238 20.4472136,21.5347318 Z"
                                opacity="0.7"
                              />
                            </g>
                          </g>
                        </g>
                      </g>
                    </svg>
                    <span class="ms-1">App</span>
                  </a>
                </li>
                <li class="nav-item">
                  <a
                    class="px-0 py-1 mb-0 nav-link"
                    data-bs-toggle="tab"
                    href="javascript:;"
                    role="tab"
                    aria-selected="false"
                  >
                    <svg
                      class="text-dark"
                      width="16px"
                      height="16px"
                      viewBox="0 0 40 44"
                      version="1.1"
                      xmlns="http://www.w3.org/2000/svg"
                      xmlns:xlink="http://www.w3.org/1999/xlink"
                    >
                      <title>document</title>
                      <g
                        stroke="none"
                        stroke-width="1"
                        fill="none"
                        fill-rule="evenodd"
                      >
                        <g
                          transform="translate(-1870.000000, -591.000000)"
                          fill="#FFFFFF"
                          fill-rule="nonzero"
                        >
                          <g transform="translate(1716.000000, 291.000000)">
                            <g transform="translate(154.000000, 300.000000)">
                              <path
                                class="color-background"
                                d="M40,40 L36.3636364,40 L36.3636364,3.63636364 L5.45454545,3.63636364 L5.45454545,0 L38.1818182,0 C39.1854545,0 40,0.814545455 40,1.81818182 L40,40 Z"
                                opacity="0.603585379"
                              />
                              <path
                                class="color-background"
                                d="M30.9090909,7.27272727 L1.81818182,7.27272727 C0.814545455,7.27272727 0,8.08727273 0,9.09090909 L0,41.8181818 C0,42.8218182 0.814545455,43.6363636 1.81818182,43.6363636 L30.9090909,43.6363636 C31.9127273,43.6363636 32.7272727,42.8218182 32.7272727,41.8181818 L32.7272727,9.09090909 C32.7272727,8.08727273 31.9127273,7.27272727 30.9090909,7.27272727 Z M18.1818182,34.5454545 L7.27272727,34.5454545 L7.27272727,30.9090909 L18.1818182,30.9090909 L18.1818182,34.5454545 Z M25.4545455,27.2727273 L7.27272727,27.2727273 L7.27272727,23.6363636 L25.4545455,23.6363636 L25.4545455,27.2727273 Z M25.4545455,20 L7.27272727,20 L7.27272727,16.3636364 L25.4545455,16.3636364 L25.4545455,20 Z"
                              />
                            </g>
                          </g>
                        </g>
                      </g>
                    </svg>
                    <span class="ms-1">Messages</span>
                  </a>
                </li>
                <li class="nav-item">
                  <a
                    class="px-0 py-1 mb-0 nav-link"
                    data-bs-toggle="tab"
                    href="javascript:;"
                    role="tab"
                    aria-selected="false"
                  >
                    <svg
                      class="text-dark"
                      width="16px"
                      height="16px"
                      viewBox="0 0 40 40"
                      version="1.1"
                      xmlns="http://www.w3.org/2000/svg"
                      xmlns:xlink="http://www.w3.org/1999/xlink"
                    >
                      <title>settings</title>
                      <g
                        stroke="none"
                        stroke-width="1"
                        fill="none"
                        fill-rule="evenodd"
                      >
                        <g
                          transform="translate(-2020.000000, -442.000000)"
                          fill="#FFFFFF"
                          fill-rule="nonzero"
                        >
                          <g transform="translate(1716.000000, 291.000000)">
                            <g transform="translate(304.000000, 151.000000)">
                              <polygon
                                class="color-background"
                                opacity="0.596981957"
                                points="18.0883333 15.7316667 11.1783333 8.82166667 13.3333333 6.66666667 6.66666667 0 0 6.66666667 6.66666667 13.3333333 8.82166667 11.1783333 15.315 17.6716667"
                              />
                              <path
                                class="color-background"
                                d="M31.5666667,23.2333333 C31.0516667,23.2933333 30.53,23.3333333 30,23.3333333 C29.4916667,23.3333333 28.9866667,23.3033333 28.48,23.245 L22.4116667,30.7433333 L29.9416667,38.2733333 C32.2433333,40.575 35.9733333,40.575 38.275,38.2733333 L38.275,38.2733333 C40.5766667,35.9716667 40.5766667,32.2416667 38.275,29.94 L31.5666667,23.2333333 Z"
                                opacity="0.596981957"
                              />
                              <path
                                class="color-background"
                                d="M33.785,11.285 L28.715,6.215 L34.0616667,0.868333333 C32.82,0.315 31.4483333,0 30,0 C24.4766667,0 20,4.47666667 20,10 C20,10.99 20.1483333,11.9433333 20.4166667,12.8466667 L2.435,27.3966667 C0.95,28.7083333 0.0633333333,30.595 0.00333333333,32.5733333 C-0.0583333333,34.5533333 0.71,36.4916667 2.11,37.89 C3.47,39.2516667 5.27833333,40 7.20166667,40 C9.26666667,40 11.2366667,39.1133333 12.6033333,37.565 L27.1533333,19.5833333 C28.0566667,19.8516667 29.01,20 30,20 C35.5233333,20 40,15.5233333 40,10 C40,8.55166667 39.685,7.18 39.1316667,5.93666667 L33.785,11.285 Z"
                              />
                            </g>
                          </g>
                        </g>
                      </g>
                    </svg>
                    <span class="ms-1">Settings</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="false" class="py-4 container-fluid">
      <div class="row">
        <div class="col-12">
          <div class="multisteps-form">
            <div class="row">
              <div class="mx-auto mt-4 mb-3 col-12 col-lg-8 mb-sm-5">
                <div class="multisteps-form__progress">
                  <button
                    class="multisteps-form__progress-btn js-active"
                    type="button"
                    title="Product Info"
                    :class="activeStep >= 0 ? activeClass : ''"
                    @click="activeStep = 0"
                  >
                    <span>1. Product Info</span>
                  </button>
                  <button
                    class="multisteps-form__progress-btn"
                    type="button"
                    title="Media"
                    :class="activeStep >= 1 ? activeClass : ''"
                    @click="activeStep = 1"
                  >
                    2. Media
                  </button>
                  <button
                    class="multisteps-form__progress-btn"
                    type="button"
                    title="Socials"
                    :class="activeStep >= 2 ? activeClass : ''"
                    @click="activeStep = 2"
                  >
                    3. Socials
                  </button>
                  <button
                    class="multisteps-form__progress-btn"
                    type="button"
                    title="Pricing"
                    :class="activeStep >= 3 ? activeClass : ''"
                    @click="activeStep = 3"
                  >
                    4. Pricing
                  </button>
                </div>
              </div>
            </div>
            <!--form panels-->
            <div class="row">
              <div class="m-auto col-12 col-lg-8">
                <form class="mb-8 multisteps-form__form">
                  <!--single form panel-->
                  <product-info :class="activeStep === 0 ? activeClass : ''" />
                  <!--single form panel-->
                  <media :class="activeStep === 1 ? activeClass : ''" />
                  <!--single form panel-->
                  <socials :class="activeStep === 2 ? activeClass : ''" />
                  <!--single form panel-->
                  <pricing :class="activeStep === 3 ? activeClass : ''" />
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    
    
    
    </div>
    


    <div class="newpaper">

      <a-form
        :model="formState"
        name="validate_other"
        v-bind="formItemLayout"
        class="formStatecss"
        @finishFailed="onFinishFailed"
        @finish="onFinish"
      >
        <a-form-item label="论文标题">
          <a-form-item name="input-number" no-style >
            <!-- <a-input v-model="formState.title"/> -->
            <input
              v-model=formState.title
              class="form-control"
              type="text"
              placeholder=""
            />
          </a-form-item>
        </a-form-item>

        <!-- <a-form-item label="所属文献库"  :rules="[{ required: true, message: '文献库不能非空!' }]"> 
          <a-form-item name="input-number" no-style>
            <input
              v-model=formState.library_title
              class="form-control"
              type="text"
              placeholder=""
            />
          </a-form-item>
        </a-form-item> -->

        <a-form-item label="论文作者">
          <a-form-item name="input-number" no-style>
            <!-- <a-input v-model="formState.author"/> -->
            <input
              v-model=formState.author
              class="form-control"
              type="text"
              placeholder=""
            />
          </a-form-item>
        </a-form-item>

        <a-form-item
          name="select"
          label="国家"
          has-feedback

        >
        <input
            v-model=formState.country
            class="form-control"
            type="text"
            placeholder=""
          />
        </a-form-item>

        <a-form-item label="出版社">
          <a-form-item name="input-number" no-style>
            <!-- <a-input v-model="formState.press"/> -->
            <input
              v-model=formState.press
              class="form-control"
              type="text"
              placeholder=""
            />
          </a-form-item>
        </a-form-item>

        <a-form-item label="发表日期">
          <a-form-item name="input-number" no-style>
            <!-- <a-input v-model="formState.pressdata"/> -->
            <input
              v-model=formState.pressdate
              class="form-control"
              type="text"
              placeholder=""
            />
          </a-form-item>
        </a-form-item>

        <!-- <a-form-item label="InputNumber">
          <a-form-item name="input-number" no-style>
            <a-input-number v-model:value="formState['input-number']" :min="1" :max="10" />
          </a-form-item>
          <span class="ant-form-text">machines</span>
        </a-form-item> -->
        <a-form-item label="引用格式">
          <a-form-item name="input-number" no-style>
            <!-- <a-input v-model="formState.pressdata"/> -->
            <input
              v-model=formState.reference
              class="form-control"
              type="text"
              placeholder=""
            />
          </a-form-item>
        </a-form-item>


        <a-form-item label="PDF上传">
          <a-form-item name="dragger" no-style>
            <input id="inputField" name="inputField" type="file" placeholder="ds" @change="handleFileUpload">
          </a-form-item>
        </a-form-item>

        <!-- <a-button type="primary" :size="size" style="float: right;">
          <template #icon>
            <DownloadOutlined />
          </template>
          确认创建
        </a-button> -->
      </a-form>
      <a-button type="primary" size="large" style="float: right;margin-right: 30vh;" @click="submitmodify">
          <template #icon>
            <DownloadOutlined />
          </template>
          保存修改
        </a-button>
    </div>

  </template>
  
<script>
import ProductInfo from "../products/components/ProductInfo.vue";
import Media from "../products/components/Media.vue";
import Socials from "../products/components/Socials.vue";
import Pricing from "../products/components/Pricing.vue";
import axios from 'axios';
// import * as qiniu from 'qiniu-js';
import { message } from 'ant-design-vue';
import { defineComponent } from 'vue';
// import { UploadOutlined, InboxOutlined } from '@ant-design/icons-vue';
import setNavPills from "@/assets/js/nav-pills.js";

export default defineComponent({
  name: "ModifyPaper",
  components: {
    ProductInfo,
    Media,
    Socials,
    Pricing,
  },
  setup(){
    const formItemLayout = {
      labelCol: {
        span: 6,
      },
      wrapperCol: {
        span: 14,
      },
    };
    // const formState = reactive({
    //   'input-number': 3,
    //   'checkbox-group': ['A', 'B'],
    //   rate: 3.5,
    // });
    const onFinish = values => {
      console.log('Success:', values);
    };
    const onFinishFailed = errorInfo => {
      console.log('Failed:', errorInfo);
    };

    return {
      // formState,
      onFinish,
      onFinishFailed,
      formItemLayout,
    };
  },
  data() {
    return {
      showMenu: false,
      activeClass: "js-active position-relative",
      activeStep: 0,
      formSteps: 3,
      file: null,
      uploadUrl: 'https://upload.qiniup.com', // 替换为实际的上传地址
      token: this.$store.state.token, // 替换为实际的上传凭证
      avatar:this.$store.state.avatar,
      formState: this.$store.state.paper,
    //   formState:{
    //     title:'',
    //     library_title:'',
    //     creater_id:0,
    //     author:'',
    //     country:'',
    //     press:'',
    //     pressdate:'',
    //     url:''
    //   },
    };
  },
  created(){
    if(this.$store.state.logined === false)
      this.$router.push({ name: "Signin Illustration" });
  },
  mounted() {
    this.$store.state.isAbsolute = true;
    // this.getUploadToken();
    setNavPills();
  },
  beforeUnmount() {
    this.$store.state.isAbsolute = false;
  },
  methods: {
    nextStep() {
      if (this.activeStep < this.formSteps) {
        this.activeStep += 1;
      } else {
        this.activeStep -= 1;
      }
    },
    prevStep() {
      if (this.activeStep > 0) {
        this.activeStep -= 1;
      }
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
          this.formState.url = "https://qny.littlexi.love/"+response.data.key;
          // console.log(this.$store.state.library.certificate)
          console.log('文件上传成功', response.data);
        })
        .catch(error => {
          console.error('文件上传失败', error);
        });
    },
    submitmodify(){
      console.log(this.formState)
      axios.put('http://43.143.73.132:8000/api/paper/'+this.formState.id,this.formState)
      .then(resp=>{
        console.log(resp)
        if(resp.status == 200)
        {
          message.success("修改成功");
          // this.$store.state.paper=this.formState;
          this.$store.state.paper=resp.data.data;
        //   this.$router.push({name:"Order Details"});
        }
        else
        {
          message.error("修改失败");
        }
      })
      .catch(err => {
        console.log(err);
        message.error("修改失败，请稍后重试");
      });
    }
  }
});
</script>
  

<style scoped>
.formStatecss{
  margin-top: 3vh;
}
.newpaper{
  /* text-align: center; */
  /* background-color: pink; */
}
.title {
  font-size: 500%;
  color: #fff;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

</style>