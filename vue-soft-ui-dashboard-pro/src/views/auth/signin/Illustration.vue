<template>
  <div class="container top-0 position-sticky z-index-sticky">
    <div class="row">
      <div class="col-12">
        <navbar
          is-blur="blur blur-rounded my-3 py-2 start-0 end-0 mx-4 shadow"
          btn-background="bg-gradient-success"
          :dark-mode="true"
        />
      </div>
    </div>
  </div>
  <main class="mt-0 main-content">
    <section>
      <div class="page-header min-vh-100">
        <div class="container">
          <div class="row">
            <div
              class="mx-auto col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0"
            >
              <div class="card card-plain">
                <div class="pb-0 card-header text-start">
                  <h4 class="font-weight-bolder">登录</h4>
                  <p class="mb-0">请输入用户名和密码</p>
                  <p class="mb-0">Enter your email and password to sign in</p>
                </div>
                <div class="card-body">
                  <form role="form">
                    <div class="mb-3">
                      <!-- <soft-input
                        id="email"
                        type="email"
                        placeholder="Email"
                        name="email"
                        size="lg"
                      /> -->
                      <a-input v-model:value="username" placeholder="" />
                    </div>
                    <!-- <div class="mb-3"> -->
                      <!-- <soft-input
                        id="password"
                        type="password"
                        placeholder="Password"
                        name="password"
                        size="lg"
                      /> -->
                      <a-input-password v-model:value="password" placeholder="" />
                    <!-- </div> -->
                    <soft-switch id="rememberMe" name="rememberMe">
                      记住我
                    </soft-switch>

                    <div class="text-center">
                      <soft-button
                        class="mt-4"
                        variant="gradient"
                        color="success"
                        full-width
                        size="lg"
                        @click="loginclk"
                        >登录
                      </soft-button>
                    </div>
                  </form>
                </div>
                <div class="px-1 pt-0 text-center card-footer px-lg-2">
                  <p class="mx-auto mb-4 text-sm">
                    还没有账户?
                    <router-link
                      :to="{ name: 'Signup Illustration' }"
                      class="text-success text-gradient font-weight-bold"
                    >
                      注册
                    </router-link>
                  </p>
                </div>
              </div>
            </div>
            <div
              class="top-0 my-auto text-center col-6 d-lg-flex d-none h-100 pe-0 position-absolute end-0 justify-content-center flex-column"
            >
              <div
                class="m-3 position-relative bg-gradient-success h-100 px-7 border-radius-lg d-flex flex-column justify-content-center"
              >
                <img
                  src="@/assets/img/shapes/pattern-lines.svg"
                  alt="pattern-lines"
                  class="position-absolute opacity-4 start-0"
                />

                <h4 class="mt-5 text-white font-weight-bolder">
                  文渊-论文管理系统
                </h4>
                <p class="text-white">
                  Wenyuan Paper Management System
                </p>
                <p class="text-white">
                  &nbsp; &nbsp; &nbsp; &nbsp;你的私人知识财产管理系统，通过智能化的分类和搜索功能，轻松整理和管理文献、笔记和研究成果。安全加密技术保障您的数据安全，不用担心泄露和丢失。
                </p>
                <p class="text-white">
                  &nbsp; &nbsp; &nbsp; &nbsp;高度可定制的界面和功能，满足个性化需求。文渊不仅是一款工具，更是您知识创造和管理的得力助手。让文渊与您并肩，开启知识管理新纪元。
                </p>

                <div class="position-relative">
                  <img
                    class="max-width-500 w-100 position-relative z-index-2"
                    src="@/assets/img/illustrations/chat.png"
                    alt="chat-img"
                  />
                </div>
                <!-- <h4 class="mt-5 text-white font-weight-bolder">
                  "Attention is the new currency"
                </h4>
                <p class="text-white">
                  The more effortless the writing looks, the more effort the
                  writer actually put into the process.
                </p> -->
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import Navbar from "@/examples/PageLayout/Navbar.vue";
// import SoftInput from "@/components/SoftInput.vue";
import SoftSwitch from "@/components/SoftSwitch.vue";
import SoftButton from "@/components/SoftButton.vue";
const body = document.getElementsByTagName("body")[0];
import axios from "axios";
import { message } from "ant-design-vue";

import { mapMutations } from "vuex";
// import { InputPassword } from "ant-design-vue";
export default {
  name: "SigninIllustration",
  components: {
    Navbar,
    // SoftInput,
    SoftSwitch,
    SoftButton,
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  created() {
    this.toggleEveryDisplay();
    this.toggleHideConfig();
    body.classList.remove("bg-gray-100");
  },
  beforeUnmount() {
    this.toggleEveryDisplay();
    this.toggleHideConfig();
    body.classList.add("bg-gray-100");
  },
  methods: {
    ...mapMutations(["toggleEveryDisplay", "toggleHideConfig"]),
    loginclk(event){
      event.preventDefault()
      axios.post("http://43.143.73.132:8000/api/user/login", {
        username: this.username,
        password: this.password,
      }).then((res) => {
        console.log(res);
        if (res.data.code == 200) {
          this.$store.state.logined = true;
          this.$store.state.click_total = res.data.data.click_total;
          this.$store.state.library_total = res.data.data.library_total;
          this.$store.state.paper_total = res.data.data.paper_total;
          this.$store.state.user_total = res.data.data.user_total;
          this.$store.state.user = res.data.data.user_info; 
          message.success("登录成功");
          this.$router.push({ name: "Default" });
        } else {
          message.error("登录失败");
        }
      }).catch((err) => {
        console.log(err);
        message.error("登录失败");
      });

    }
  },
};
</script>
