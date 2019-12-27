<template>
  <div class="fillcontain">
    <head-top></head-top>
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
            <el-button size="small" @click="handleEdit(scope.$index, scope.row)">修改</el-button>
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
    <el-dialog title="订单修改" :visible.sync="dialogFormVisible" style="width:80%;margin:0 auto">
      <el-form :model="form">
        <el-form-item label="订单id" :label-width="formLabelWidth">
          <el-input v-model="form.oid" autocomplete="off" disabled></el-input>
          <!-- {{ form.oid }} -->
        </el-form-item>
        <el-form-item label="用户名" :label-width="formLabelWidth">
          <el-input v-model="form.user_name" autocomplete="off" disabled></el-input>
          <!-- {{ form.user_address }} -->
        </el-form-item>
        <el-form-item label="总价格" :label-width="formLabelWidth">
          <el-input v-model="form.order_allprice" autocomplete="off"></el-input>
          <!-- {{ form.user_pwd }} -->
        </el-form-item>
        <el-form-item label="收货地址" :label-width="formLabelWidth">
          <el-input v-model="form.bus_address" autocomplete="off"></el-input>
          <!-- {{ form.user_time }} -->
        </el-form-item>
        <el-form-item label="订单状态" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.order_status" autocomplete="off"></el-input> -->
          <!-- {{ form.user_time }} -->
          <el-select v-model="form.order_status" placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
              :disabled="item.disabled"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import headTop from "../../components/headTop";
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
          value: "商家准备",
          label: "商家准备"
        },
        {
          value: "已发货",
          label: "已发货"
        },
        {
          value: "快递中",
          label: "快递中"
        },
        {
          value: "用户收到",
          label: "用户收到"
        },
        {
          value: "退单中",
          label: "退单中",
          disabled: true
        },
        {
          value: "退单完成",
          label: "退单完成"
        }
      ],
      dialogFormVisible: false
    };
  },
  components: {
    headTop
  },
  mounted() {
    // this.restaurant_id = this.$route.query.restaurant_id;
    this.initData();
  },
  computed: {
    storeinfo() {
      return JSON.parse(this.$store.state.storeinfo);
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
      let params = { bid: this.storeinfo.bid };
      let tableListData = [];
      order.orderListAll(params).then(res => {
        if (res.code == "0000") {
          let orderData = res.data;
          for (var i = 0; i < orderData.length; i++) {
            let e = orderData[i];
            user.userListOne(e).then(res => {
              if (res.code == "0000") {
                let data = {};
                (data.oid = e["oid"]),
                  (data.bid = e["bid"]),
                  (data.uid = e["uid"]),
                  (data.order_allprice = e["order_allprice"]),
                  (data.order_status = e["order_status"]),
                  (data.user_name = res.data[0]["user_name"]);
                business.bussinessListOne(data).then(res => {
                  if (res.code == "0000") {
                    data.bus_name = res.data[0]["bus_name"];
                    data.bus_address = res.data[0]["bus_address"];
                    data.bid = res.data[0]["bid"];
                    tableListData.push(data);
                    this.tableData = tableListData;
                  }
                });
              }
            });
          }
        }
      });
    },
    // 分页方法
    handleCurrentChange(cpage) {
      this.currpage = cpage;
    },
    handleSizeChange(psize) {
      this.pagesize = psize;
    },
    // 编辑订单信息
    handleEdit(index, row) {
      this.dialogFormVisible = true;
      this.form = deepClone(row);
    },
    // 提交订单修改
    submit() {
      // console.log(this.form)
      order.orderListEdit(this.form).then(res => {
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
  padding: 20px;
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
