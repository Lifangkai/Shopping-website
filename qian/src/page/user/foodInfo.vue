<template>
  <div>
    <el-row style="margin-top:30px;" justify="center" class="row-bg">
      <el-col :span="8" :offset="1">
        <div class="wrap">
          <div class="biger" id="biger"></div>
          <div class="imgs">
            <div class="main" id="main">
              <div class="mask" id="mask"></div>
            </div>
            <ul class="smaller" id="smaller"></ul>
          </div>
        </div>
        <!-- <el-form :model="foodForm" label-width="110px" class="form food_form">
          <el-form-item label="商品图片:">
            <div class="wrap">
              <div class="biger" id="biger"></div>
              <div class="imgs">
                <div class="main" id="main">
                  <div class="mask" id="mask"></div>
                </div>
                <ul class="smaller" id="smaller"></ul>
              </div>
            </div>
          </el-form-item>
          <el-form-item label="商品种类:" prop="name">
            {{ foodForm.food_class }}
          </el-form-item>
          <el-form-item label="种类描述:" prop="description">
            {{ foodForm.food_class_detail }}
          </el-form-item>
          <el-form-item label="商品名称:" prop="name">
            {{ foodForm.food_name }}
          </el-form-item>
          <el-form-item label="商品活动:" prop="activity">
            {{ foodForm.food_activity }}
          </el-form-item>
          <el-form-item label="商品详情:" prop="description">
            {{ foodForm.food_introduction }}
          </el-form-item>
          <el-form-item label="商品特点:">
            <el-tag
              v-for="(item,index) in foodForm.food_characteristic"
              :key="index"
              style="marginRight:5px"
            >{{ item }}</el-tag>
          </el-form-item>
          <el-form-item label="商品规格:"> 
            <el-table
              :data="foodForm.food_other"
              style="margin-bottom: 20px;"
              :row-class-name="tableRowClassName"
            >
              <el-table-column prop="specs" label="规格"></el-table-column>
              <el-table-column prop="packing_fee" label="包装费"></el-table-column>
              <el-table-column prop="price" label="价格"></el-table-column>
            </el-table>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="addFood()">添加到购物车</el-button>
            <el-button @click="back">返回</el-button>
          </el-form-item>
        </el-form>-->
      </el-col>
      <el-col :span="12">
        <h1>{{ foodForm.food_name }}</h1>
        <p class="title">商品种类：{{ foodForm.food_class }}</p>
        <p class="title">种类描述：{{ foodForm.food_class_detail }}</p>
        <p class="price">价格：￥{{ foodPrice }}</p>
        <!-- <el-row style="marginTop:20px"> -->
        <el-button type="danger" class="shopBtn" @click="addFood()">添加到购物车</el-button>
        <!-- <el-col :span="5"><el-button size="medium" class="shopBtn" @click="back">返回</el-button></el-col> -->
        <!-- </el-row> -->
      </el-col>
    </el-row>
    <el-row justify="center" class="row-bg">
      <el-col :span="4">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <h2>{{ businessForm.bus_name }}</h2>
            <!-- <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button> -->
          </div>
          <div class="text item">
            <p style="color: #666;fontSize: 16px;">店铺电话：{{ businessForm.bus_phone }}</p>
            <p class="title">店铺地址：{{ businessForm.bus_address }}</p>
            <p class="title">店铺介绍：{{ businessForm.bus_introduction }}</p>
          </div>
        </el-card>
      </el-col>
      <el-col :span="16" :offset="2">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="商品详情" name="first">
            <p style="color: #666;fontSize: 16px;">商品详情：{{ foodForm.food_introduction }}</p>
            <p class="title">
              商品特点：
              <el-tag
                v-for="(item,index) in foodForm.food_characteristic"
                :key="index"
                style="marginRight:5px"
              >{{ item }}</el-tag>
            </p>
            <p class="title">商品活动：{{ foodForm.food_activity }}</p>
            <p class="title">商品规格：</p>
            <el-table
              :data="foodForm.food_other"
              style="margin-top: 20px;"
              :row-class-name="tableRowClassName"
              border
            >
              <el-table-column prop="specs" label="规格"></el-table-column>
              <el-table-column prop="packing_fee" label="包装费"></el-table-column>
              <el-table-column prop="price" label="价格"></el-table-column>
            </el-table>
          </el-tab-pane>
          <el-tab-pane label="店铺详情" name="second">
            <el-form :model="businessForm">
              <el-form-item label="店铺简介" prop="bus_introduction">{{ businessForm.bus_introduction }}</el-form-item>
              <el-form-item label="店铺分类">
                <!-- <el-cascader :options="categoryOptions" v-model="value"></el-cascader> -->
                {{ businessForm.bus_class }}
              </el-form-item>
              <el-form-item label="店铺特点" style="white-space: nowrap;">
                <br />
                <span>品牌保证</span>
                <el-switch on-text off-text v-model="delivery_count.is_premium"></el-switch>
                <span>蜂鸟专送</span>
                <el-switch on-text off-text v-model="delivery_count.delivery_mode"></el-switch>
                <span>新开店铺</span>
                <el-switch on-text off-text v-model="delivery_count.new"></el-switch>
              </el-form-item>
              <el-form-item style="white-space: nowrap;">
                <span>外卖保</span>
                <el-switch on-text off-text v-model="delivery_count.bao"></el-switch>
                <span>准时达</span>
                <el-switch on-text off-text v-model="delivery_count.zhun"></el-switch>
                <span>开发票</span>
                <el-switch on-text off-text v-model="delivery_count.piao"></el-switch>
              </el-form-item>
              <el-form-item label="配送费" prop="bus_delivery">
                <!-- <el-input-number v-model="formData.bus_delivery" :min="0" :max="20"></el-input-number> -->
                ￥{{ businessForm.bus_delivery }}
              </el-form-item>
              <el-form-item label="起送价" prop="bus_start_delivery">
                <!-- <el-input-number v-model="formData.bus_start_delivery" :min="0" :max="100"></el-input-number> -->
                ￥{{ businessForm.bus_start_delivery }}
              </el-form-item>
              <el-form-item label="营业时间" style="white-space: nowrap;">
                <p>起始时间：{{ businessForm.bus_start_time }} ------ 结束时间：{{ businessForm.bus_end_time }}</p>
              </el-form-item>
              <el-form-item label="店铺头像">
                <img
                  v-if="businessForm.bus_avator"
                  :src="bussinessImageUrl + businessForm.bus_avator"
                  class="avatar"
                />
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
              </el-form-item>
              <el-form-item label="优惠活动">
                <!-- <el-select
                      v-model="activityValue"
                      @change="selectActivity"
                      :placeholder="activityValue"
                    >
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value"
                      ></el-option>
                </el-select>-->
                <el-table
                  :data="activities"
                  style="min-width: 600px;margin-bottom: 20px;"
                  align="center"
                  :row-class-name="tableRowClassName"
                  border
                >
                  <el-table-column prop="icon_name" label="活动标题" align="cneter" width="120"></el-table-column>
                  <el-table-column prop="name" label="活动名称" align="cneter" width="120"></el-table-column>
                  <el-table-column prop="description" align="cneter" label="活动详情"></el-table-column>
                </el-table>
              </el-form-item>
            </el-form>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import { foodImageUrl } from "../../api/api.js";
