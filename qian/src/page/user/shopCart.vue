<template>
  <div class="container">
    <!-- 购物车列表 -->
    <el-table
      :data="tableData"
      tooltip-effect="dark"
      border
      style="width: 100%;marginTop:50px"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="60"></el-table-column>
      <el-table-column label="商品信息" width="240">
        <template slot-scope="scope">
          <el-row>
            <el-col :span="12">
              <img :src="foodImageUrl + scope.row.food_avator" style="width:100%;height:100%" />
            </el-col>
            <el-col :span="6">
              <p style="marginTop:40px">{{ scope.row.food_name }}</p>
            </el-col>
          </el-row>
        </template>
      </el-table-column>
      <el-table-column label="商品参数">
        <template slot-scope="scope">{{ scope.row.food_introduction }}</template>
      </el-table-column>
      <el-table-column label="单价">
        <template slot-scope="scope">{{ scope.row.food_price }}</template>
      </el-table-column>
      <el-table-column label="数量" min-width="120">
        <template slot-scope="scope">
          <el-input-number v-model="scope.row.food_number" :min="1" @change="handleEdit(scope.row)"></el-input-number>
        </template>
      </el-table-column>
      <el-table-column label="金额">
        <template slot-scope="scope">{{ scope.row.food_price * scope.row.food_number }}</template>
      </el-table-column>
      <el-table-column label="操作" width="100">
        <template slot-scope="scope">
          <el-button size="small" type="danger" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 结算 -->
    <el-row class="row_class">
      <el-col :span="4" :offset="14">
        <p>已选商品 {{ totel }} 件</p>
      </el-col>
      <el-col :span="4">
        <p>合计 {{ totelAllPrice }}</p>
      </el-col>
      <el-col :span="2">
        <el-button type="danger" class="buttonCost" @click="handleCost" :disabled="totel == 0">结算</el-button>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import { foodImageUrl, order, shopcart } from "../../api/api.js";
import { deepClone, createId } from "../comm_func.js";
export default {
  data() {
    return {
      foodImageUrl,
      tableData: [],
      multipleSelection: [],
      selectList: []
    };
  },
  computed: {
    userinfo() {
      return JSON.parse(sessionStorage.getItem("userinfo"));
    },
    userroot() {
      return this.$store.state.userroot;
    },
    // 选中商品
    totel() {
      return this.selectList.length;
    },
    // 选中商品总价
    totelAllPrice() {
      let num = 0;
      this.selectList.forEach((item, i) => {
        num += item.food_price * item.food_number;
      });
      return num;
    }
  },
  mounted() {
    this.initData();
  },
  methods: {
    // 初始化数据
    initData() {
      // console.log(this.shopcart);
      shopcart.shopCartAll().then(res => {
        if (res.code == "0000") {
          this.tableData = res.data;
        }
      });
    },
    handleSelectionChange(val) {
      this.selectList = val;
      // console.log(val)
    },
    // 删除商品
    handleDelete(row) {
      shopcart.shopCartDel(row).then(res => {
        if (res.code == "0000") {
          this.$message({
            message: res.msg,
            type: "success"
          });
          this.initData();
        }
      });
    },
    //修改购物车信息
    handleEdit(row) {
      shopcart.shopCartEdit(row).then(res => {
        if (res.code == "0000") {
          condole.log(success);
        }
      });
    },
    // 结算接口
    orderListAdd(params) {
      return new Promise((resolve, reject) => {
        order.orderListAdd(params).then(res => {
          resolve(res);
        });
      });
    },
    // 结算
    handleCost() {
      let modelBody = [];
      for (var i = 0; i < this.selectList.length; i++) {
        // console.log(index)
        let params = {
          oid: createId(),
          bid: this.selectList[i].bid,
          uid: this.userinfo.uid,
          fid: this.selectList[i].fid,
          food_number: parseInt(this.selectList[i].food_number),
          order_name: this.selectList[i].food_name,
          order_allprice:this.selectList[i].food_price * this.selectList[i].food_number,
          order_status: "商家准备"
        };
        modelBody.push(params);
      }
      let aliparams = {
        uid: this.userinfo.uid,
        order_allprice: this.totelAllPrice,
        order_name: modelBody[0].order_name,
        modelBody: modelBody
      };
      shopcart.alipay(aliparams).then(res => {
          //返回参数
          let htmls = res
          console.log(htmls)
          let routerData = this.$router.resolve({
            path: '/applyText',
            query: { htmls: res }
          });
          // this.htmls = res.data.result; //打开新页面
          window.open(routerData.href, "_blank");
          // const div = document.createElement("div");
          // div.innerHTML = htmls;
          // document.body.appendChild(div);
          // document.forms[0].submit();
      })
    }
  }
};
</script>
<style scoped>
.row_class {
  background: #eef1f6;
  margin-top: 30px;
}
.row_class p {
  line-height: 50px;
}
.buttonCost {
  /* margin-top: 50%; */
  /* transform: translateY(-50%); */
  width: 100%;
  height: 50px;
}
</style>