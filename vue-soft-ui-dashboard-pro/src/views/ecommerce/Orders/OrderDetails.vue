<template>
  <div v-if="false" class="container-fluid py-4" >
    <div class="row">
      <div class="col-lg-8 mx-auto">
        <div class="card mb-4">
          <div class="card-header p-3 pb-0">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <h6>Order Details</h6>
                <p class="text-sm mb-0">
                  Order no.
                  <b>241342</b> from
                  <b>23.02.2021</b>
                </p>
                <p class="text-sm">
                  Code:
                  <b>KF332</b>
                </p>
              </div>
              <soft-button
                color="secondary"
                variant="gradient"
                class="ms-auto mb-0"
                >Invoice</soft-button
              >
            </div>
          </div>
          <div class="card-body p-3 pt-0">
            <hr class="horizontal dark mt-0 mb-4" />
            <div class="row">
              <div class="col-lg-6 col-md-6 col-12">
                <div class="d-flex">
                  <div>
                    <soft-avatar
                      img="https://images.unsplash.com/photo-1511499767150-a48a237f0083?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;ixlib=rb-1.2.1&amp;auto=format&amp;fit=crop&amp;w=1400&amp;q=80"
                      class="me-3"
                      size="xxl"
                      border-radius="lg"
                      alt="product image"
                    />
                  </div>
                  <div>
                    <h6 class="text-lg mb-0 mt-2">Gold Glasses</h6>
                    <p class="text-sm mb-3">Order was delivered 2 days ago.</p>
                    <soft-badge color="success" variant="gradient" size="sm"
                      >Delivered</soft-badge
                    >
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-md-6 col-12 my-auto text-end">
                <soft-button color="info" variant="gradient" class="mb-0"
                  >Contact Us</soft-button
                >
                <p class="text-sm mt-2 mb-0">
                  Do you like the product? Leave us a review
                  <a href="javascript:;">here</a>.
                </p>
              </div>
            </div>
            <hr class="horizontal dark mt-4 mb-4" />
            <div class="row">
              <div class="col-lg-3 col-md-6 col-12">
                <h6 class="mb-3">Track order</h6>
                <div class="timeline timeline-one-side">
                  <div class="timeline-block mb-3">
                    <span class="timeline-step">
                      <i class="ni ni-bell-55 text-secondary"></i>
                    </span>
                    <div class="timeline-content">
                      <h6 class="text-dark text-sm font-weight-bold mb-0">
                        Order received
                      </h6>
                      <p
                        class="text-secondary font-weight-bold text-xs mt-1 mb-0"
                      >
                        22 DEC 7:20 AM
                      </p>
                    </div>
                  </div>
                  <div class="timeline-block mb-3">
                    <span class="timeline-step">
                      <i class="ni ni-html5 text-secondary"></i>
                    </span>
                    <div class="timeline-content">
                      <h6 class="text-dark text-sm font-weight-bold mb-0">
                        Generate order id #1832412
                      </h6>
                      <p
                        class="text-secondary font-weight-bold text-xs mt-1 mb-0"
                      >
                        22 DEC 7:21 AM
                      </p>
                    </div>
                  </div>
                  <div class="timeline-block mb-3">
                    <span class="timeline-step">
                      <i class="ni ni-cart text-secondary"></i>
                    </span>
                    <div class="timeline-content">
                      <h6 class="text-dark text-sm font-weight-bold mb-0">
                        Order transmited to courier
                      </h6>
                      <p
                        class="text-secondary font-weight-bold text-xs mt-1 mb-0"
                      >
                        22 DEC 8:10 AM
                      </p>
                    </div>
                  </div>
                  <div class="timeline-block mb-3">
                    <span class="timeline-step">
                      <i
                        class="ni ni-check-bold text-success text-gradient"
                      ></i>
                    </span>
                    <div class="timeline-content">
                      <h6 class="text-dark text-sm font-weight-bold mb-0">
                        Order delivered
                      </h6>
                      <p
                        class="text-secondary font-weight-bold text-xs mt-1 mb-0"
                      >
                        22 DEC 4:54 PM
                      </p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-5 col-md-6 col-12">
                <h6 class="mb-3">Payment details</h6>
                <div
                  class="card card-body border card-plain border-radius-lg d-flex align-items-center flex-row"
                >
                  <img
                    class="w-10 me-3 mb-0"
                    src="../../../assets/img/logos/mastercard.png"
                    alt="logo"
                  />
                  <h6 class="mb-0">
                    ****&nbsp;&nbsp;&nbsp;****&nbsp;&nbsp;&nbsp;****&nbsp;&nbsp;&nbsp;7852
                  </h6>
                  <soft-button
                    color="secondary"
                    variant="outline"
                    class="btn-icon-only btn-rounded mb-0 ms-2 btn-sm d-flex align-items-center justify-content-center ms-auto"
                    data-bs-toggle="tooltip"
                    data-bs-placement="bottom"
                    title
                    data-bs-original-title="We do not store card details"
                  >
                    <i class="fas fa-info" aria-hidden="true"></i>
                  </soft-button>
                </div>
                <h6 class="mb-3 mt-4">Billing Information</h6>
                <ul class="list-group">
                  <li
                    class="list-group-item border-0 d-flex p-4 mb-2 bg-gray-100 border-radius-lg"
                  >
                    <div class="d-flex flex-column">
                      <h6 class="mb-3 text-sm">Oliver Liam</h6>
                      <span class="mb-2 text-xs">
                        Company Name:
                        <span class="text-dark font-weight-bold ms-2"
                          >Viking Burrito</span
                        >
                      </span>
                      <span class="mb-2 text-xs">
                        Email Address:
                        <span class="text-dark ms-2 font-weight-bold"
                          >oliver@burrito.com</span
                        >
                      </span>
                      <span class="text-xs">
                        VAT Number:
                        <span class="text-dark ms-2 font-weight-bold"
                          >FRB1235476</span
                        >
                      </span>
                    </div>
                  </li>
                </ul>
              </div>
              <div class="col-lg-3 col-12 ms-auto">
                <h6 class="mb-3">Order Summary</h6>
                <div class="d-flex justify-content-between">
                  <span class="mb-2 text-sm">Product Price:</span>
                  <span class="text-dark font-weight-bold ms-2">$90</span>
                </div>
                <div class="d-flex justify-content-between">
                  <span class="mb-2 text-sm">Delivery:</span>
                  <span class="text-dark ms-2 font-weight-bold">$14</span>
                </div>
                <div class="d-flex justify-content-between">
                  <span class="text-sm">Taxes:</span>
                  <span class="text-dark ms-2 font-weight-bold">$1.95</span>
                </div>
                <div class="d-flex justify-content-between mt-4">
                  <span class="mb-2 text-lg">Total:</span>
                  <span class="text-dark text-lg ms-2 font-weight-bold"
                    >$105.95</span
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <a-descriptions :title=paper.title>
      <a-descriptions-item label="文献库">{{ paper.library }}</a-descriptions-item>
      <a-descriptions-item label="作者">{{ paper.author }}</a-descriptions-item>
      <a-descriptions-item label="国家">{{ paper.country }}</a-descriptions-item>
      <a-descriptions-item label="出版社">{{ paper.press }}</a-descriptions-item>
      <a-descriptions-item label="日期">{{ paper.pressdate }}</a-descriptions-item>
      <a-descriptions-item label="平均分"><a-rate v-model:value="avgscore" disabled  /></a-descriptions-item>
      <a-descriptions-item label="评分">
         <a-rate v-model:value="markscore" />
         <a-button type="primary" ghost @click="submitmark">打分</a-button>
        </a-descriptions-item>
    </a-descriptions>
    
    <div class="containerpdf">
      <iframe :src=paper.url  class="pdf_iframe"></iframe>
    </div>

    <div class="postcomment">
      <a-comment >
        <!-- <template #avatar>
          <a-avatar src="https://joeschmoe.io/api/v1/random" alt="Han Solo" />
        </template> -->
        <template #content>
          <a-textarea v-model:value="commentvalue" placeholder="哎哟，不错哦，发条评论吧" :rows="4" />
          <span>&nbsp;</span>
          <a-form-item style="float: right;">
            <a-button html-type="submit" :loading="submitting" type="primary" @click="addcommentclk">
              发布
            </a-button>
          </a-form-item>
        </template>
      </a-comment>
    </div>

    <div class="containercomment">
      <a-list
          v-if="comments.length"
          :data-source="comments"
          :header="`${comments.length} ${comments.length > 1 ? 'replies' : 'reply'}`"
          item-layout="horizontal"
        >
          <template #renderItem="{ item }">
            <a-list-item>
              <a-comment
                :author="item.username"
                :avatar="item.avatar"
                :content="item.content"
                :datetime="item.time"
              />
              <a-button v-if="item.username == this.$store.state.user.username" type="dashed" size="small" danger @click="deleteComment(item)">删除</a-button>
            </a-list-item>
          </template>
        </a-list>
        <div style="display: flex; justify-content: center;">
          <a-button type="primary" @click="getcomment">加载更多</a-button>
        </div>

        </div>


  </div>