import { deepClone } from "../comm_func.js";
import { scroll } from "../tools.js";
import { business, bussinessImageUrl, shopcart } from "../../api/api.js";
export default {
  data() {
    return {
      foodImageUrl,
      bussinessImageUrl,
      foodForm: {},
      foodPrice: "",
      activeName: "first",
      businessForm: {},
      delivery_count: "",
      activities: []
    };
  },
  computed: {
    username() {
      return this.$store.state.username;
    },
    userinfo() {
      return JSON.parse(sessionStorage.getItem("userinfo"));
    },
    shopcart() {
      return this.$store.state.shopcart;
    }
  },
  mounted() {
    this.foodForm = deepClone(this.$route.params.data);
    //   console.log(this.foodForm)
    this.foodForm.food_characteristic = JSON.parse(
      this.foodForm.food_characteristic
    );
    this.foodForm.food_other = JSON.parse(this.foodForm.food_other);
    let num = 0;
    this.foodForm.food_other.forEach((item, i) => {
      num += item.price;
    });
    this.foodPrice = num;
    business.bussinessListOne(this.foodForm).then(res => {
      if (res.code == "0000") {
        // console.log(res.data);
        this.businessForm = res.data[0];
        this.delivery_count = JSON.parse(this.businessForm.bus_characteristic);
        console.log(this.delivery_count);
        this.activities = JSON.parse(this.businessForm.bus_discount);
      }
    });
    // console.log(this.foodForm)
    this.moveFunc();
    // scroll();
  },
  methods: {
    // 添加到购物车
    addFood() {
      if (!sessionStorage.getItem("username")) {
        this.$router.push({ path: "/login" });
        return;
      }
      let price = 0;
      for (var i = 0; i < this.foodForm.food_other.length; i++) {
        price += this.foodForm.food_other[i].price;
      }
      let params = {
        uid: this.userinfo.uid,
        bid: this.foodForm.bid,
        fid: this.foodForm.fid,
        food_name: this.foodForm.food_name,
        food_avator: this.foodForm.food_avator,
        food_introduction: this.foodForm.food_introduction,
        food_price: price,
        food_number: 1
      };
      shopcart.shopCartAdd(params).then(res => {
        if (res.code == "0000") {
          this.$message({
            message: "添加成功",
            type: res.msg
          });
        }
      });
    },
    tableRowClassName(row, index) {
      if (index === 1) {
        return "info-row";
      } else if (index === 3) {
        return "positive-row";
      }
      return "";
    },
    // 移动
    moveFunc() {
      var biger = document.getElementById("biger");
      var main = document.getElementById("main");
      var smaller = document.getElementById("smaller");
      var mask = document.getElementById("mask");
      var wrap = biger.parentNode;
      var imgArr = [{ path: this.foodImageUrl + this.foodForm.food_avator }];
      var imgSum = imgArr.length;
      if (imgSum > 5) {
        imgSum = 5;
      }
      for (var i = 0; i < imgSum; i++) {
        var lis = document.createElement("li");
        var imgs = document.createElement("img");
        imgs.src = imgArr[i].path;
        imgs.style.width = 64 + "px";
        imgs.style.height = 64 + "px";
        lis.appendChild(imgs);
        smaller.appendChild(lis);
      }
      var mainImg = document.createElement("img");
      var bigImg = document.createElement("img");
      var liArr = smaller.children;
      bigImg.src = mainImg.src = liArr[0].children[0].src;
      mainImg.style.width = 390 + "px";
      mainImg.style.height = 390 + "px";
      bigImg.style.width = 780 + "px";
      bigImg.style.height = 780 + "px";
      bigImg.style.position = "absolute";
      bigImg.style.position = "absolute";
      main.insertBefore(mainImg, mask);
      biger.appendChild(bigImg);
      var bigPic = biger.children[0];
      liArr[0].className = "current";
      for (var i = 0; i < liArr.length; i++) {
        liArr[i].index = i;
        liArr[i].onclick = function() {
          this.className = "current";
          bigPic.src = main.children[0].src = this.children[0].src;
          for (var j = 0; j < liArr.length; j++) {
            if (this != liArr[j]) {
              liArr[j].removeAttribute("class");
              liArr[j].removeAttribute("className");
            }
          }
        };
      }
      main.onmouseenter = function() {
        mask.style.display = "block";
        biger.style.display = "block";
      };
      main.onmouseleave = function() {
        mask.style.display = "none";
        biger.style.display = "none";
      };
      main.onmousemove = function(e) {
        // 获取元素距离左边浏览器距离
        var getOffsetLeft = function(obj) {
          var tmp = obj.offsetLeft;
          var node = obj.offsetParent;
          while (node != null) {
            tmp += node.offsetLeft;
            node = node.offsetParent;
          }
          return tmp;
        };
        // 获取元素距离上边浏览器距离
        var getOffsetTop = function(obj) {
          var tmp = obj.offsetTop;
          var node = obj.offsetParent;
          while (node != null) {
            tmp += node.offsetTop;
            node = node.offsetParent;
          }
          return tmp;
        };
        var e = e || window.event;
        var pagex = e.pageX || scroll().left + e.clientX;
        var pagey = e.pageY || scroll().top + e.clientY;
        // console.log(wrap);
        var eleLeft = getOffsetLeft(main);
        var eleTop = getOffsetTop(main);
        // console.log(eleLeft, eleTop);
        pagex = pagex - eleLeft - mask.offsetWidth / 2;
        pagey = pagey - eleTop - mask.offsetHeight / 2;
        if (pagex < 0) {
          pagex = 0;
        }
        if (pagey < 0) {
          pagey = 0;
        }
        if (pagex > main.offsetWidth - mask.offsetWidth) {
          pagex = main.offsetWidth - mask.offsetWidth;
        }
        if (pagey > main.offsetHeight - mask.offsetHeight) {
          pagey = main.offsetHeight - mask.offsetHeight;
        }
        mask.style.left = pagex + "px";
        mask.style.top = pagey + "px";
        var scale =
          (bigPic.offsetWidth - biger.offsetWidth) /
          (main.offsetWidth - mask.offsetWidth);
        var xx = pagex * scale;
        var yy = pagey * scale;
        bigPic.style.left = -xx + "px";
        bigPic.style.top = -yy + "px";
      };
    },
    // tab选择
    handleClick(tab, event) {
      console.log(tab, event);
    }
  }
};
</script>
<style scoped>
.avatar {
  width: 300px;
  height: 300px;
  display: block;
}
img {
  vertical-align: middle;
  width: 100%;
  height: 100%;
}
.wrap {
  position: relative;
  width: 400px;
  height: 492px;
}
.imgs {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
}
.main {
  position: relative;
  overflow: hidden;
  padding: 4px;
  width: 390px;
  height: 390px;
  border: 1px solid #dadada;
}
/* .main img {
  width: 390px;
  height: 390px;
} */
.smaller {
  position: relative;
  overflow: hidden;
  width: 400px;
  height: 82px;
  margin-top: 10px;
}
.smaller li {
  position: relative;
  float: left;
  padding: 2px;
  width: 64px;
  height: 64px;
  border: 2px solid #000;
  margin-left: 10px;
  cursor: pointer;
}
.smaller li:first-child {
  margin-left: 0;
}
.smaller .current {
  border-color: #ff6a00;
}
.biger {
  position: absolute;
  overflow: hidden;
  display: none;
  left: 410px;
  width: 400px;
  height: 400px;
}
.mask {
  position: absolute;
  display: none;
  left: 0;
  top: 0;
  width: 200px;
  height: 200px;
  background: url("../mask-bg.png") repeat;
  cursor: crosshair;
}
/* .biger img {
  position: absolute;
  left: 0;
  top: 0;
  width: 200%;
  height: 200%;
} */
.title {
  color: #666;
  font-size: 16px;
  margin-top: 25px;
}
.price {
  color: #e3554c;
  font-size: 30px;
  font-weight: 600;
  margin-top: 20px;
}
.shopBtn {
  width: 200px;
  height: 60px;
  font-size: 18px;
  margin-top: 100px;
  background: #e3554c;
}
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  margin-left: 20px;
  width: 250px;
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
/* .el-switch.is-checked .el-switch__core {
  cursor:not-allowed
} */
</style>