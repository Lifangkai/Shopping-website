<template>
  <div class="container table_container">
    <div class="table_container">
      <el-table :data="dataList" style="width: 100%">
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="用户名">
                <span>{{ props.row.user_name }}</span>
              </el-form-item>
              <el-form-item label="店铺名称">
                <span>{{ props.row.bus_name }}</span>
              </el-form-item>
              <el-form-item label="收货地址">
                <span>{{ props.row.bus_address }}</span>
              </el-form-item>
              <el-form-item label="店铺 ID">
                <span>{{ props.row.bid }}</span>
              </el-form-item>
              <el-form-item label="店铺地址">
                <span>{{ props.row.bus_address }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="订单 ID" prop="oid"></el-table-column>
        <el-table-column label="总价格" prop="order_allprice"></el-table-column>
        <el-table-column label="订单状态" prop="order_status"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="small" type="danger" plain @click="handleDel(scope.$index, scope.row)">删除订单</el-button>
            <el-button
              size="small"
              type="info"
              plain
              @click="handleWithdraw(scope.$index, scope.row)"
            >退单</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="Pagination" style="text-align: left;margin-top: 10px;">
        <el-pagination
          @current-change="handleCurrentChange"
          @size-change="handleSizeChange"
          :page-size="pagesize"
          :page-sizes="[5, 10, 15, 20]"
          layout="prev, pager, next, sizes, total, jumper"
          :total="tableData.length"
        ></el-pagination>
      </div>
    </div>
    <!-- <el-dialog title="订单修改" :visible.sync="dialogFormVisible" style="width:80%;margin:0 auto">
      <el-form :model="form">
        <el-form-item label="订单id" :label-width="formLabelWidth">
          <el-input v-model="form.oid" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="用户名" :label-width="formLabelWidth">
          <el-input v-model="form.user_name" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="总价格" :label-width="formLabelWidth">
          <el-input v-model="form.order_allprice" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="收货地址" :label-width="formLabelWidth">
          <el-input v-model="form.bus_address" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="订单状态" :label-width="formLabelWidth">
          <el-input v-model="form.order_status" autocomplete="off" disabled></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </div>
    </el-dialog>-->
  </div>
</template>

<script>
import { order, business, user } from "@/api/api.js";
import { deepClone } from "../comm_func.js";
export default {
  data() {
    return {
      pagesize: 10,
      tableData: [],
      currpage: 1,
      formLabelWidth: "120px",
      form: {},
      options: [
        {
          value: "退单中",
          label: "退单中"
        }
      ],
      dialogFormVisible: false
    };
  },
  mounted() {
    this.initData();
  },
  computed: {
    userinfo() {
      return JSON.parse(sessionStorage.getItem("userinfo"));
    },
    userroot() {
      return this.$store.state.userroot;
    },
    dataList() {
      return this.tableData.slice(
        (this.currpage - 1) * this.pagesize,
        this.currpage * this.pagesize
      );
    }
  },
  methods: {
    // 初始化数据
    initData() {
      let params = { uid: this.userinfo.uid };
      // console.log(params)
      let tableListData = [];
      order.orderListAll(params).then(res => {
        if (res.code == "0000") {
          let orderData = res.data;
          for (var i = 0; i < orderData.length; i++) {
            let e = orderData[i];
            this.userListOne(e).then(val => {
              // console.log(val);
              let data = {};
              (data.oid = e["oid"]),
                (data.bid = e["bid"]),
                (data.uid = e["uid"]),
                (data.order_allprice = e["order_allprice"]),
                (data.order_status = e["order_status"]),
                (data.user_name = val["user_name"]),
                // console.log(data);
                this.businessListOne(data).then(val => {
                  console.log(val);
                  data.bus_name = val["bus_name"];
                  data.bus_address = val["bus_address"];
                  data.bid = val["bid"];
                  tableListData.push(data);
                  this.tableData = tableListData;
                  // console.log(this.tableData);
                });
            });
          }
        }
      });
    },
    // 订单对应用户信息
    userListOne(e) {
      return new Promise((resolve, reject) => {
        user.userListOne(e).then(res => {
          // console.log(res);
          if (res.code == "0000") {
            resolve(res.data[0]);
          }
        });
      });
    },
    // 订单对应商铺信息
    businessListOne(e) {
      return new Promise((resolve, reject) => {
        business.bussinessListOne(e).then(res => {
          if (res.code == "0000") {
            resolve(res.data[0]);
          }
        });
      });
    },
    // 分页方法
    handleCurrentChange(cpage) {
      this.currpage = cpage;
    },
    handleSizeChange(psize) {
      this.pagesize = psize;
    },
    // 删除订单
    handleDel(index, row) {
      order.orderListDel(row).then(res => {
        if(res.code == "0000"){
          this.initData()
          this.$message({
            message: res.msg,
            type: "success"
          });
        }else{
          this.$message({
            message: res.msg,
            type: "success"
          });
        }
      })
    },
    // 退单
    handleWithdraw(index, row) {
      let ret = deepClone(row);
      if (ret.order_status != "退单中") {
        ret.order_status = "退单中";
        this.submit(ret);
      } else {
        this.$message({
          message: "操作错误",
          type: "error"
        });
        return
      }
    },
    // 提交订单修改
    submit(ret) {
      // console.log(this.form)
      order.orderListEdit(ret).then(res => {
        if (res.code == "0000") {
          this.initData();
          this.dialogFormVisible = false;
          this.$message({
            message: res.msg,
            type: "success"
          });
        } else {
          this.$message({
            message: res.msg,
            type: "error"
          });
        }
      });
    }
  }
};
</script>

<style lang="less">
@import "../../style/mixin";
.table_container {
  padding: 20px 0;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>
