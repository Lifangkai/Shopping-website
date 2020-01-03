<template>
  <div class="user">
    <!-- 头部 -->
    <div class="container">
      <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <!-- <h3>在线购物网站</h3> -->
        <el-menu-item index="userHome">
          <h3>个人购物网站</h3>
        </el-menu-item>
        <el-menu-item index="goodAll">所有商品</el-menu-item>
        <el-menu-item index="猜你喜欢">猜你喜欢</el-menu-item>
        <el-menu-item index="食品区">食品区</el-menu-item>
        <el-menu-item index="护肤品区">护肤品区</el-menu-item>
        <el-menu-item index="纺织区">纺织区</el-menu-item>
        <el-menu-item index="妇婴区">妇婴区</el-menu-item>
        <el-menu-item index="零食区">零食区</el-menu-item>
        <el-menu-item index="冻饮区">冻饮区</el-menu-item>
        <el-menu-item index="热饮区">热饮区</el-menu-item>
        <el-menu-item index="日用品区">日用品区</el-menu-item>
        <el-submenu index="2">
          <template slot="title">个人中心</template>
          <el-menu-item index="userInfo" v-show="userinfo" >个人信息</el-menu-item>
          <el-menu-item index="userOrder" v-show="userinfo" >订单管理</el-menu-item>
          <el-menu-item index="shopCart" v-show="userinfo" >购物车</el-menu-item>
          <el-menu-item index="login" v-show="!userinfo" >登陆注册</el-menu-item>
          <el-menu-item index="/" v-show="userinfo" @click="back">退出登陆</el-menu-item>
        </el-submenu>
      </el-menu>
    </div>

    <!-- 中间 -->
    <div class="zhongjian">
      <router-view></router-view>
    </div>

    <!-- 尾部 -->
    <footer style="paddingBottom:50px">
      <div class="container">
        <hr style="margin:100px 0 50px" />
        <p class="pull-right">
          <el-button @click="backTop">Back to top</el-button>
        </p>
        <p>
          &copy; 2016 Company, Inc. &middot;
          <a href="#">Privacy</a> &middot;
          <a href="#">Terms</a>
        </p>
      </div>
    </footer>
  </div>
</template>
<script>
import { user,api } from "../../api/api.js";
import { deepClone } from "../comm_func.js"
export default {
  data() {
    return {
      activeIndex2: "userHome",
      userinfo:""
    };
  },
  beforeMount() {
    this.initData();
  },
  mounted() {
    // console.log(this.userinfo)
  },
  computed: {
  },
  methods: {
    // 初始化数据
    initData() {
      let data = {};
      user.userListOne().then(res => {
        if (res.code == "0000") {
          data = deepClone(res.data[0]);
          this.userinfo = res.data[0]
          data = JSON.stringify(data)
          sessionStorage.setItem("userinfo",data)
          sessionStorage.setItem("username",res.data[0].user_name)
          sessionStorage.setItem("userroot","1")
        }
      });
    },
    // 选中导航
    handleSelect(key, keyPath) {
      if (
        key == "猜你喜欢" ||
        key == "食品区" ||
        key == "护肤品区" ||
        key == "纺织区" ||
        key == "妇婴区" ||
        key == "零食区" ||
        key == "冻饮区" ||
        key == "热饮区" ||
        key == "日用品区"
      ) {
        this.$router.push({ path: "goodClass", query: { data: key } });
      } else {
        this.$router.push({ path: key });
      }
    },
    // 返回顶部
    backTop() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    },
    // 退出登陆
    back(){
      api.loginOut().then(res => {
        if(res.code == "0000"){
          sessionStorage.removeItem("userinfo")
          sessionStorage.removeItem("userroot")
          sessionStorage.removeItem("username")
          this.$router.go(0)
        }
      })
    }
  }
};
</script>
<style lang="less">
@import "../../style/mixin";
.pull-right {
  float: right;
}
.user {
  background: #f2f2f2;
}
.user .el-menu-demo {
  /* background-color: #545c64; */
  /* color: #fff */
  background: rgba(0, 0, 0, 0.7);
  z-index: 2;
}
.user .el-menu-item,
.user .el-submenu__title {
  color: #fff;
}
.user .el-menu--horizontal.el-menu--dark .el-submenu .el-menu-item.is-active,
.user .el-menu-item.is-active {
  color: #ffd04b;
  border-bottom: 2px solid #ffd04b;
}
.user .el-menu--horizontal .el-menu-item {
  border: none;
}
.user .el-menu--horizontal .el-menu-item:hover,
.user .el-menu--horizontal .el-submenu__title:hover {
  background: none;
}
.user .el-menu--horizontal > .el-menu-item:hover,
.user .el-menu--horizontal > .el-submenu.is-active .el-submenu__title,
.user .el-menu--horizontal > .el-submenu:hover .el-submenu__title {
  border-bottom: 2px solid #ffd04b;
}
.user .el-menu--horizontal .el-submenu > .el-menu {
  background: rgba(0, 0, 0, 0.7);
}
.user .el-menu--horizontal .el-submenu .el-menu-item {
  background: transparent;
}
// .zhongjian {
//   padding:50px 0;
//   margin: 10px 0;
//   background: #F5F5F5
// }
</style>