</template>

<script>
import SoftButton from "@/components/SoftButton.vue";
import SoftAvatar from "@/components/SoftAvatar.vue";
import SoftBadge from "@/components/SoftBadge.vue";
import axios from "axios";
import { message } from "ant-design-vue";
import { defineComponent, ref } from 'vue';
export default defineComponent({
  name: "OrderDetails",
  components: {
    SoftButton,
    SoftAvatar,
    SoftBadge,
  },
  data() {
    return {
      markscore : ref(0),
      avgscore : ref(this.$store.state.paper.mark),
      paper:this.$store.state.paper,
      page_num:0,
      page_size:10,
      // markscore:2,
      comments:[

      ],
      // comments: [
      //   {
      //     author: "小明",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "你好，我有一个问题需要咨询二次元是我的避风港，心情不好的时候会看，心情好的时候也会看，空虚的时候，平静的时候......我生命的每时每刻，他们是有血有肉的生命我始终相信我有一天能打破次元壁去到他们的世界旅行，就算要等到我死去的那一刻，也足了。",
      //     datetime: "2012-10-11"
      //   },
      //   {
      //     author: "littlexi",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "这是一个很有用的小助手。",
      //     datetime: ""
      //   },
      //   {
      //     author: "Alice",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "非常感谢你的帮助！",
      //     datetime: ""
      //   },
      //   {
      //     author: "张三",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "你好，我想知道如何使用这个功能。",
      //     datetime: ""
      //   },
      //   {
      //     author: "Jane Smith",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "请问这个功能是否免费？",
      //     datetime: ""
      //   },
      //   {
      //     author: "李四",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "非常好的助手，推荐给大家。",
      //     datetime: ""
      //   },
      //   {
      //     author: "Lucy",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "我有一个建议，希望能够添加这个功能。",
      //     datetime: ""
      //   },
      //   {
      //     author: "Mike",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "非常快速的回答，谢谢！",
      //     datetime: ""
      //   },
      //   {
      //     author: "王五",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "请问这个功能是否支持移动设备？",
      //     datetime: ""
      //   },
      //   {
      //     author: "Emily",
      //     avatar: "https://pchub.littlexi.love/avatar/fls.jpg",
      //     content: "非常喜欢这个小助手，非常实用！",
      //     datetime: ""
      //   }
      // ],
      commentvalue:"",
      submitting:false,
      username:this.$store.state.username,
    };
  },
  created(){
    if(this.$store.state.logined === false)
      this.$router.push({ name: "Signin Illustration" });
      this.page_num=0;
    this.markscore=this.$store.state.markscore;
    this.getcomment();

  },
  methods:{
    addcommentclk(){
      // console.log(this.$store.state.username);
      console.log(this.$store.state.paper);
      var para={
        user_id:this.$store.state.user.id,
        paper_id:this.$store.state.paper.id,
        content:this.commentvalue,
      }
      console.log(para)
      axios.post("http://43.143.73.132:8000/api/paper/comment",para).then((res)=>{
        if(res.status == 200)
        {
          message.success("评论成功");
          this.comments=[];
          this.page_num=0;
          this.getcomment();
        }
      })
    },
    getcomment(){
      var paper_id=this.$store.state.paper.id;
      axios.get("http://43.143.73.132:8000/api/paper/comment/"+paper_id+"/"+this.page_num+"/"+this.page_size)
      .then((res)=>{
        console.log(res);
        if(res.status == 200)
        {
          if(res.data.data.length == 0)
          {
            message.error("暂无更多消息");
            return ;
          }
          this.page_num+=1;
          // console.log(res.data.data);
          // this.comments=res.data.data;
          // console.log(this.comments)
          // this.comments = [...this.comments,];
          this.comments = this.comments.concat(res.data.data);
        }
      })
    },
    deleteComment(item){
      axios.delete("http://43.143.73.132:8000/api/paper/comment/"+item.comment_id)
      .then((res)=>{
        console.log(res);
        if(res.status == 200)
        {
          if(res.data.data.length == 0)
          {
            message.error("删除成功");
            return ;
          }
          this.comments=[];
          this.page_num = 0;
          this.getcomment();
        }
        else
        {
          message.error("删除失败");
        }
      })
    },
    submitmark(){
      axios.post("http://43.143.73.132:8000/api/paper/mark",{
        user_id:this.$store.state.user.id,
        paper_id:this.$store.state.paper.id,
        mark:this.markscore,
      })
      .then((res)=>{
        console.log(res);
        if(res.status == 200)
        {
          message.success("评分成功");
        }
        else
        {
          message.error("评分失败");
        }
      })
    }
  }
});
</script>

<style scoped>
.container {
  /* height: calc(100vh - 100px); */
  /* width: 100vh; */
  /* margin: 0; */
  /* margin-right: 0; */
  /* margin-left: 0; */
  /* position: relative; */
}
.containerpdf{
  /* overflow: hidden;  */
  width: 100%;
  /* float: left; */
}
.containercomment{
  /* width: 25vh; */
  /* height: ; */
  /* white-space: nowrap;  */
  overflow-wrap: break-word;
  /* float: left; */
}
.pdf_iframe {
width: 100%;
height: 900px;
}
</style>