<template>
  <div v-if="false" class="container-fluid py-4" >
    <div class="d-sm-flex justify-content-between">
      <div>
        <soft-button color="success" variant="gradient">New order</soft-button>
      </div>
      <div class="d-flex">
        <div class="dropdown d-inline">
          <soft-button
            id="navbarDropdownMenuLink2"
            color="dark"
            variant="outline"
            class="dropdown-toggle"
            data-bs-toggle="dropdown"
            aria-expanded="false"
            >Filters</soft-button
          >
          <ul
            class="dropdown-menu dropdown-menu-lg-start px-2 py-3"
            aria-labelledby="navbarDropdownMenuLink2"
            style
          >
            <li>
              <a class="dropdown-item border-radius-md" href="javascript:;"
                >Status: Paid</a
              >
            </li>
            <li>
              <a class="dropdown-item border-radius-md" href="javascript:;"
                >Status: Refunded</a
              >
            </li>
            <li>
              <a class="dropdown-item border-radius-md" href="javascript:;"
                >Status: Canceled</a
              >
            </li>
            <li>
              <hr class="horizontal dark my-2" />
            </li>
            <li>
              <a
                class="dropdown-item border-radius-md text-danger"
                href="javascript:;"
                >Remove Filter</a
              >
            </li>
          </ul>
        </div>
        <soft-button
          class="btn-icon ms-2 export"
          size
          color="dark"
          variant="outline"
          data-type="csv"
        >
          <span class="btn-inner--icon">
            <i class="ni ni-archive-2"></i>
          </span>
          <span class="btn-inner--text">Export CSV</span>
        </soft-button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <div class="card mt-4">
          <div class="table-responsive">
            <table id="order-list" class="table table-flush">
              <thead class="thead-light">
                <tr>
                  <th>Id</th>
                  <th>Date</th>
                  <th>Status</th>
                  <th>Customer</th>
                  <th>Product</th>
                  <th>Revenue</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10421</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">1 Nov, 10:20 AM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-avatar
                        :img="img1"
                        class="me-2"
                        size="xs"
                        alt="user image"
                        circular
                      />
                      <span>Orlando Imieto</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">Nike Sport V2</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$140,20</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10422</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">1 Nov, 10:53 AM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-avatar
                        :img="img2"
                        size="xs"
                        class="me-2"
                        alt="user image"
                        circular
                      />
                      <span>Alice Murinho</span>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">Valvet T-shirt</span>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">$42,00</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10423</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">1 Nov, 11:13 AM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="dark"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-undo" aria-hidden="true"></i>
                      </soft-button>
                      <span>Refunded</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="avatar avatar-xs me-2 bg-gradient-dark">
                        <span>M</span>
                      </div>
                      <span>Michael Mirra</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">
                      Leather Wallet
                      <span class="text-secondary ms-2">+1 more</span>
                    </span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$25,50</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10424</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">1 Nov, 12:20 PM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="d-flex align-items-center">
                        <soft-avatar
                          :img="img3"
                          size="xs"
                          class="me-2"
                          alt="user image"
                          circular
                        />
                        <span>Andrew Nichel</span>
                      </div>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">Bracelet Onu-Lino</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$19,40</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10425</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">1 Nov, 1:40 PM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="danger"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-times" aria-hidden="true"></i>
                      </soft-button>
                      <span>Canceled</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="d-flex align-items-center">
                        <soft-avatar
                          :img="img4"
                          size="xs"
                          class="me-2"
                          alt="user image"
                          circular
                        />
                        <span>Sebastian Koga</span>
                      </div>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">
                      Phone Case Pink
                      <span class="text-secondary ms-2">x 2</span>
                    </span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$44,90</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10426</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">1 Nov, 2:19 AM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="avatar avatar-xs me-2 bg-gradient-success">
                        <span>L</span>
                      </div>
                      <span>Laur Gilbert</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">Backpack Niver</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$112,50</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10427</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">1 Nov, 3:42 AM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="avatar avatar-xs me-2 bg-gradient-dark">
                        <span>I</span>
                      </div>
                      <span>Iryna Innda</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">Adidas Vio</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$200,00</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10428</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">2 Nov, 9:32 AM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="avatar avatar-xs me-2 bg-gradient-dark">
                        <span>A</span>
                      </div>
                      <span>Arrias Liunda</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">Airpods 2 Gen</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$350,00</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10429</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">2 Nov, 10:14 AM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="d-flex align-items-center">
                        <soft-avatar
                          :img="img5"
                          size="xs"
                          class="me-2"
                          alt="user image"
                          circular
                        />
                        <span>Rugna Ilpio</span>
                      </div>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">Bracelet Warret</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$15,00</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10430</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">2 Nov, 12:56 PM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="dark"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-undo" aria-hidden="true"></i>
                      </soft-button>
                      <span>Refunded</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="d-flex align-items-center">
                        <soft-avatar
                          :img="img6"
                          size="xs"
                          class="me-2"
                          alt="user image"
                          circular
                        />
                        <span>Anna Landa</span>
                      </div>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">
                      Watter Bottle India
                      <span class="text-secondary ms-2">x 3</span>
                    </span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$25,00</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10431</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">2 Nov, 3:12 PM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="avatar avatar-xs me-2 bg-gradient-dark">
                        <span>K</span>
                      </div>
                      <span>Karl Innas</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">Kitchen Gadgets</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$164,90</span>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <soft-checkbox />
                      <p class="text-xs font-weight-bold ms-2 mb-0">#10432</p>
                    </div>
                  </td>
                  <td class="font-weight-bold">
                    <span class="my-2 text-xs">2 Nov, 5:12 PM</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <soft-button
                        color="success"
                        variant="outline"
                        class="btn-icon-only btn-rounded mb-0 me-2 btn-sm d-flex align-items-center justify-content-center"
                      >
                        <i class="fas fa-check" aria-hidden="true"></i>
                      </soft-button>
                      <span>Paid</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <div class="d-flex align-items-center">
                      <div class="avatar avatar-xs me-2 bg-gradient-info">
                        <span>O</span>
                      </div>
                      <span>Oana Kilas</span>
                    </div>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">Office Papers</span>
                  </td>
                  <td class="text-xs font-weight-bold">
                    <span class="my-2 text-xs">$23,90</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>

  <a-select v-model:value="searchtype" style="width: 5%;float: left;">
    <a-select-option value="title">标题</a-select-option>
    <a-select-option value="author">作者</a-select-option>
    <a-select-option value="press">出版</a-select-option>
  </a-select>
    <a-input v-model:value="searchvalue" placeholder="请输入内容" style="width: 20%" />
  <a-button type="primary" @click="searchclk">搜索</a-button>

  <a
      class="mb-0 btn bg-gradient-success btn-sm"
      style="float: right;"
      @click="newpaperbutton()"
      >+&nbsp; 新建论文</a>

  <a-table :columns="columns" :data-source="data" :pagination="false">
    <template #name="{ text }">
      <a>{{ text }}</a>
    </template>
    <template #customTitle>
      <span>
        <smile-outlined />
        论文标题
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
          type="text"
          size="small"
          class="mb-0 btn bg-gradient-success"
          @click="showModal(record)"
        >
          详情
        </a-button>
        <!-- v-if="record.creater_id == this.$store.state.user.id" -->
        <a-button

          type="text"
          size="small"
          class="mb-0 btn bg-gradient-success"
          style="margin-left: 10px;"
          @click="editorder(record)"
        >
          编辑
        </a-button>
        <!-- v-if="record.creater_id == this.$store.state.user.id" -->
        <a-button

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

  <div class="paginationcss">
    <a-pagination v-model:current="pagenumber" show-quick-jumper :total="pagetotal" @change="onChange" />
  </div>

