<template>
  <div style="marginTop:100px">
    <!-- <head-top></head-top> -->
    <header class="admin_title">管理员信息</header>
    <div class="admin_set">
      <ul>
        <li>
          <span>姓名：</span>
          <span>{{adminInfo.admin_name}}</span>
        </li>
        <li>
          <span>注册地址：</span>
          <span>{{adminInfo.admin_address}}</span>
        </li>
        <li>
          <span>注册时间：</span>
          <span>{{adminInfo.admin_registertime}}</span>
        </li>
        <li>
          <span>管理员权限：</span>
          <span>{{adminInfo.admin_authority}}</span>
        </li>
        <li>
          <span>管理员 ID：</span>
          <span>{{adminInfo.aid}}</span>
        </li>
        <li>
          <span>更换头像：</span>
          <el-upload
            class="avatar-uploader"
            :action="base + '/adminlist/queryimg/'"
            :data="adminInfo"
            :on-success="uploadImg"
            :show-file-list="false"
          >
            <img
              v-if="adminInfo.admin_avator"
              :src="adminImageUrl + adminInfo.admin_avator"
              class="avatar"
            />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
// import headTop from "../../components/headTop";
// import {mapState} from 'vuex'
import { admin, base, adminImageUrl } from "@/api/api.js";
import { deepClone } from "../comm_func.js";
// import {baseUrl, baseImgPath} from '@/config/env'

export default {
  data() {
    return {
      base,
      // baseUrl,
      // baseImgPath,
      adminImageUrl,
      // imgActionUrl:"http://localhost:8000/adminlist/queryimg/",
      adminInfo: {}
    };
  },
  components: {
    // headTop
  },
  computed: {
    // ...mapState(['adminInfo']),
    // userinfo() {
    //   return this.$store.state.userinfo;
    // }
    username(){
      return this.$store.state.username
    }
  },
  mounted() {
    this.initData()
    // this.$router.go(0)
  },
  methods: {
    // 初始化数据
    initData(){
      admin.AdminListOne().then(res => {
        if (res.code == "0000") {
          // let data = JSON.stringify(deepClone(res.data[0]))
          // sessionStorage.setItem("userinfo",data)
          this.adminInfo = res.data[0]
          // this.$store.commit("setAdminInfo",this.adminInfo )
          sessionStorage.setItem("admininfo",JSON.stringify(this.adminInfo))
          this.$store.commit("setAdminInfo",JSON.stringify(this.adminInfo) )
          // this.$router.go(0)
        }
      });
    },
    uploadImg(res) {
        if(res.code == "0000"){
            this.adminInfo.admin_avator = res.data
            let data = JSON.stringify(deepClone(this.adminInfo))
            sessionStorage.setItem("admininfo",data)
            this.$store.commit("setAdminInfo",this.adminInfo )
            this.$router.go(0)
        }
    }
  }
};
</script>

<style lang="less">
@import "../../style/mixin";
.explain_text {
  margin-top: 20px;
  text-align: center;
  font-size: 20px;
  color: #333;
}
.admin_set {
  width: 60%;
  background-color: #f9fafc;
  min-height: 400px;
  margin: 20px auto 0;
  border-radius: 10px;
  ul > li {
    padding: 20px;
    span {
      color: #666;
    }
  }
}
.admin_title {
  margin-top: 20px;
  .sc(24px, #666);
  text-align: center;
}
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  margin-top: 10px;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #20a0ff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 120px;
  height: 120px;
  line-height: 120px;
  text-align: center;
}
.avatar {
  width: 120px;
  height: 120px;
  display: block;
}
</style>
