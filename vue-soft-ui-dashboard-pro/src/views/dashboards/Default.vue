<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-7 position-relative z-index-2">
        <div class="mb-4 card card-plain">
          <div class="p-3 card-body">
            <div class="row">
              <div class="col-lg-6">
                <div class="d-flex flex-column h-100">
                  
                  <h2 class="mb-0 font-weight-bolder">文献库数据</h2>
                  <a-cascader :options="options" placeholder="Please select" @change="onChange" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-5 col-sm-5">
            <mini-statistics-card
              title="用户数量"
              :value=this.$store.state.user_total
              :percentage="{
                value: '+55%',
                color: 'text-success',
              }"
              :icon="{
                component: 'ni ni-money-coins',
                background: iconBackground,
              }"
              direction-reverse
            />
            <mini-statistics-card
              title="文献库数量"
              :value=this.$store.state.library_total
              :percentage="{
                value: '+3%',
                color: 'text-success',
              }"
              :icon="{
                component: 'ni ni-world',
                background: iconBackground,
              }"
              direction-reverse
            />
          </div>
          <div class="mt-4 col-lg-5 col-sm-5 mt-sm-0">
            <mini-statistics-card
              title="论文数量"
              :value=this.$store.state.paper_total
              :percentage="{
                value: '-2%',
                color: 'text-danger',
              }"
              :icon="{
                component: 'ni ni-paper-diploma',
                background: iconBackground,
              }"
              direction-reverse
            />

            <mini-statistics-card
              title="论文阅读量"
              :value=this.$store.state.click_total
              :percentage="{
                value: '+5%',
                color: 'text-success',
              }"
              :icon="{
                component: 'ni ni-cart',
                background: iconBackground,
              }"
              direction-reverse
            />
          </div>
        </div>
        <!-- <div class="row">
          <sales-table
            title="公告栏"
            :rows=hotpapers
          />
        </div> -->
        <h3> 公告栏 </h3>
        <a-button v-if="this.$store.state.user.username == 'admin'" type="primary" @click="newnoticeclk">{{ newsubstyle }}</a-button>
        <a-form-item v-if="newshow" label="标题" style="width: 60%;">
          <a-form-item name="input-number" no-style>
            <!-- <a-input v-model="formState.author"/> -->
            <input
              v-model=title
              class="form-control"
              type="text"
              placeholder=""
            />
          </a-form-item>
        </a-form-item>
        <a-form-item v-if="newshow" label="内容" style="width: 60%;">
          <a-form-item name="input-number" no-style>
            <!-- <a-input v-model="formState.author"/> -->
            <input
              v-model=content
              class="form-control"
              type="text"
              placeholder=""
            />
          </a-form-item>
        </a-form-item>
        
        <!-- <a-button v-if="'admin' == this.$store.state.user.username" type="dashed" size="small" danger @click="newnoticeclk">新建</a-button> -->
        <a-list item-layout="horizontal" :data-source="notices" style="width: 60%;">
          <template #renderItem="{ item }">
            <a-list-item>
              <a-list-item-meta
                :description=item.content
              >
                <template #title>
                  <a href="https://www.antdv.com/">{{ item.title }} {{ item.time }}</a>
                </template>
                <template #avatar>
                  <a-avatar src="https://qny.littlexi.love/FhIybVlG_S0pd5zHY8Xye1LtLWpF" />
                </template>
              </a-list-item-meta>
            </a-list-item>
          </template>
        </a-list>

      </div>
    </div>
    <div  class="mt-4 row" >
      <div class="mb-4 col-lg-5 mb-lg-0">
        <div v-if="false" class="card z-index-2">
          <div class="p-3 card-body">
            <!-- <reports-bar-chart
              id="chart-bar"
              title="用户活跃度"
              description="(<strong>+23%</strong>) than last week"
              :chart="{
                labels: [
                  'Apr',
                  'May',
                  'Jun',
                  'Jul',
                  'Aug',
                  'Sep',
                  'Oct',
                  'Nov',
                  'Dec',
                ],
                datasets: {
                  label: 'Sales',
                  data: [40, 200, 100, 220, 500, 100, 400, 230, 500],
                },
              }"
              :items="[
                {
                  icon: {
                    color: 'primary',
                    component: faUsers,
                  },
                  label: 'users',
                  progress: { content: '37K', percentage: 60 },
                },
                {
                  icon: { color: 'info', component: faHandPointer },
                  label: 'clicks',
                  progress: { content: '2m', percentage: 90 },
                },
                {
                  icon: { color: 'warning', component: faCreditCard },
                  label: 'Sales',
                  progress: { content: '435$', percentage: 30 },
                },
                {
                  icon: { color: 'danger', component: faScrewdriverWrench },
                  label: 'Items',
                  progress: { content: '43', percentage: 50 },
                },
              ]"
            >
            </reports-bar-chart> -->
          </div>
        </div>
      </div>
      <div class="col-lg-7">
        <!-- line chart -->
        <div class="card z-index-2">
          <gradient-line-chart
            id="chart-line"
            title="Gradient Line Chart"
            description="<i class='fa fa-arrow-up text-success'></i>
      <span class='font-weight-bold'>4% more</span> in 2021"
            :chart="{
              labels: [
                'Apr',
                'May',
                'Jun',
                'Jul',
                'Aug',
                'Sep',
                'Oct',
                'Nov',
                'Dec',
              ],
              datasets: [
                {
                  label: 'Mobile Apps',
                  data: [500, 40, 300, 220, 500, 250, 400, 230, 500],
                },
                {
                  label: 'Websites',
                  data: [300, 90, 40, 140, 290, 290, 340, 230, 400],
                },
              ],
            }"
          />
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-12">
        <!-- globe -->
        <globe width="700" height="600" />
      </div>
    </div>
  </div>