</template>

<script>
import { DataTable } from "simple-datatables";
import SoftButton from "@/components/SoftButton.vue";
import SoftAvatar from "@/components/SoftAvatar.vue";
import SoftCheckbox from "@/components/SoftCheckbox.vue";
import img1 from "../../../assets/img/team-2.jpg";
import img2 from "../../../assets/img/team-1.jpg";
import img3 from "../../../assets/img/team-3.jpg";
import img4 from "../../../assets/img/team-4.jpg";
import img5 from "../../../assets/img/team-5.jpg";
import img6 from "../../../assets/img/ivana-squares.jpg";
import {message} from "ant-design-vue"
import axios from "axios";

export default {
  name: "OrderList",
  components: {
    SoftButton,
    SoftAvatar,
    SoftCheckbox,
  },
  data() {
    return {
      img1,
      img2,
      img3,
      img4,
      img5,
      img6,
      pagenumber: 1,
      pagesize: 10,
      pagetotal:50,
      searchtype:'',
      searchvalue:'',
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
          title: '作者',
          dataIndex: 'author',
          key: 'author',
        },
        {
          title: '出版',
          dataIndex: 'press',
          key: 'press',
        },
        {
          title: '出版时间',
          key: 'pressdate',
          dataIndex: 'pressdate',
          slots: {
            customRender: 'pressdate',
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
          id:'',
          title:'游戏环境下的中国文化输出探索——以《原神》为例',
          library_title:0,
          creater_id:0,
          author:'刘姝秀',
          country:'中国',
          press:'中国传媒大学文化产业管理学院',
          pressdate:'2021-10-01',
          url:'https://qny.littlexi.love/FmgyW6rKjpbaA-jeCkpbLKlHgbjB'
        }
      ],
    };
  },
  created(){
    if(this.$store.state.logined === false)
      this.$router.push({ name: "Signin Illustration" });
    this.getall();
  },
  mounted() {
    if (document.getElementById("order-list")) {
      const dataTableSearch = new DataTable("#order-list", {
        searchable: true,
        fixedHeight: false,
        perPageSelect: false,
      });

      document.querySelectorAll(".export").forEach(function (el) {
        el.addEventListener("click", function (el) {
          var type = el.dataset.type;

          var data = {
            type: type,
            filename: "soft-ui-" + type,
          };

          if (type === "csv") {
            data.columnDelimiter = "|";
          }

          dataTableSearch.export(data);
        });
      });
    }
  },
  methods:{
    deleteclk(record){
      // this.visible=true;
      console.log(record)
      axios.delete('http://43.143.73.132:8000/api/paper/'+record.id)
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
              text: "你的论文已经成功删除！",
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
              text: "你的论文未被删除",
              icon: "error",
              customClass: {
                confirmButton: "btn bg-gradient-success",
              },
              buttonsStyling: false,
            });
          }
        });

    },
    newpaperbutton(){
      this.$router.push({ name: "New Paper" });
    },
    getall(){
      var params="http://43.143.73.132:8000/api/paper/"+this.$store.state.library.id+"/" +(this.pagenumber-1)+"/"+this.pagesize;
      console.log(params)
      axios.get(params).then(res=>{
        console.log(res)
        if(res.data.code === 200)
        {
          this.data = res.data.data.data;
          this.pagetotal = res.data.data.page_total;
          message.success("获取数据成功");
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
    showModal(record){
      console.log(record)
      this.addclick(record)
      this.$store.state.paper=record;
      this.$router.push({name:'Order Details'})
    },
    addclick(record)
    {
      console.log(record)
      var params="http://43.143.73.132:8000/api/paper/click/"+record.id+"/"+this.$store.state.user.id;
      console.log(params)
      axios.get(params).then(res=>{
        console.log(res)
        console.log(res.data.data.mark);       
        this.$store.state.markscore=res.data.data.mark;
      }).catch(err=>{
        console.log(err)
        // message.error(err);
      });
    },
    searchclk(){
      // console.log(this.searchtype)
      // console.log(this.searchvalue)
      if(this.searchvalue=='')
      {
        this.getall();
        return ;
      }
      var param='http://43.143.73.132:8000/api/paper/search/'+this.searchtype;
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
    },
    editorder(record){
      this.$store.state.paper=record;

      this.$router.push({name:"Modify Paper"})
    }
  }
};
</script>

<style scoped>
.paginationcss{
  display: flex;
  justify-content: center;
}
</style>