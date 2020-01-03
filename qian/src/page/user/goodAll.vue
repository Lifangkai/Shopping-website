<template>
  <div class="container">
    <!-- 搜索 -->
    <el-row type="flex" justify="center" style="margin:50px 0">
      <el-col :span="12">
        <div>
          <el-input v-model="search" placeholder="请输入商品名称">
            <!-- <el-button slot="append" @click="handleSearch">搜索</el-button> -->
          </el-input>
        </div>
      </el-col>
    </el-row>
    <!-- 商品分类 -->
    <template v-if="search == ''">
      <div v-for="(item,index) in classList" :key="index">
        <h2 style="margin:20px 0px">{{ item }}</h2>
        <el-row type="flex">
          <template v-for="(value,i) in dataList">
            <el-col :span="4" v-if="value.food_class == item">
              <el-card :body-style="{ padding: '0px',width:'200px' }">
                <img :src="foodImageUrl + value.food_avator" style="height:200px;width:100%" />
                <div style="padding: 14px;">
                  <p class="foodName">{{ value.food_name }}</p>
                  <p class="foodSell">特点：{{ value.food_characteristic }}</p>
                  <!-- <p class="foodPrice">价格：{{ value.food_name }}</p> -->
                  <div class="bottom">
                    <el-button type="text" class="button" @click="handleClick(value,i)">商品详情</el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
          </template>
        </el-row>
      </div>
    </template>

    <!-- 商品搜索 -->
    <template v-else>
      <el-row>
        <template v-for="(value,i) in searchList">
          <el-col :span="4" style="marginTop:20px">
            <el-card :body-style="{ padding: '0px' }">
              <img :src="foodImageUrl + value.food_avator" style="height:200px;width:100%" />
              <div style="padding: 14px;">
                <p class="foodName">{{ value.food_name }}</p>
                  <p class="foodSell">特点：{{ value.food_characteristic }}</p>
                  <!-- <p class="foodPrice">价格：{{ value.food_name }}</p> -->
                <div class="bottom">
                  <el-button type="text" class="button" @click="handleClick(value,i)">商品详情</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </template>
      </el-row>
    </template>
  </div>
</template>
<script>
import { food, foodImageUrl } from "../../api/api.js";
import { array_remove_repeat, deepClone } from "../comm_func.js";
export default {
  data() {
    return {
      foodImageUrl,
      search: "",
      dataList: [],
      classList: []
    };
  },
  mounted() {
    this.initData();
  },
  computed: {
    searchList() {
      return this.dataList.filter(data =>
        data.food_name.toLowerCase().includes(this.search.toLowerCase())
      );
    }
  },
  methods: {
    // 初始化数据
    initData() {
      let data = [];
      food.foodListAll().then(res => {
        if (res.code == "0000") {
          this.dataList = res.data;
          for (var i = 0; i < this.dataList.length; i++) {
            data.push(this.dataList[i].food_class);
          }
          // console.log(this.dataList)
          this.classList = array_remove_repeat(data);
        }
      });
    },
    // 商品详情
    handleClick(value, i) {
      // console.log(value);
      this.$router.push({
        name: "商品详情",
        params: {
          data: value
        }
      });
    },
    // 搜索
    handleSearch() {}
  }
};
</script>
<style lang="less">
@import "../../style/mixin";
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
      clear: both
  }
</style>