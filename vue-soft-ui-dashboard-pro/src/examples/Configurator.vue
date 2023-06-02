<template>
  <div class="fixed-plugin">
    <!-- <a
      class="px-3 py-2 fixed-plugin-button text-dark position-fixed"
      @click="toggle"
    >
      <i class="py-2 fa fa-cog"> </i>
    </a> -->

    <div class="px-3 py-2 fixed-plugin-button  position-fixed aibtn"   @click="showDrawer">
    <!-- <img src="https://qny.littlexi.love/FuxTGuZvg8kVCGnrP4NsD8CRfRvw"> -->
    </div>
    <a-drawer
      title="珐露珊-机逐封秘"
      mask=false
      :placement="placement"
      :closable="false"
      :visible="visible"
      @close="onClose"
    >
    <p>积极求知，是学者不可或缺的品质 。夜晚是能够宁静思考的宝贵时段。知论派的研究涉及大量的古文与字符。</p>

      <div>
        <a-list
          v-if="comments.length"
          :data-source="comments"
          :header="`${comments.length} ${comments.length > 1 ? 'replies' : 'reply'}`"
          item-layout="horizontal"
        >
          <template #renderItem="{ item }">
            <a-list-item>
              <a-comment
                :author="item.author"
                :avatar="item.avatar"
                :content="item.content"
                :datetime="item.datetime"
              />

            </a-list-item>
          </template>
        </a-list> 
      </div>
      <div>
        <a-comment >
          <!-- <template #avatar>
            <a-avatar src="https://joeschmoe.io/api/v1/random" alt="Han Solo" />
          </template> -->
          <template #content>
            <a-textarea v-model:value="askvalue" placeholder="请输入内容..." :rows="4" />
            <span>&nbsp;</span>
            <a-form-item style="float: right;">
              <a-button html-type="submit" :loading="submitting" type="primary" @click="askclk">
                提问
              </a-button>
            </a-form-item>
          </template>
        </a-comment>
      </div>

    </a-drawer>
    <!-- <LikeFilled>ss</LikeFilled> -->
    <div class="shadow-lg card blur">
      <div class="pt-3 pb-0 bg-transparent card-header">
        <div class="float-start">
          <h5 class="mt-3 mb-0">文渊</h5>
          <p>界面设置</p>
        </div>
        <div class="mt-4 float-end" @click="toggle">
          <button class="p-0 btn btn-link text-dark fixed-plugin-close-button">
            <i class="fa fa-close"></i>
          </button>
        </div>
        <!-- End Toggle Button -->
      </div>
      <hr class="my-1 horizontal dark" />
      <div class="pt-0 card-body pt-sm-3">
        <!-- Sidebar Backgrounds -->
        <div>
          <h6 class="mb-0">主题颜色</h6>
        </div>
        <a href="#" class="switch-trigger background-color">
          <div
            class="my-2 badge-colors"
            :class="isRTL ? 'text-end' : ' text-start'"
          >
            <span
              class="badge filter bg-gradient-primary active"
              data-color="primary"
              @click="sidebarColor('primary')"
            ></span>
            <span
              class="badge filter bg-gradient-dark"
              data-color="dark"
              @click="sidebarColor('dark')"
            ></span>
            <span
              class="badge filter bg-gradient-info"
              data-color="info"
              @click="sidebarColor('info')"
            ></span>
            <span
              class="badge filter bg-gradient-success"
              data-color="success"
              @click="sidebarColor('success')"
            ></span>
            <span
              class="badge filter bg-gradient-warning"
              data-color="warning"
              @click="sidebarColor('warning')"
            ></span>
            <span
              class="badge filter bg-gradient-danger"
              data-color="danger"
              @click="sidebarColor('danger')"
            ></span>
          </div>
        </a>
        <!-- Sidenav Type -->
        <div class="mt-3">
          <h6 class="mb-0">侧边栏背景</h6>
          <!-- <p class="text-sm">Choose between 2 different sidenav types.</p> -->
        </div>
        <div class="d-flex">
          <button
            id="btn-transparent"
            class="px-3 mb-2 btn bg-gradient-success w-100"
            :class="isTransparent === 'bg-transparent' ? 'active' : ''"
            @click="sidebarType('bg-transparent')"
          >
            Transparent
          </button>
          <button
            id="btn-white"
            class="px-3 mb-2 btn bg-gradient-success w-100 ms-2"
            :class="isTransparent === 'bg-white' ? 'active' : ''"
            @click="sidebarType('bg-white')"
          >
            White
          </button>
        </div>
        <p class="mt-2 text-sm d-xl-none d-block">
          You can change the sidenav type just on desktop view.
        </p>
        <!-- Navbar Fixed -->
        <div class="mt-3">
          <h6 class="mb-0">固定导航栏</h6>
        </div>
        <div class="form-check form-switch ps-0">
          <input
            id="navbarFixed"
            class="mt-1 form-check-input"
            :class="isRTL ? 'float-end  me-auto' : ' ms-auto'"
            type="checkbox"
            :checked="isNavFixed"
            @click="setNavbarFixed"
          />
        </div>
        <hr class="mb-1 horizontal dark" />
        <div class="mt-2">
          <h6 class="mb-0">隐藏侧边栏描述</h6>
        </div>
        <div class="form-check form-switch ps-0">
          <input
            id="navbarMinimize"
            class="mt-1 form-check-input"
            :class="isRTL ? 'float-end  me-auto' : ' ms-auto'"
            type="checkbox"
            :checked="!isPinned"
            @click="navbarMinimize"
          />
        </div>
        <hr class="horizontal dark my-sm-4" />
        <a
          class="btn bg-gradient-info w-100"
          href="https://github.com/littlexi0"
          >联系我们</a
        >
        <a
          class="btn bg-gradient-dark w-100"
          href="https://demos.creative-tim.com/vue-soft-ui-dashboard/"
          >关于我们</a
        >
        <a
          class="btn btn-outline-dark w-100"
          href="https://www.littlexi.love/"
          >更多</a
        >
        <div class="text-center w-100">
          <h6 class="mt-3">感谢分享</h6>
          <a
            href="https://qzone.qq.com/"
            class="mb-0 btn btn-dark me-2"
            target="_blank"
          >
            <i class="fab fa-qq me-1" aria-hidden="true"></i> QQ
          </a>
          <a
            href="https://wx.qq.com/index.php"
            class="mb-0 btn btn-dark me-2"
            target="_blank"
          >
            <i class="fab fa-weixin me-1" aria-hidden="true"></i> 微信
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapActions, mapState } from "vuex";
import axios from 'axios';

