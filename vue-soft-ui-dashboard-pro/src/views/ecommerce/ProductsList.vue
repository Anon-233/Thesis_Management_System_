<template>

  <div>
    <a-select v-model:value="searchtype" style="width: 5%;float: left;">
      <a-select-option value="title">标题</a-select-option>
      <a-select-option value="topic">主题</a-select-option>
    </a-select>
      <a-input v-model:value="searchvalue" placeholder="Basic usage" style="width: 20%" />
    <a-button type="primary" @click="searchclk">搜索</a-button>

    <a
      href="./new-product"
      class="mb-0 btn bg-gradient-success btn-sm"
      style="float: right"
      >+&nbsp; 新建文献库</a
    >
  <a-table :columns="columns" :data-source="data" :pagination="false">


    <!-- <template #name="{ text }">
      <a>{{ text }}</a>
    </template> -->
    <template #customTitle>
      <span>
        <smile-outlined />
        文献库名称
      </span>
    </template>
    <template #tags="{ text: tags }">
      <span>
        <a-tag
          v-for="tag in tags"
          :key="tag"
          :color="green"
        >
          {{ tag.toUpperCase() }}
        </a-tag>
      </span>
    </template>
    <template #action="{ record }">
      <span>
        <a-button
          v-if="record.is_public||(record.creater_id == this.$store.state.user.id)"
          type="text"
          size="small"
          class="mb-0 btn bg-gradient-success"
          @click="jumptopapers(record)"
        >
          详情
        </a-button>
        <a-button
          v-if="record.creater_id == this.$store.state.user.id"
          type="text"
          size="small"
          class="mb-0 btn bg-gradient-success"
          style="margin-left: 5px;"
          @click="modifyclick(record)"
        >
          编辑
        </a-button>
        <a-button
          v-if="record.creater_id == this.$store.state.user.id"
          type="text"
          size="small"
          class="mb-0 btn bg-gradient-success"
          style="margin-left: 5px;"
          @click="showSwal(record)"
        >
          删除
      </a-button>
      </span>
    </template>
  </a-table>

  <!-- 修改弹窗 -->
  <div>
    <a-modal
      v-model:visible="visible"
      title="Title"
      mask=false
      ok-text="修改"
      cancel-text="取消"
      :confirm-loading="confirmLoading"
      @ok="handleOk"
    >
      <p>{{ modalText }}</p>
    </a-modal>
  </div>

  <div class="paginationcss">
    <a-pagination v-model:current="pagenumber" show-quick-jumper :total="pagetotal" @change="onChange" />
  </div>

  </div>
</template>

