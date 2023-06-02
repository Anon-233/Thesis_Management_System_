<template>
  <div id="profile" class="card card-body mt-4">
    <div class="row justify-content-center align-items-center">
      <div class="col-sm-auto col-4">
        <soft-avatar
          :img="img"
          alt="bruce"
          size="xl"
          shadow="sm"
          border-radius="lg"
        />
      </div>
      <div class="col-sm-auto col-8 my-auto">
        <div class="h-100">
          <h5 class="mb-1 font-weight-bolder">{{ user.username }}</h5>
          <p class="mb-0 font-weight-bold text-sm">电话号码 : {{ user.phone==""?"未设置":user.phone }}</p>
        </div>
      </div>
      <div class="col-sm-auto ms-sm-auto mt-sm-0 mt-3 d-flex">
        <label class="form-check-label mb-0 me-2">
          <!-- <small id="profileVisibility">Switch to invisible</small> -->
        </label>
        <!-- <soft-switch id="profile" name="profileVisibility" checked /> -->
      </div>
    </div>
  </div>
  <div id="basic-info" class="card mt-4">
    <div class="card-header">
      <h5>基本信息</h5>
    </div>
    <div class="card-body pt-0">
      <div class="row">
        <div class="col-6">
          <label class="form-label">名</label>
          <a-input v-model:value="user.firstname" />
        </div>
        <div class="col-6">
          <label class="form-label">姓</label>
          <a-input v-model:value="user.lastname" />
      </div>
    </div>

    <div class="row">
      <h5>修改头像</h5>
    </div>
    <div class="col-6">
      <input id="inputField" name="inputField" type="file" placeholder="ds" @change="handleFileUpload">
    </div>

      <div class="row">
        <!-- <div class="col-sm-4 col-6">
          <label class="form-label mt-2">I'm</label>
          <select
            id="choices-gender"
            class="form-control"
            name="choices-gender"
          >
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div> -->
        <div class="col-sm-8">
          <div class="row">
            <div class="col-sm-5 col-5">
              <label class="form-label mt-2">出生日期</label>
              <a-input v-model:value="user.birth" />
              <!-- <select
                id="choices-month"
                class="form-control"
                name="choices-month"
              ></select> -->
            </div>
            <!-- <div class="col-sm-4 col-3">
              <label class="form-label mt-2">&nbsp;</label>
              <select
                id="choices-day"
                class="form-control"
                name="choices-day"
              ></select>
            </div>
            <div class="col-sm-3 col-4">
              <label class="form-label mt-2">&nbsp;</label>
              <select
                id="choices-year"
                class="form-control"
                name="choices-year"
              ></select>
            </div> -->
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-6">
          <label class="form-label mt-2">邮箱</label>
          <a-input v-model:value="user.email" />
        </div>
        <!-- <div class="col-6">
          <label class="form-label mt-2">Confirmation Email</label>
          <soft-input
            id="confirmEmail"
            type="email"
            placeholder="example@email.com"
          />
        </div> -->
      </div>
      <div class="row">
        <div class="col-6">
          <label class="form-label mt-2">地址</label>
          <a-input v-model:value="user.location" />
        </div>
        <div class="col-6">
          <label class="form-label mt-2">联系电话</label>
          <a-input v-model:value="user.phone" />
        </div>
      </div>
      <!-- <div class="row">
        <div class="col-md-6 align-self-center">
          <label class="form-label mt-2">Language</label>
          <select
            id="choices-language"
            class="form-control"
            name="choices-language"
          >
            <option value="English">English</option>
            <option value="French">French</option>
            <option value="Spanish">Spanish</option>
          </select>
        </div>
        <div class="col-md-6">
          <label class="form-label mt-2">Skills</label>
          <input
            id="choices-skills"
            class="form-control"
            type="text"
            value="vuejs, angular, react"
            placeholder="Enter something"
            onfocus="focused(this)"
            onfocusout="defocused(this)"
          />
        </div>
      </div> -->
      <!-- <div class="row"> -->
        <a-button type="primary" style="float: right; margin-top: 10px;" @click="changebasicinfosubmitclk">修改信息</a-button>
      <!-- </div> -->
    </div>
  </div>
  <div id="password" class="card mt-4">
    <div class="card-header">
      <h5>修改密码</h5>
    </div>
    <div class="card-body pt-0">
      <label class="form-label">当前密码</label>

      <a-input v-model:value="currentpassword" type="password" />
      <!-- <a-input
        id="currentPassword"
        v-model="currentpassword"

        type="password"
        placeholder="Current Password"
      /> -->
      <label class="form-label">新密码</label>
      <a-input v-model:value="password1" type="password"/>
      <!-- <a-input id="newPassword" v-model="password1"  type="password" placeholder="New Password" /> -->
      <label class="form-label">确定新密码</label>
      <a-input v-model:value="password2"   type="password" />
      <!-- <a-input
        id="confirmPassword"
        v-model="password2"

        type="password"
        placeholder="Confirm password"
      /> -->
      <a-button type="primary" style="float: right; margin-top: 10px;" @click="changepasswordsubmitclk">修改密码</a-button>
    </div>
  </div>
  <!-- <div id="2fa" class="card mt-4">
    <div class="card-header d-flex">
      <h5 class="mb-0">Two-factor authentication</h5>
      <soft-badge color="success" class="ms-auto">Enabled</soft-badge>
    </div>
    <div class="card-body">
      <div class="d-flex">
        <p class="my-auto">Security keys</p>
        <p class="text-secondary text-sm ms-auto my-auto me-3">
          No Security Keys
        </p>
        <soft-button
          color="dark"
          variant="outline"
          size="sm"
          class="mb-0"
          type="button"
          >Add</soft-button
        >
      </div>
      <hr class="horizontal dark" />
      <div class="d-flex">
        <p class="my-auto">SMS number</p>
        <p class="text-secondary text-sm ms-auto my-auto me-3">+4012374423</p>
        <soft-button
          color="dark"
          variant="outline"
          size="sm"
          class="mb-0"
          type="button"
          >Edit</soft-button
        >
      </div>
      <hr class="horizontal dark" />
      <div class="d-flex">
        <p class="my-auto">Authenticator app</p>
        <p class="text-secondary text-sm ms-auto my-auto me-3">
          Not Configured
        </p>
        <soft-button
          color="dark"
          variant="outline"
          size="sm"
          class="mb-0"
          type="button"
          >Set up</soft-button
        >
      </div>
    </div>
  </div>
  <div id="accounts" class="card mt-4">
    <div class="card-header">
      <h5>Accounts</h5>
      <p class="text-sm">
        Here you can setup and manage your integration settings.
      </p>
    </div>
    <div class="card-body pt-0">
      <div class="d-flex">
        <soft-avatar class="width-48-px" :img="img1" alt="logo_slack" />
        <div class="my-auto ms-3">
          <div class="h-100">
            <h5 class="mb-0">Slack</h5>
            <a class="text-sm text-body" href="javascript:;">
              Show less
              <i class="fas fa-chevron-up text-xs ms-1" aria-hidden="true"></i>
            </a>
          </div>
        </div>
        <p class="text-sm text-secondary ms-auto me-3 my-auto">Enabled</p>
        <div class="my-auto">
          <soft-switch id="slack" name="showMore" checked />
        </div>
      </div>
      <div class="ps-5 pt-3 ms-3">
        <p class="mb-0 text-sm">
          You haven't added your Slack yet or you aren't authorized. Please add
          our Slack Bot to your account by clicking on
          <a href="javascript">here</a>. When you've added the bot, send your
          verification code that you have received.
        </p>
        <div
          class="d-sm-flex align-items-center bg-gray-100 border-radius-lg p-2 my-4"
        >
          <p class="text-sm font-weight-bold my-auto ps-sm-2">
            Verification Code
          </p>
          <soft-input
            type="text"
            value="1172913"
            class="my-auto w-20 ms-sm-auto"
          />
        </div>
        <div class="d-sm-flex bg-gray-100 border-radius-lg p-2 my-4">
          <p class="text-sm font-weight-bold my-auto ps-sm-2">
            Connected account
          </p>
          <h6 class="text-sm ms-auto me-3 my-auto">hello@creative-tim.com</h6>
          <soft-button
            color="danger"
            variant="gradient"
            size="sm"
            class="my-sm-auto mt-2 mb-0"
            type="button"
            name="button"
            >Delete</soft-button
          >
        </div>
      </div>
      <hr class="horizontal dark" />
      <div class="d-flex">
        <soft-avatar class="width-48-px" :img="img2" alt="logo_spotify" />
        <div class="my-auto ms-3">
          <div class="h-100">
            <h5 class="mb-0">Spotify</h5>
            <p class="mb-0 text-sm">Music</p>
          </div>
        </div>
        <p class="text-sm text-secondary ms-auto me-3 my-auto">Enabled</p>
        <div class="my-auto">
          <soft-switch id="spotify" name="show" checked />
        </div>
      </div>
      <hr class="horizontal dark" />
      <div class="d-flex">
        <soft-avatar class="width-48-px" :img="img3" alt="logo_atlassian" />
        <div class="my-auto ms-3">
          <div class="h-100">
            <h5 class="mb-0">Atlassian</h5>
            <p class="mb-0 text-sm">Payment vendor</p>
          </div>
        </div>
        <p class="text-sm text-secondary ms-auto me-3 my-auto">Enabled</p>
        <div class="my-auto">
          <soft-switch id="atlassian" name="showMore2" checked />
        </div>
      </div>
      <hr class="horizontal dark" />
      <div class="d-flex">
        <soft-avatar class="width-48-px" :img="img4" alt="logo_asana" />
        <div class="my-auto ms-3">
          <div class="h-100">
            <h5 class="mb-0">Asana</h5>
            <p class="mb-0 text-sm">Organize your team</p>
          </div>
        </div>
        <div class="my-auto ms-auto">
          <soft-switch id="Asana" name="showMore3" />
        </div>
      </div>
    </div>
  </div>
  <div id="notifications" class="card mt-4">
    <div class="card-header">
      <h5>Notifications</h5>
      <p class="text-sm">
        Choose how you receive notifications. These notification settings apply
        to the things you’re watching.
      </p>
    </div>
    <div class="card-body pt-0">
      <div class="table-responsive">
        <table class="table mb-0">
          <thead>
            <tr>
              <th class="ps-1" colspan="4">
                <p class="mb-0">Activity</p>
              </th>
              <th class="text-center">
                <p class="mb-0">Email</p>
              </th>
              <th class="text-center">
                <p class="mb-0">Push</p>
              </th>
              <th class="text-center">
                <p class="mb-0">SMS</p>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="ps-1" colspan="4">
                <div class="my-auto">
                  <span class="text-dark d-block text-sm">Mentions</span>
                  <span class="text-xs font-weight-normal"
                    >Notify when another user mentions you in a comment</span
                  >
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch
                    id="mentionsEmail"
                    name="mentionsEmail"
                    checked
                  />
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="mentionsPush" name="mentionsPush" />
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="mentionsSms" name="mentionsSms" />
                </div>
              </td>
            </tr>
            <tr>
              <td class="ps-1" colspan="4">
                <div class="my-auto">
                  <span class="text-dark d-block text-sm">Comments</span>
                  <span class="text-xs font-weight-normal"
                    >Notify when another user comments your item.</span
                  >
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch
                    id="commentsEmail"
                    name="commentsEmail"
                    checked
                  />
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="commentsPush" name="commentsPush" checked />
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="commentsSms" name="commentsSms" />
                </div>
              </td>
            </tr>
            <tr>
              <td class="ps-1" colspan="4">
                <div class="my-auto">
                  <span class="text-dark d-block text-sm">Follows</span>
                  <span class="text-xs font-weight-normal"
                    >Notify when another user follows you.</span
                  >
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="followsEmail" name="followsEmail" checked />
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="followsEmail" name="followsPush" checked />
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="followsEmail" name="followsSms" checked />
                </div>
              </td>
            </tr>
            <tr>
              <td class="ps-1" colspan="4">
                <div class="my-auto">
                  <p class="text-sm mb-0">Log in from a new device</p>
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="deviceEmail" name="deviceEmail" checked />
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="devicePush" name="devicePush" checked />
                </div>
              </td>
              <td>
                <div class="ms-auto">
                  <soft-switch id="deviceSms" name="deviceSms" checked />
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div id="sessions" class="card mt-4">
    <div class="card-header pb-3">
      <h5>Sessions</h5>
      <p class="text-sm">
        This is a list of devices that have logged into your account. Remove
        those that you do not recognize.
      </p>
    </div>
    <div class="card-body pt-0">
      <div class="d-flex align-items-center">
        <div class="text-center w-5">
          <i class="fas fa-desktop text-lg opacity-6"></i>
        </div>
        <div class="my-auto ms-3">
          <div class="h-100">
            <p class="text-sm mb-1">Bucharest 68.133.163.201</p>
            <p class="mb-0 text-xs">Your current session</p>
          </div>
        </div>
        <soft-badge color="success" size="sm" class="my-auto ms-auto me-3"
          >Active</soft-badge
        >
        <p class="text-secondary text-sm my-auto me-3">EU</p>
        <a
          href="javascript:;"
          class="text-primary text-sm icon-move-right my-auto"
        >
          See more
          <i class="fas fa-arrow-right text-xs ms-1" aria-hidden="true"></i>
        </a>
      </div>
      <hr class="horizontal dark" />
      <div class="d-flex align-items-center">
        <div class="text-center w-5">
          <i class="fas fa-desktop text-lg opacity-6"></i>
        </div>
        <p class="my-auto ms-3">Chrome on macOS</p>
        <p class="text-secondary text-sm ms-auto my-auto me-3">US</p>
        <a
          href="javascript:;"
          class="text-primary text-sm icon-move-right my-auto"
        >
          See more
          <i class="fas fa-arrow-right text-xs ms-1" aria-hidden="true"></i>
        </a>
      </div>
      <hr class="horizontal dark" />
      <div class="d-flex align-items-center">
        <div class="text-center w-5">
          <i class="fas fa-mobile text-lg opacity-6"></i>
        </div>
        <p class="my-auto ms-3">Safari on iPhone</p>
        <p class="text-secondary text-sm ms-auto my-auto me-3">US</p>
        <a
          href="javascript:;"
          class="text-primary text-sm icon-move-right my-auto"
        >
          See more
          <i class="fas fa-arrow-right text-xs ms-1" aria-hidden="true"></i>
        </a>
      </div>
    </div>
  </div> -->
  <div id="delete" class="card mt-4">
    <div class="card-header">
      <h5>注销账户</h5>
      <p class="text-sm mb-0">
        一旦你注销账户，无法恢复，请考虑清楚
      </p>
    </div>
    <div class="card-body d-sm-flex pt-0">
      <div class="d-flex align-items-center mb-sm-0 mb-4">
        <div>
          <soft-switch id="deleteAccount" name="deleteAccount" />
        </div>
        <div class="ms-2">
          <span class="text-dark font-weight-bold d-block text-sm"
            >Confirm</span
          >
          <span class="text-xs d-block" >我想要注销账户</span>
        </div>
        
      </div>
      <a-button type="primary" style="float: right; margin:10px 0 0 70vh;" danger @click="deleteaccountclk">注销账户</a-button>
    </div>
  </div>
