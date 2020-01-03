<template>
  <div class="fillcontain">
    <head-top></head-top>
    <div class="form_container">
      <el-form label-position="right" label-width="80px" :model="formLabelAlign">
        <h2 style="width:100%;textAlign:center;marginBottom:20px">个人信息</h2>
        <el-form-item label="创建时间">
          <el-input v-model="formLabelAlign.store_time" disabled></el-input>
        </el-form-item>
        <el-form-item label="商家id">
          <el-input v-model="formLabelAlign.sid" disabled></el-input>
        </el-form-item>
        <el-form-item label="商家名称">
          <el-input v-model="formLabelAlign.store_name"></el-input>
        </el-form-item>
        <el-form-item label="商家地址">
          <el-input v-model="formLabelAlign.store_address"></el-input>
        </el-form-item>
        <h2 style="width:100%;textAlign:center;marginBottom:20px">修改密码</h2>
        <el-form-item label="旧密码">
          <el-input v-model="password.old" type="password"></el-input>
        </el-form-item>
        <el-form-item label="新密码">
          <el-input v-model="password.new" type="password"></el-input>
        </el-form-item>
        <el-form-item label="确认密码">
          <el-input v-model="password.again" type="password"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">立即修改</el-button>
          <el-button @click="back">退出登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import headTop from "../../components/headTop";
import { store,api } from "@/api/api.js";
import md5 from "js-md5";
import { deepClone } from "../comm_func.js"
export default {
  data() {
    return {
      formLabelAlign: {},
      password: {
        old: "",
        new: "",
        again: ""
      },
    };
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
    storeinfo(){
      return JSON.parse(this.$store.state.storeinfo)
    }
  },
  mounted() {
    this.initData();
  },
  components: {
    headTop
  },
  watch: {
    // $route(to) {
    //   if (
    //     to.fullPath == "/addGoods" ||
    //     to.fullPath == "/foodList" ||
    //     to.fullPath == "/shopList"
    //   ) {
    //     if (this.storeinfo.bid == "") {
    //       this.$notify({
    //         title: "警告",
    //         message: "请先添加店铺",
    //         type: "warning"
    //       });
    //     }
    //   } else if (to.fullPath == "/addShop") {
    //     if (this.storeinfo.bid != "") {
    //       this.$notify({
    //         title: "警告",
    //         message: "已有店铺",
    //         type: "warning"
    //       });
    //     }
    //   }
    // }
  },
  methods: {
    // 初始化数据
    initData() {
      new Promise((resolve, reject) => {
        store.storeListOne().then(res => {
          if (res.code == "0000") {
            sessionStorage.setItem("storeinfo",JSON.stringify(deepClone(res.data[0])))
            this.$store.commit("setStoreInfo",JSON.stringify(deepClone(res.data[0])))
            this.formLabelAlign = res.data[0];
            if(this.formLabelAlign.bid == ""){
              this.$store.commit("setIsShow",false)
              sessionStorage.setItem("isShowShop",false)
            }else{
              this.$store.commit("setIsShow",true)
              sessionStorage.setItem("isShowShop",true)
            }
            resolve(this.formLabelAlign);
          }
        });
      }).then(params => {
        store.storeListWarnQuery().then(res => {
          if (res.code == "0000") {
            if (res.data.length != 0) {
              this.$notify({
                title: "警告",
                message: res.data[0].store_content,
                type: "warning"
              });
            }
          }
        });
      });
    },
    // 修改商家信息
    onSubmit() {
      if (this.password.old == "") {
        this.storeListEdit(this.formLabelAlign);
      } else {
        let old = md5(this.password.old);
        if (old !== this.formLabelAlign.store_pwd) {
          this.$message({
            message: "旧密码错误",
            type: "error"
          });
          return;
        } else if (this.password.new !== this.password.again) {
          this.$message({
            message: "两次密码不同",
            type: "error"
          });
          return;
        } else if (this.password.new == "" || this.password.again == "") {
          this.$message({
            message: "输入新密码",
            type: "error"
          });
          return;
        } else {
          this.formLabelAlign.store_pwd = md5(this.password.new);
          this.storeListEdit(this.formLabelAlign);
        }
      }
    },
    // 修改商家信息方法
    storeListEdit(params) {
      store.storeListEdit(params).then(res => {
        if (res.code == "0000") {
          this.$message({
            message: res.msg,
            type: "success"
          });
          // this.$store.commit("setUserInfo", params);
          sessionStorage.setItem("storeinfo",JSON.stringify(deepClone(params)))
        } else {
          this.$message({
            message: res.msg,
            type: "error"
          });
        }
      });
    },
    // 退出
    back(){
      api.loginOut().then(res => {
        if(res.code == "0000"){
          sessionStorage.removeItem("storeinfo")
          sessionStorage.removeItem("userroot")
          sessionStorage.removeItem("username")
          sessionStorage.removeItem("isShowShop")
          this.$router.push({path:"/"})
        }
      })
    }
  }
};
</script>
<style lang="less">
@import "../../style/mixin";
.form_container {
  width: 50%;
  margin: 50px auto 0;
}
</style>