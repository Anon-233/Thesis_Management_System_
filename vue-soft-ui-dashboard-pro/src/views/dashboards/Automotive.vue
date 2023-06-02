<template>
  <div class="py-4 container-fluid ">

    <button @click="ask">chat</button>

    <!-- <a-button type="primary" class="px-3 py-2 fixed-plugin-button text-dark position-fixed" @click="showDrawer">Open</a-button>
    <a-drawer
      title="Basic Drawer"
      :placement="placement"
      :closable="false"
      :visible="visible"
      @close="onClose"
    >
      <p>Some contents...</p>
      <p>Some contents...</p>
      <p>Some contents...</p>
    </a-drawer> -->

  </div>
</template>

<script>
// import MiniStatisticsCard from "../../examples/Cards/MiniStatisticsCard.vue";
// import PlayerCard from "./components/PlayerCard.vue";
// import CardDetail from "./components/CardDetail.vue";
// import setTooltip from "@/assets/js/tooltip.js";
// import axios from 'axios';
// import {  ref } from 'vue';
export default {
  name: "Automotive",
  // components: {
  //   MiniStatisticsCard,
  //   PlayerCard,
  //   CardDetail
  // },
  data() {
    return {
      apiKey:"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",
      placement:'left',
      visible:false
    };
  },
  mounted() {
    // setTooltip(this.$store.state.bootstrap);

  },

  methods:{
    // ask(){
    //   const model = 'gpt-3.5-turbo';
    //   const messages = [{ role: 'user', content: '用100字写写什么是群？' }];

    //   const config = {
    //     headers: {
    //       'Content-Type': 'application/json',
    //       'Authorization': `Bearer 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`,
    //     },
    //   };

    //   const requestData = {
    //     model,
    //     messages,
    //   };

    //   axios.post('https://api.openai.com/v1/chat/completions', requestData, config)
    //     .then(response => {
    //       const completion = response.data.choices[0].message;
    //       console.log(completion.content);
    //       console.log(completion.role);
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },
    // showDrawer(){
    //   this.visible = true;
    // },
    // onClose(){
    //   this.visible = false;
    // },
  }
};
</script>
