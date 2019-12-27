<template>
  <div class="container">
    <div class="form_container">
      <el-form label-position="right" label-width="80px" :model="formLabelAlign">
        <h2 style="width:100%;textAlign:center;marginBottom:20px">个人信息</h2>
        <el-form-item label="创建时间">
          <el-input v-model="formLabelAlign.user_time" disabled></el-input>
        </el-form-item>
        <el-form-item label="用户id">
          <el-input v-model="formLabelAlign.uid" disabled></el-input>
        </el-form-item>
        <el-form-item label="用户名称">
          <el-input v-model="formLabelAlign.user_name"></el-input>
        </el-form-item>
        <el-form-item label="收货地址">
          <el-input v-model="formLabelAlign.user_address"></el-input>
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
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
<script>
import { user } from "@/api/api.js";
import md5 from "js-md5";
export default {
  data() {
    return {
      formLabelAlign: {},
      password: {
        old: "",
        new: "",
        again: ""
      }
    };
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
    userinfo() {
      return JSON.parse(sessionStorage.getItem("userinfo"));
    },
  },
  mounted() {
    this.formLabelAlign = this.userinfo
    this.initData();
  },
  methods: {
    // 初始化数据
    initData() {
      user.userListWarnQuery(this.formLabelAlign).then(res => {
        if (res.code == "0000") {
          console.log(res.data);
          if (res.data.length != 0) {
            this.$notify({
              title: "警告",
              message: res.data[0].user_content,
              type: "warning"
            });
          }
        }
      });
    },
    // 修改用户信息
    onSubmit() {
      if (this.password.old == "") {
        this.userListEdit(this.formLabelAlign);
      } else {
        let old = md5(this.password.old);
        if (this.password.new == "" || this.password.again == "") {
          this.$message({
            message: "输入新密码",
            type: "error"
          });
          return;
        } else if (old !== this.formLabelAlign.user_pwd) {
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
        } else {
          this.formLabelAlign.store_pwd = md5(this.password.new);
          this.userListEdit(this.formLabelAlign);
        }
      }
    },
    // 修改用户信息方法
    userListEdit(params) {
      user.userListEdit(params).then(res => {
        if (res.code == "0000") {
          this.$message({
            message: res.msg,
            type: "success"
          });
          // this.$store.commit("setUserInfo", params);
          sessionStorage.setItem("userinfo",JSON.stringify(params))
          this.$store.commit("setUserInfo",JSON.stringify(params))
        } else {
          this.$message({
            message: res.msg,
            type: "error"
          });
        }
      });
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