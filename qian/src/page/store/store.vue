<template>
  <div class="manage_page fillcontain">
    <el-row style="height: 100%;">
      <el-col :span="4" style="min-height: 100%; background-color: #324057;">
        <el-menu :default-active="defaultActive" style="min-height: 100%;" theme="dark" router>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-edit"></i>店铺
            </template>
            <el-menu-item index="shopList" v-show="isShowShop">店铺管理</el-menu-item>
            <el-menu-item index="addShop"  v-show="!isShowShop">添加店铺</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-star-off"></i>商品
            </template>
            <el-menu-item index="foodList" v-show="isShowShop">商品列表</el-menu-item>
            <el-menu-item index="addGoods" v-show="isShowShop">添加商品</el-menu-item>
          </el-submenu>
          <el-menu-item index="orderList" v-show="isShowShop">
            <i class="el-icon-more"></i>订单列表
          </el-menu-item>
          <el-menu-item index="storeInfo">
            <i class="el-icon-setting"></i>个人中心
          </el-menu-item>
        </el-menu>
      </el-col>
      <el-col :span="20" style="height: 100%;overflow: auto;">
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  computed: {
    defaultActive: function() {
      return this.$route.path.replace("/", "");
    },
    isShowShop(){
      return this.$store.state.isShowShop
    }
  }
};
</script>


<style lang="less" scoped>
@import "../../style/mixin";
.manage_page {
}
</style>
