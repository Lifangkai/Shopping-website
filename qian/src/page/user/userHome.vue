<template>
  <div class="userHome">
    <!-- 轮播图 -->
    <el-carousel trigger="click" height="400px" type="card">
      <el-carousel-item v-for="item in imgList" :key="item">
        <!-- <h3>{{ item }}</h3> -->
        <img class="lunbo" :src="item" />
      </el-carousel-item>
    </el-carousel>

    <!-- 推荐 -->
    <div class="container">
      <el-row type="flex" class="row-bg" justify="space-around">
        <el-col :span="6" class="tuijian">
          <img src="https://www.starbucks.com.cn/images/pages/tmall-1101-cn.jpg" alt="">
          <h2>双十一活动 速来抢购</h2>
          <p>更多精彩优惠，更多礼品，尽在双十一</p>
        </el-col>
        <el-col :span="6" class="tuijian">
          <img src="https://www.starbucks.com.cn/images/pages/starbucks-design-studio-web-china.jpg" alt="">
          <h2>全球创意设计师平台</h2>
          <p>国际设计师顶尖制作，物美价廉等你取</p>
        </el-col>
        <el-col :span="6" class="tuijian">
          <!-- <el-card :body-style="{ padding: '0px' }"> -->
            <!-- <img -->
              <!-- src="https://www.starbucks.com.cn/images/pages/homepage-career-cn.jpg" -->
              <!-- class="image" -->
            <!-- /> -->
            <!-- <div style="padding: 14px;"> -->
              <!-- <span>淘宝美食 食在任性</span> -->
              <!-- <div class="bottom clearfix"> -->
                <!-- <el-button type="text" class="button">操作按钮</el-button> -->
              <!-- </div> -->
            <!-- </div> -->
          <!-- </el-card> -->
        <img src="https://www.starbucks.com.cn/images/pages/homepage-career-cn.jpg" alt="">
          <h2>淘宝美食 是在任性</h2>
          <p>星巴克欢迎你的到来</p>
        </el-col>
      </el-row>

      <!-- <hr style="margin:50px 0 100px" /> -->

      <!-- 网站介绍 -->
      <el-row type="flex" class="row-bg" justify="space-around">
        <el-col :span="9">
          <h2 class="web_title">足不出户即可购买到你所喜欢的商品</h2>
          <p class="web_context">
            提供个人对个人的买卖平台有淘宝、易趣、拍拍等，另外还有许多提供其它
            <br />各种各样商品出售的网站。
          </p>
        </el-col>
        <el-col :span="8">
          <img
            src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573467094655&di=2b24f420f601628adf3604c6cb96d809&imgtype=0&src=http%3A%2F%2Fimg.mp.sohu.com%2Fupload%2F20170731%2F26ec9bd4e8f94219beb4c68512ef537a_th.png"
            alt
          />
        </el-col>
      </el-row>

      <br>

      <el-row type="flex" class="row-bg" justify="space-around">
        <el-col :span="8">
          <img
            src="http://img.mp.sohu.com/upload/20170731/1730037c3a2c44b3a5a34a4dd409e368_th.png"
            alt
          />
        </el-col>
        <el-col :span="9">
          <h2 class="web_title">可以货比三家，买到物美价廉的商品</h2>
          <p class="web_context">
            购物网址导航是指通过科学统筹的方法，对网友常用的购物网站进行对比，
            <br />根据网站的规模、实力、信誉等进行排行，方便网友们快速找到自已购物所需要的网站
          </p>
        </el-col>
      </el-row>

      <br>

      <el-row type="flex" class="row-bg" justify="space-around">
        <el-col :span="9">
          <h2 class="web_title">努力探寻更高意义上的导购原则和规范</h2>
          <p class="web_context">
            由于互联网在中国的迅猛发展，以及网上购物本身优势带来网购市场空前的繁荣，
            <br />迫使众多卖家急需找到更多的展示平台为自己打开销量
          </p>
        </el-col>
        <el-col :span="8">
          <img
            src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573467168530&di=8ec9eb7796466ea0069dc7acadd5d18a&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171012%2Fff01d81f159148428929638fed0fc167.jpeg"
            alt
          />
        </el-col>
      </el-row>

    </div>
  </div>
</template>
<script>
import { user,base } from "../../api/api.js";
export default {
  data() {
    return {
      base,
      imgList: [
        base + "/media/lunbo/lunbo6.jpg",
        base + "/media/lunbo/015587554320db0000019ae910eee0.jpg@1280w_1l_2o_100sh.jpg",
        base + "/media/lunbo/01605a554320e10000019ae9299b20.jpg@1280w_1l_2o_100sh.jpg",
        base + "/media/lunbo/011abc554320e00000019ae9af49db.jpg@1280w_1l_2o_100sh.jpg",
        base + "/media/lunbo/01f760554320e10000019ae9c6a3c4.jpg@1280w_1l_2o_100sh.jpg"
      ],
      currentDate: new Date()
    };
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
  },
  mounted() {
    // this.initData()
  },
  methods: {
    // 初始化数据
    // initData(){
    //   user.userListOne().then(res => {
    //     if(res.code == "0000"){
    //       this.$store.commit("setUserInfo",res.data[0])
    //     }
    //   })
    // }
  },
};
</script>
<style lang="less" scoped>
@import "../../style/mixin";
.userHome .el-carousel {
  top: -10px;
  z-index: 0;
}
.userHome .el-carousel__container {
  /* height: 500px; */
}
.userHome .el-carousel__item {
  width: 50%;
  height: 100%;
}
.lunbo {
  width: 100%;
  height: 100%;
}
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
.web_title {
    font-size: 45px;
    color: #5A5A5A;
    margin-top: 100px
}
.web_context {
    margin-top: 20px;
    font-size: 20px;
    color: #777777
}
.tuijian {
  text-align: center;
}
.tuijian img {
  width: 200px;
  height: 200px;
  border-radius: 50%
}

.tuijian h2 {
  margin-top: 10px;
  font-size: 30px;
  font-weight: 600
}
.tuijian p {
  margin-top: 10px;
  font-size: 15px;
}
</style>