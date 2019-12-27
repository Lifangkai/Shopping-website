<template>
  <div class="container">
    <!-- 搜索 -->
    <el-row type="flex" justify="center" style="margin:50px 0">
      <!-- <el-col :span="12">
        <div>
          <el-input v-model="search" placeholder="请输入商品名称">
          </el-input>
        </div>
      </el-col> -->
    </el-row>
    <!-- 商品分类 -->
        <el-row type="flex">
          <template v-for="(value,i) in dataList">
            <el-col :span="4">
              <el-card :body-style="{ padding: '0px' }">
                <img :src="foodImageUrl + value.food_avator" style="height:200px;width:100%" />
                <div style="padding: 14px;">
                  <p class="foodName">{{ value.food_name }}</p>
                  <p class="foodSell">特点：{{ value.food_characteristic }}</p>
                  <div class="bottom">
                    <el-button type="text" class="button" @click="handleClick(value,i)">商品详情</el-button>
                  </div>
                </div>
              </el-card>
            </el-col>
          </template>
        </el-row>

    <!-- 商品搜索 -->
    <!-- <template v-else>
      <el-row type="flex">
        <template v-for="(value,i) in searchList">
          <el-col :span="3" :offset="1">
            <el-card :body-style="{ padding: '0px' }">
              <img :src="foodImageUrl + value.food_avator" style="height:150px;width:100%" />
              <div style="padding: 14px;">
                <span>{{ value.food_name }}</span>
                <div class="bottom">
                  <el-button type="text" class="button" @click="handleClick(value,i)">商品详情</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </template>
      </el-row>
    </template> -->
  </div>
</template>
<script>
import { food, foodImageUrl } from "../../api/api.js";
import { array_remove_repeat, deepClone } from "../comm_func.js";
export default {
  data() {
    return {
      foodImageUrl,
      dataList: [],
    };
  },
  mounted() {
    let className = this.$route.query.data
    this.initData(className);
  },
  watch: {
      $route(to) {
          let className = this.$route.query.data
          this.initData(className)
      }
  },
  computed: {
    // searchList() {
    //   return this.dataList.filter(data =>
    //     data.food_name.toLowerCase().includes(this.search.toLowerCase())
    //   );
    // }
  },
  methods: {
    // 初始化数据
    initData(ele) {
        let params = {
            food_class:ele
        }
      food.foodListQuery(params).then(res => {
        if (res.code == "0000") {
          this.dataList = res.data;
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