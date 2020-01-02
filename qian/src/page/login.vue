<template>
  <div class="login_page fillcontain" id="login_page">
    <div class="star comet"></div>
    <transition name="form-fade" mode="in-out">
      <section class="form_contianer">
        <div class="manage_tip">
          <p v-show="radio1 == 1">在线购物系统</p>
          <p v-show="radio1 == 2">店铺管理系统</p>
          <p v-show="radio1 == 3">后台管理系统</p>
        </div>
        <div v-show="!isRegister">
          <div class="user_group">
            <el-radio v-model="radio1" label="1" border>用户</el-radio>
            <el-radio v-model="radio1" label="2" border>商家</el-radio>
            <el-radio v-model="radio1" label="3" border>管理员</el-radio>
          </div>
          <el-form :model="loginForm" :rules="loginRules" ref="loginForm">
            <el-form-item prop="username">
              <el-input type="text" v-model="loginForm.username" placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input type="password" placeholder="密码" v-model="loginForm.password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="beforeLogin" class="submit_btn">登陆</el-button>
            </el-form-item>
            <el-form-item>
              <el-button @click="isRegister = !isRegister" class="submit_btn">注册</el-button>
            </el-form-item>
            <!-- <el-form-item>
              <el-button @click="$router.go(-1)" class="submit_btn">返回</el-button>
            </el-form-item> -->
          </el-form>
          <slide-verify
          v-if="isShow"
          :l="40"
          :r="10"
          :w="310"
          :h="155"
          @success="onSuccess"
          @fail="onFail"
          @refresh="onRefresh"
          :slider-text="text"
          style="marginBottom:20px"
        ></slide-verify>
        </div>
        <div v-show="isRegister">
          <div class="user_group">
            <el-radio v-model="radio1" label="1" border>用户</el-radio>
            <el-radio v-model="radio1" label="2" border>商家</el-radio>
          </div>
          <el-form
            :model="registerForm"
            :rules="registerRules"
            ref="registerForm"
            style="marginTop:30px"
          >
            <el-form-item prop="username">
              <el-input type="text" v-model="registerForm.username" placeholder="用户名"></el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input type="password" placeholder="密码" v-model="registerForm.password"></el-input>
            </el-form-item>
            <el-form-item prop="address">
              <el-input type="text" placeholder="地址" v-model="registerForm.address"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="userRegister()" class="submit_btn">确定</el-button>
            </el-form-item>
            <el-form-item>
              <el-button @click="isRegister = !isRegister" class="submit_btn">返回</el-button>
            </el-form-item>
          </el-form>
        </div>
      </section>
    </transition>
  </div>
</template>

<script>
import { api } from "@/api/api.js";
import { deepClone } from "./comm_func.js";
import dateFormat from "dateformat";
import md5 from "js-md5";
import { generateStars } from "./index";
export default {
  data() {
    return {
      loginForm: {
        username: "lifangkai",
        password: "lifangkai"
      },
      registerForm: {
        username: "lifangkai",
        password: "lifangkai",
        address: "lifangkai"
      },
      loginRules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" }
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }]
      },
      registerRules: {
        username: [
          { required: true, message: "请输入用户名", trigger: "blur" }
        ],
        password: [{ required: true, message: "请输入密码", trigger: "blur" }],
        address: [{ required: true, message: "请输入地址", trigger: "blur" }]
      },
      radio1: "1",
      isRegister: false,
      isShow: false,
      text: "向右滑"
    };
  },
  mounted() {
    generateStars(150);
  },
  watch: {
    radio1(){
      this.isShow = false
    }
  },
  methods: {
    // 登陆前判断
    beforeLogin(){
      // console.log(this.loginRules)
      if(this.loginForm.username != "" && this.loginForm.password != ""){
        this.isShow = true
      } else {
        this.isShow = false
      }
    },
    // 登陆
    userLogin() {
      let params = deepClone(this.loginForm);
      params["password"] = md5(params["password"]);
      if (this.radio1 == "1") {
        // 用户登陆
        api.userLogin(params).then(res => {
          console.log(res);
          if (res.code == "0000") {
            this.$store.commit("setUserName", params["username"]);
            sessionStorage.setItem("username", params["username"]);
            let root = "1";
            sessionStorage.setItem("userroot", root);
            this.$store.commit("setUserRoot", root);
            this.$router.push("/userHome");
          } else {
            this.$message({
              message: res.msg,
              type: "error"
            });
          }
        });
      } else if (this.radio1 == "2") {
        // 商家登陆
        api.storeLogin(params).then(res => {
          // console.log(res);
          if (res.code == "0000") {
            this.$store.commit("setUserName", params["username"]);
            sessionStorage.setItem("username", params["username"]);
            let root = "2";
            sessionStorage.setItem("userroot", root);
            this.$store.commit("setUserRoot", root);
            this.$router.push("/storeInfo");
          } else {
            this.$message({
              message: res.msg,
              type: "error"
            });
          }
        });
      } else if (this.radio1 == "3") {
        // 管理员登陆
        api.adminLogin(params).then(res => {
          console.log(res);
          if (res.code == "0000") {
            this.$store.commit("setUserName", params["username"]);
            sessionStorage.setItem("username", params["username"]);
            let root = "3";
            sessionStorage.setItem("userroot", root);
            this.$store.commit("setUserRoot", root);
            this.$router.push("/adminSet");
          } else {
            this.$message({
              message: res.msg,
              type: "error"
            });
          }
        });
      }
    },
    // 注册
    userRegister() {
      let params = deepClone(this.registerForm);
      let time = dateFormat(new Date(), "yyyy-MM-dd hh:mm:ss");
      params["password"] = md5(params["password"]);
      params["time"] = time.toString();
      if (this.radio1 == "1") {
        api.userRegister(params).then(res => {
          // console.log(res);
          if (res.code == "0000") {
            this.$message({
              message: res.msg,
              type: "success"
            });
            this.registerForm = {};
            this.isRegister = !this.isRegister;
          } else {
            this.$message({
              message: res.msg,
              type: "error"
            });
          }
        });
      } else if (this.radio1 == "2") {
        api.storeRegister(params).then(res => {
          // console.log(res);
          if (res.code == "0000") {
            this.$message({
              message: res.msg,
              type: "success"
            });
            this.registerForm = {};
            this.isRegister = !this.isRegister;
          } else {
            this.$message({
              message: res.msg,
              type: "error"
            });
          }
        });
      }
    },
    // 验证
    onSuccess() {
      this.isShow = false;
      this.userLogin();
    },
    onFail() {
      // this.isShow = false;
      this.$message.error('验证码错误');
    },
    onRefresh() {}
  }
};
</script>

<style lang="less" scoped>
@import "../style/mixin";
@import "./style.css";
.login_page {
  // background-color: #324057;
}
.user_group {
  margin-bottom: 20px;
  margin-top: 10px;
}
.manage_tip {
  position: absolute;
  width: 100%;
  top: -100px;
  left: 0;
  p {
    font-size: 34px;
    color: #fff;
  }
}
.form_contianer {
  width: 320px;
  //   height: %;
  .ctp(320px, 210px);
  padding: 0px 25px;
  border-radius: 5px;
  text-align: center;
  background-color: #fff;
  .submit_btn {
    width: 100%;
    font-size: 16px;
  }
}
.tip {
  font-size: 12px;
  color: red;
}
.form-fade-enter-active,
.form-fade-leave-active {
  transition: all 1s;
}
.form-fade-enter,
.form-fade-leave-active {
  transform: translate3d(0, -50px, 0);
  opacity: 0;
}
</style>
