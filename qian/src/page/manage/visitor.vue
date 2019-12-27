<template>
  <div>
    <head-top></head-top>
    <visitor-pie :pieData="userpieData" :legendData="userlegendData" :storepieData="storepieData" :storelegendData="storelegendData"></visitor-pie>
    <!-- <pie-two :pieData="storepieData" :legendData="storelegendData" :title="storeTitle"></pie-two> -->
  </div>
</template>

<script>
import headTop from "../../components/headTop";
import visitorPie from "@/components/visitorPie";
import { user,store } from "@/api/api.js";
import { array_remove_repeat } from "../comm_func.js";
export default {
  data() {
    return {
      userlegendData: [],
      userpieData: [],
      storelegendData: [],
      storepieData: [],
    };
  },
  components: {
    headTop,
    visitorPie,
  },
  mounted(){
    // 用户分布情况
    user.userListAll().then(res => {
      if (res.code == "0000") {
        let data = res.data;
        let legendData = [];
        for (var i = 0; i < data.length; i++) {
          legendData.push(data[i]["user_address"]);
        }
        // console.log(legendData);
        legendData = array_remove_repeat(legendData);
        this.userlegendData = legendData;
        for (var j = 0; j < legendData.length; j++) {
          let params = { address: legendData[j] };
          this.userListAddress(params).then(val => {
            this.userpieData.push({ value: val, name: params["address"] });
            // console.log(this.pieData);
          });
        }
      }
    });
    // 商家分布情况
    store.storeListAll().then(res => {
      if (res.code == "0000") {
        let data = res.data;
        let legendData = [];
        for (var i = 0; i < data.length; i++) {
          legendData.push(data[i]["store_address"]);
        }
        // console.log(legendData);
        legendData = array_remove_repeat(legendData);
        this.storelegendData = legendData;
        for (var j = 0; j < legendData.length; j++) {
          let params = { address: legendData[j] };
          this.storeListAddress(params).then(val => {
            this.storepieData.push({ value: val, name: params["address"] });
          });
        }
      }
    });
  },
  methods: {
    // 用户地址统计
    userListAddress(params) {
      return new Promise((resolve, reject) => {
        user.userListAddress(params).then(res => {
          if (res.code == "0000") {
            resolve(res.data);
          }
        });
      });
    },
    // 商家地址统计
    storeListAddress(params) {
      return new Promise((resolve, reject) => {
        store.storeListAddress(params).then(res => {
          if (res.code == "0000") {
            resolve(res.data);
          }
        });
      });
    },
  }
};
</script>

<style lang="less">
@import "../../style/mixin";
</style>
