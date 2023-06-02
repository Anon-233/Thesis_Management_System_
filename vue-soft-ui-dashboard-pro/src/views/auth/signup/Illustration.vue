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
              class="col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0 mx-auto"
            >
              <div class="card card-plain">
                <div class="card-header pb-0 text-left">
                  <h4 class="font-weight-bolder">注册</h4>
                  <p class="mb-0">请输入用户名和密码注册</p>
                  <p class="mb-0">Enter your username and password to register</p>
                </div>
                <div class="card-body pb-3">
                  <form >
                    <label>用户名</label>
                    <a-input v-model:value="user.username" placeholder="" />
                    <label>密码</label>

                    <a-input-password v-model:value="password1" placeholder="" />
                    <label>请再次输入密码</label>
                    <a-input-password v-model:value="password2" placeholder="" />
                    <soft-checkbox
                    
                      id="flexCheckDefault"
                      class="font-weight-light"
                      name="terms"
                      checked
                    >
                      我同意
                      <a href="https://qny.littlexi.love/netxieyi" class="text-dark font-weight-bolder"
                        >用户须知</a
                      >
                    </soft-checkbox>
                    <div class="text-center"  >
                      <soft-button
                        color="success"
                        variant="gradient"
                        full-width
                        class="w-100 mt-4 mb-0"
                        @click="signinclik"
                        >注册</soft-button
                      >
                      <!-- <button @click="signinclik"></button> -->
                    </div>
                  </form>
                </div>
                <div class="card-footer text-center pt-0 px-sm-4 px-1">
                  <p class="mb-4 mx-auto">
                    已经有账户了？
                    <router-link
                      :to="{ name: 'Signin Illustration' }"
                      class="text-success text-gradient font-weight-bold"
                      >登录
                    </router-link>
                  </p>
                </div>
              </div>
            </div>
            <div
              class="col-6 d-lg-flex d-none h-100 my-auto pe-0 position-absolute top-0 end-0 text-center justify-content-center flex-column"
            >
              <div
                class="position-relative bg-gradient-success h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center"
              >
                <img
                  src="../../../assets/img/shapes/pattern-lines.svg"
                  alt="pattern-lines"
                  class="position-absolute opacity-4 start-0"
                />
                <h4 class="mt-5 text-white font-weight-bolder">
                  文渊-论文管理系统
                </h4>
                <p class="text-white">
                  Wenyuan Paper Management System
                </p>
                <div class="position-relative">
                  <img
                    class="max-width-500 w-100 position-relative z-index-2"
                    src="@/assets/img/illustrations/danger-chat-ill.png"
                    alt="chat-img"
                  />
                </div>
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
import SoftCheckbox from "@/components/SoftCheckbox.vue";
import SoftButton from "@/components/SoftButton.vue";
const body = document.getElementsByTagName("body")[0];
import axios from "axios";


import { mapMutations } from "vuex";
import { message } from "ant-design-vue";
export default {
  name: "SigninIllustration",
  components: {
    Navbar,
    // SoftInput,
    SoftCheckbox,
    SoftButton,
  },
  data(){
    return{
        password1:"",
        password2:"",
        user:{
          id:"",
          username: "user1",
          password: "user1user1",
          avatar:"",
          firstname: "",
          gender:"",
          birth:"",
          lastname: "",
          email: "",
          phone: "",
          location: "",
        },
    }
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
    signinclik(event){
      event.preventDefault()
      console.log(this.user)
      // console.log(1);
      if(this.password1!=this.password2){
        message.error("两次密码不一致,请检查重新输入");
        return;
      }
      // console.log(2)
      console.log(this.user)
      this.user.password=this.password1;
      axios.post('http://43.143.73.132:8000/api/user/register', this.user)
      .then(resp => {
        console.log(resp)
        if (resp.data.code === 200) {
          message.success("注册成功");
          this.$router.push({ name: "Signin Illustration" });
        } else {
          message.error("注册失败");
        }
      })
      .catch(err => {
        console.log(err)
        message.error("注册失败");
      });

    }
  }
};
</script>
