<template>
  <div class="header_container">
    <el-breadcrumb separator="/">
      <!-- <el-breadcrumb-item :to="{ path: '/manage' }">首页</el-breadcrumb-item> -->
      <el-breadcrumb-item>{{$route.meta.title}}</el-breadcrumb-item>
    </el-breadcrumb>
    <el-dropdown @command="handleCommand" menu-align="start" v-if="userroot==3">
      <img :src="adminImageUrl + admininfo.admin_avator" class="avator" />
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="home">个人中心</el-dropdown-item>
        <el-dropdown-item command="singout">退出</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
import { user,store,admin,adminImageUrl } from "@/api/api.js";
export default {
  data() {
    return {
      adminImageUrl
    };
  },
  created() {
  },
  mounted() {
    console.log(this.admininfo)
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
    admininfo() {
      return JSON.parse(sessionStorage.getItem("admininfo"));
    },
    userroot() {
      return sessionStorage.getItem("userroot");
    }
  },
  methods: {
    handleCommand(command) {
      if (command == "home") {
        this.$router.push("/adminSet");
      } else if (command == "singout") {
        sessionStorage.removeItem("admininfo")
        sessionStorage.removeItem("userroot")
        sessionStorage.removeItem("username")
        this.$message({
          type: "success",
          message: "退出成功"
        });
        this.$router.push("/");
      }
    }
  }
};
</script>

<style lang="less">
@import "../style/mixin";
.header_container {
  background-color: #eff2f7;
  height: 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 20px;
}
.avator {
  .wh(36px, 36px);
  border-radius: 50%;
  margin-right: 37px;
}
.el-dropdown-menu__item {
  text-align: center;
}
</style>