</template>
<script>
import MiniStatisticsCard from "../../examples/Cards/MiniStatisticsCard.vue";
// import ReportsBarChart from "../../examples/Charts/ReportsBarChart.vue";
import GradientLineChart from "../../examples/Charts/GradientLineChart.vue";
// import SalesTable from "./components/SalesTable.vue";
import US from "@/assets/img/icons/flags/US.png";
import DE from "@/assets/img/icons/flags/DE.png";
import GB from "@/assets/img/icons/flags/GB.png";
import BR from "@/assets/img/icons/flags/BR.png";
import { message } from "ant-design-vue";
import axios from "axios";

import Globe from "../../examples/Globe.vue";
import {
  faHandPointer,
  faUsers,
  faCreditCard,
  faScrewdriverWrench,
} from "@fortawesome/free-solid-svg-icons";

export default {
  name: "DashboardDefault",
  components: {
    MiniStatisticsCard,
    // ReportsBarChart,
    GradientLineChart,
    // SalesTable,
    Globe,
  },
  data() {
    return {
      faHandPointer,
      faUsers,
      faCreditCard,
      faScrewdriverWrench,
      iconBackground: "bg-gradient-success",
      US,
      DE,
      BR,
      GB,
      newshow:false,
      title:'',
      content:'',
      newsubstyle:'新建',
      notices:[
        {
          id:1,
          sender_id:1,
          content:"佛奥佛奥佛佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥佛奥奥佛奥佛奥佛奥",
          time:"2021-01-02",
          title:"电话",
        },
        {
          id:1,
          sender_id:1,
          content:"佛奥",
          time:"2021-01-02",
          title:"电话",
        }
      ],
      hotpapers:[
        {
          papertitle:'三体三体三体三三体三三体三',
          author: '250570',
          publisher: '$230,900',
          bounce: '29.9%',
        },
        {
          papertitle:'三体',

          author: '3.900',
          publisher: '$440,000',
          bounce: '40.22%',
        },
        {
          papertitle:'三体',

          author: '1.400',
          publisher: '$190,700',
          bounce: '23.44%',
        },
        {
          papertitle:'三体2',

          author: '52262',
          publisher: '$143,960',
          bounce: '32.14%',
        },
      ]
    };
  },
  created(){
    if(this.$store.state.logined === false)
      this.$router.push({ name: "Signin Illustration" });
    this.getnotices();
    axios.post('http://43.143.73.132:8000/api/user/token',
    {token:this.$store.state.user.token}
    )
    .then(res=>{
      console.log(res);
        if (res.data.code == 200) {
          this.$store.state.logined = true;
          this.$store.state.click_total = res.data.data.click_total;
          this.$store.state.library_total = res.data.data.library_total;
          this.$store.state.paper_total = res.data.data.paper_total;
          this.$store.state.user_total = res.data.data.user_total;
          this.$store.state.user = res.data.data.user_info;
          message.success("查询成功");
          // this.$router.push({ name: "Default" });
        } else {
          message.error("查询失败");
        }
    })
  },
  methods:{
    getnotices(){
    axios.get('http://43.143.73.132:8000/api/notice/')
    .then(res=>{
      console.log(res);
        if (res.data.code == 200) {
          this.notices = res.data.data;
          // message.error("查询失败");
        } else {
          message.error("查询失败");
        }
    })
    },
    newnoticeclk(){
      if(this.newshow==false)
      {
        this.newshow=true;
        this.newsubstyle='提交'
        return;
      }
      axios.post('http://43.143.73.132:8000/api/notice/',
      {
        user_id:this.$store.state.user.id,
        title:this.title,
        content:this.content,
      }
      )
      .then(res=>{
        console.log(res);
          if (res.data.code == 200) {
            // this.notices = res.data.data;
            this.getnotices();
            this.newshow=false;
            this.newsubstyle='新建';
            message.success("新建成功");
          } else {
            message.error("查询失败");
          }
      })
    }
  }

};
</script>