<script>
// import { DataTable } from "simple-datatables";
// import setTooltip from "@/assets/js/tooltip.js";
import axios from 'axios';
import { ref, defineComponent } from 'vue';
import {message} from 'ant-design-vue';
export default defineComponent({
  name: "ProductsList",
  setup() {
    const modalText = ref('Content of the modal');
    const visible = ref(false);
    const confirmLoading = ref(false);
    const showModal = () => {
      console.log(visible.value)
      visible.value = true;
    };
    const handleOk = () => {
      modalText.value = 'The modal will be closed after two seconds';
      confirmLoading.value = true;
      setTimeout(() => {
        visible.value = false;
        confirmLoading.value = false;
      }, 2000);
    };
    return {
      modalText,
      visible,
      confirmLoading,
      showModal,
      handleOk,
    };
  },
  data(){
    return{
      pagenumber: 1,
      pagesize: 10,
      pagetotal:50,
      loading: false,
      searchtype: "",
      searchvalue: "",
      columns : [
        {
          dataIndex: 'title',
          key: 'title',
          slots: {
            title: 'customTitle',
            customRender: 'title',
          },
        },
        {
          title: '主题',
          dataIndex: 'topic',
          key: 'topic',
        },
        {
          title: '文章数量',
          dataIndex: 'papernumber',
          key: 'papernumber',
        },
        {
          title: '热度',
          key: 'clicktime',
          dataIndex: 'clicktime',
          slots: {
            customRender: 'clicktime',
          },
        },
        {
          title: '操作',
          key: 'action',
          slots: {
            customRender: 'action',
          },
        },
      ],
      data:[
        {
            "certificate": null,
            "clicktime": 0,
            "creater_id": 1066771571,
            "description": null,
            "id": 1,
            "is_public": false,
            "orgnization_name": null,
            "orgnization_type": null,
            "orgnization_url": null,
            "papernumber": 0,
            "title": "ababa",
            "topic": "impart"
        }
      ],
    }
  },
  // mounted() {
  //   if (document.getElementById("products-list")) {
  //     const dataTableSearch = new DataTable("#products-list", {
  //       searchable: true,
  //       fixedHeight: false,
  //       perPage: 7
  //     });

  //     document.querySelectorAll(".export").forEach(function (el) {
  //       el.addEventListener("click", function () {
  //         var type = el.dataset.type;

  //         var data = {
  //           type: type,
  //           filename: "soft-ui-" + type
  //         };

  //         if (type === "csv") {
  //           data.columnDelimiter = "|";
  //         }

  //         dataTableSearch.export(data);
  //       });
  //     });
  //   }
  //   setTooltip(this.$store.state.bootstrap);
  // },
  created(){
    if(this.$store.state.logined === false)
      this.$router.push({ name: "Signin Illustration" });
      this.getall();
  },
  methods: {
    deleteclk(record){
      // this.visible=true;
      console.log(record)
      axios.delete('http://43.143.73.132:8000/api/library/'+record.id)
        .then(resp=>{
          if(resp.status === 200)
          {
            message.success("删除成功");
            this.getall();
          }
          else
            message.error("删除失败")
        }).catch(err=>{
          console.log(err)
          message.error("删除失败")
        })
    },
    showSwal(record){
      // this.$store.state.showSidenav=false;
      this.$swal({
          title: "确定删除吗?",
          text: "删除操作将无法撤销!",
          showCancelButton: true,
          confirmButtonText: "删除",
          cancelButtonText: "取消",
          reverseButtons: true,
          customClass: {
            confirmButton: "btn bg-gradient-success",
            cancelButton: "btn bg-gradient-danger",
          },
          buttonsStyling: false,
        }).then((result) => {
          // this.$store.state.showSidenav=true;
          if (result.isConfirmed) {

            // 这里可以发送删除的axios请求
            this.deleteclk(record);
            this.$swal({
              title: "删除成功!",
              text: "你的文献库已经成功删除！",
              icon: "success",
              customClass: {
                confirmButton: "btn bg-gradient-success",
              },
              buttonsStyling: false,
            });
          } else if (
            /* Read more about handling dismissals below */
            result.dismiss === this.$swal.DismissReason.cancel
          ) {
            this.$swal({
              title: "取消!",
              text: "你的文献库未被删除",
              icon: "error",
              customClass: {
                confirmButton: "btn bg-gradient-success",
              },
              buttonsStyling: false,
            });
          }
        });

    },
    getall(){
      var params="http://43.143.73.132:8000/api/library/"+(this.pagenumber-1)+'/'+this.pagesize;
      console.log(params)
      axios.get(params).then(res=>{
        console.log(res)
        if(res.data.code === 200)
        {
          this.data = res.data.data.data;
          this.pagetotal = res.data.data.page_total;
          // message.success("获取数据成功");
        }
        else
        {
          message.error("获取数据失败");
        }
      }).catch(err=>{
        console.log(err)
        // message.error(err);
      });
    },
    onChange(){
      console.log(1)
      this.getall();
    },
    modifyclick(record){
      console.log(record)
      this.$store.state.library = record;
      //跳转路由
      this.$router.push({ name: "Edit Product" });
    },
    jumptopapers(record){
      this.$store.state.library = record;
      this.$router.push({ name: "Order List" });
    },
    searchclk(){
      // console.log(this.searchtype)
      // console.log(this.searchvalue)
      if(this.searchvalue=='')
      {
        this.getall();
        return ;
      }
      var param='http://43.143.73.132:8000/api/library/search/'+this.searchtype;
      axios.post(param,{
        value:this.searchvalue,
        page_num:this.pagenumber-1,
        page_size:this.pagesize
      }).then(res=>{
        console.log(res)
        if(res.data.code === 200)
        {
          this.data = res.data.data.data;
          this.pagetotal = res.data.data.page_total;
          // message.success("获取数据成功");
        }
        else
        {
          message.error("获取数据失败");
        }
      }).catch(err=>{
        console.log(err)
        // message.error(err);
      });
    }
  },
});
</script>


<style scoped> 
.paginationcss{
  display: flex;
  justify-content: center;
}
</style>