</template>

<script>
import * as Choices from "choices.js";
// import SoftButton from "@/components/SoftButton.vue";
import SoftSwitch from "@/components/SoftSwitch.vue";
// import SoftBadge from "@/components/SoftBadge.vue";
import SoftAvatar from "@/components/SoftAvatar.vue";
// import SoftInput from "@/components/SoftInput.vue";
// import img from "../../../../assets/img/bruce-mars.jpg";
import img1 from "../../../../assets/img/small-logos/logo-slack.svg";
import img2 from "../../../../assets/img/small-logos/logo-spotify.svg";
import img3 from "../../../../assets/img/small-logos/logo-atlassian.svg";
import img4 from "../../../../assets/img/small-logos/logo-asana.svg";
import message from "ant-design-vue/es/message";
import axios from "axios";

export default {
  name: "SideNavItem",
  components: {
    // SoftButton,
    SoftSwitch,
    // SoftBadge,
    SoftAvatar,
    // SoftInput,
  },
  data() {
    return {
      img:this.$store.state.user.avatar,
      img1,
      img2,
      img3,
      img4,
      user:this.$store.state.user,
      currentpassword:'',
      password1:'',
      password2:'',
      uploadUrl: 'https://upload.qiniup.com',
      file:null,
      token:this.$store.state.token,
    };
  },
  created(){
    if(this.$store.state.logined === false)
      this.$router.push({ name: "Signin Illustration" });
  },
  mounted() {
    if (document.getElementById("choices-gender")) {
      var gender = document.getElementById("choices-gender");
      new Choices(gender);
    }

    if (document.getElementById("choices-language")) {
      var language = document.getElementById("choices-language");
      new Choices(language);
    }

    if (document.getElementById("choices-month")) {
      var month = document.getElementById("choices-month");
      setTimeout(function () {
        new Choices(month);
      }, 1);

      // eslint-disable-next-line no-unused-vars
      var d = new Date();
      var monthArray = new Array();
      monthArray[0] = "January";
      monthArray[1] = "February";
      monthArray[2] = "March";
      monthArray[3] = "April";
      monthArray[4] = "May";
      monthArray[5] = "June";
      monthArray[6] = "July";
      monthArray[7] = "August";
      monthArray[8] = "September";
      monthArray[9] = "October";
      monthArray[10] = "November";
      monthArray[11] = "December";
      for (let m = 0; m <= 11; m++) {
        var optn = document.createElement("OPTION");
        optn.text = monthArray[m];
        // server side month start from one\
        optn.value = m + 1;
        // if june selected
        if (m == 1) {
          optn.selected = true;
        }
        month.options.add(optn);
      }
    }

    if (document.getElementById("choices-day")) {
      var day = document.getElementById("choices-day");
      setTimeout(function () {
        new Choices(day);
      }, 1);

      for (let y = 1; y <= 31; y++) {
        var optn1 = document.createElement("OPTION");
        optn1.text = y;
        optn1.value = y;

        if (y == 1) {
          optn1.selected = true;
        }

        day.options.add(optn1);
      }
    }

    if (document.getElementById("choices-year")) {
      var year = document.getElementById("choices-year");
      setTimeout(function () {
        new Choices(year);
      }, 1);

      for (let y = 1900; y <= 2020; y++) {
        var optn2 = document.createElement("OPTION");
        optn2.text = y;
        optn2.value = y;

        if (y == 2020) {
          optn.selected = true;
        }

        year.options.add(optn2);
      }
    }

    if (document.getElementById("choices-skills")) {
      var skills = document.getElementById("choices-skills");
      new Choices(skills, {
        delimiter: ",",
        editItems: true,
        maxItemCount: 5,
        removeItemButton: true,
        addItems: true,
      });
    }
  },
  methods:{
    handleFileUpload(event) {
      console.log(event)
      this.file = event.target.files[0];
      console.log(this.file)
      this.uploadFile();
    },
    uploadFile() {
      const formData = new FormData();
      formData.append('file', this.file);
      formData.append('token', this.token);
      console.log("uploading")
      
      axios
        .post(this.uploadUrl, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then(response => {
          // console.log
          console.log(response);
          message.success("文件上传成功");
          this.$store.state.user.avatar = "https://qny.littlexi.love/"+response.data.key;
          console.log('文件上传成功', response.data);
        })
        .catch(error => {
          console.error('文件上传失败', error);
        });
    },
    changebasicinfosubmitclk(){
      console.log(1)
      console.log(this.user);
      axios.put("http://43.143.73.132:8000/api/user/modify",this.user)
      .then(resp=>{
        if(resp.status == 200)
        {
          message.success('修改成功');
        }
        else
        {
          message.error('修改失败');
        }
      })
    },
    changepasswordsubmitclk(){
      // if(this.)
      // console.log(this.currentpassword);
      // console.log(this.password1);
      // console.log(this.password2);
      if(this.password1!=this.password2)
      {
        message.error("两次密码不一致");
        return;
      }
      axios.put("http://43.143.73.132:8000/api/user/change",
      {
        id:this.$store.state.user.id,
        oldpassword:this.currentpassword,
        newpassword:this.password1,
      }
      )
      .then(resp=>{
        if(resp.status == 200)
        {
          message.success('修改成功');
          this.$router.push({name:'Signin Illustration'});
        }
        else
        {
          message.error('修改失败');
        }
      }).catch(err=>{
        console.log(err);
        message.error('修改失败');
      })
    }
  }
};
</script>