import { defineComponent } from 'vue';
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
dayjs.extend(relativeTime);
// import dayjs from 'dayjs';
// import { LikeFilled, LikeOutlined, DislikeFilled, DislikeOutlined } from '@ant-design/icons-vue';
// import { defineComponent, ref } from 'vue';
// import relativeTime from 'dayjs/plugin/relativeTime';
dayjs.extend(relativeTime);

export default defineComponent({
  name: "Configurator",
  components: {
    // LikeFilled,
    // LikeOutlined,
    // DislikeFilled,
    // DislikeOutlined,
  },
  props: {
    toggle: {
      type: Function,
      default: null,
    },
  },
  // setup() {
    // const comments = ref([]);
    // const submitting = ref(false);
    // const value = ref('');
    // const handleSubmit = () => {
      // if (!value.value) {
      //   return;
      // }
      // submitting.value = true;
      // setTimeout(() => {
      //   submitting.value = false;
      //   comments.value = [{
      //     author: 'Han Solo',
      //     avatar: 'https://joeschmoe.io/api/v1/random',
      //     content: value.value,
      //     datetime: dayjs().fromNow(),
      //   }, ...comments.value];
      //   value.value = '';
      // }, 1000);
    // };
    // return {
      // comments,
      // submitting,
      // value,
      // handleSubmit,
    // };
  // },
  data() {
    return {
      // apiKey:this.$store.state.apiKey,
      placement:'right',
      visible:false,
      asktext:"",
      resptext:"",
      askvalue:"",
      submitting:false,
      comments:[
        {
          author:"珐露珊",
          avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
          content: "你好，我是小助理珐露珊，请问有什么需要帮助的吗？",
          datetime:""
        },
        {
          author:"littlexi",
          avatar: "https://qny.littlexi.love/FjKDpNq_oZfD3-zDja5MdiBrsDly",
          content: "你好呀",
          datetime:""
        },
        {
          author:"珐露珊",
          avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
          content: "我是珐露珊请问有什么可以帮助你的吗？",
          datetime:""
        },
        {
          author:"littlexi",
          avatar: "https://qny.littlexi.love/FjKDpNq_oZfD3-zDja5MdiBrsDly",
          content: "文言文怎么写？",
          datetime:""
        },
        {
          author:"珐露珊",
          avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
          content: "文言文是古代中国的一种文学语言，通常用于描述古代事件、文化、哲学思想等。以下是一些关于如何写文言文的基本指导：字词选择：文言文使用古代汉字和词语，所以要注意选择适当的字词。可以参考古代文献、诗词作品或字典来获取合适的词汇。语法结构：文言文的语法结构与现代汉语有所不同。句子的语序通常为主谓宾的顺序，修饰成分位于被修饰成分之前。需要注意的是，动词的使用也有一些特殊规则。文字表达：文言文的表达方式比较正式，通常使用较多的修辞手法，如比喻、夸张、对仗等。要注意修辞的使用要符合上下文的语境。",
          datetime:""
        },
      ]
    };
  },
  computed: {
    ...mapState([
      "isTransparent",
      "isNavFixed",
      "isAbsolute",
      "isPinned",
      "isRTL",
      "absolute",
      "color",
    ]),
    sidenavResponsive() {
      return this.sidenavTypeOnResize;
    },
  },
  
  beforeMount() {
    this.$store.state.isTransparent = "bg-transparent";
    // Deactivate sidenav type buttons on resize and small screens
    window.addEventListener("resize", this.sidenavTypeOnResize);
    window.addEventListener("load", this.sidenavTypeOnResize);
  },

  methods: {
    ...mapMutations(["navbarMinimize", "sidebarType", "navbarFixed"]),
    ...mapActions(["toggleSidebarColor", "setCardBackground"]),

    sidebarColor(color = "success") {
      document.querySelector("#sidenav-main").setAttribute("data-color", color);
      let mcolor = `card-background-mask-${color}`;
      this.setCardBackground(mcolor);
    },

    sidebarType(type) {
      this.toggleSidebarColor(type);
    },

    setNavbarFixed() {
      if (!this.isAbsolute) {
        this.navbarFixed();
      } else {
        this.absolute;
      }
    },

    sidenavTypeOnResize() {
      let transparent = document.querySelector("#btn-transparent");
      let white = document.querySelector("#btn-white");
      if (window.innerWidth < 1200) {
        transparent.classList.add("disabled");
        white.classList.add("disabled");
      } else {
        transparent.classList.remove("disabled");
        white.classList.remove("disabled");
      }
    },
    askclk(){
      // const apiKey = process.env.OPENAI_API_KEY;
      this.submitting = true;
      var newcomment = [{
        author: "LittleXi",
        avatar: "https://pchub.littlexi.love/avatar/xi.jpg",
        content: this.askvalue,
        datetime: ""
      }]
      this.comments.push(...newcomment);
      const model = 'gpt-3.5-turbo';
      
      const messages = [{ role: 'user', content: "假如你是原神中的珐露珊，你需要回答我以下的问题："+this.askvalue }];

      const config = {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': "Bearer "+this.$store.state.apikey,
          // 'Authorization': `Bearer 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`
        },
      };

      const requestData = {
        model,
        messages,
      };
      console.log(requestData)
      const cancelTokenSource = axios.CancelToken.source();
      console.log(config)
      axios.post('https://api.openai.com/v1/chat/completions', requestData, config,{ cancelToken: cancelTokenSource.token })
        .then(response => {
          const completion = response.data.choices[0].message;
          this.askvalue='';
          this.submitting = false;
          var newcomment = [{
            author: "珐露珊",
            avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
            content: completion.content,
            datetime: ""
          }]
          this.comments.push(...newcomment);
          // this.$message({
          //   message: completion.content,
          //   type: 'success'
          // });
        }) .catch(error => {
        if (axios.isCancel(error)) {
          // 请求已被取消
          console.log('请求已取消');
        } else {
          // 处理其他错误
          this.submitting=false;
          this.$swal({
              title: "提问失败",
              text: "派蒙：珐露珊小姐姐在睡觉，我们还是不要打扰她啦",
              // icon: "error",
              customClass: {
                confirmButton: "btn bg-gradient-success",
              },
              buttonsStyling: false,
            });
          console.log('请求出错', error);
        }
      });
       
    },
    // const placement = ref('left');
    // const visible = ref(false);
    showDrawer(){
      this.$store.state.showSidenav = false;
      this.visible = true;
    },
    onClose(){
      this.$store.state.showSidenav = true;
      this.visible = false;
    }
  },
});
</script>

<style scoped>
  .aibtn{
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background-image: url("https://qny.littlexi.love/FuxTGuZvg8kVCGnrP4NsD8CRfRvw") !important;
    background-repeat: no-repeat !important;
    background-position: center !important;
        /* 设置背景图像的大小调整方式 */
    background-size: cover !important;
    background-size: contain;
    border: 2px solid skyblue; 
  }
</style>