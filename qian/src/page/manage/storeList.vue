<template>
  <div class="fillcontain">
    <head-top></head-top>
    <div class="table_container">
      <el-input v-model="search" class="elipu" placeholder="输入关键字搜索" />
      <el-table
        :data="dataList.filter(data => !search || data.store_name.toLowerCase().includes(search.toLowerCase()))"
        style="width: 100%"
      >
        <el-table-column label="创建时间" prop="store_time"></el-table-column>
        <el-table-column label="商家名称" prop="store_name"></el-table-column>
        <el-table-column label="商家地址" prop="store_address"></el-table-column>
        <el-table-column label="操作" align="right">
          <!-- <template slot="header" slot-scope="scope"> -->
          <!-- <el-input v-model="search" size="mini" placeholder="输入关键字搜索" /> -->
          <!-- </template> -->
          <template slot-scope="scope">
            <el-button size="small" type="warning" @click="handleWarn(scope.$index, scope.row)">预警</el-button>
            <el-button size="small" type="info" @click="handleWarnDel(scope.$index, scope.row)">删除预警</el-button>
            <el-button size="small" @click="handleClick(scope.$index, scope.row)">详情</el-button>
            <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
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
    <el-dialog title="商家信息" :visible.sync="dialogFormVisible" style="width:80%;margin:0 auto">
      <el-form :model="form">
        <el-form-item label="商家姓名" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.store_name" autocomplete="off"></el-input> -->
          {{ form.store_name }}
        </el-form-item>
        <el-form-item label="商家地址" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.store_address" autocomplete="off"></el-input> -->
          {{ form.store_address }}
        </el-form-item>
        <el-form-item label="商家密码" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.store_pwd" autocomplete="off" type="password" disabled></el-input> -->
          {{ form.store_pwd }}
        </el-form-item>
        <el-form-item label="创建时间" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.store_time" autocomplete="off"></el-input> -->
          {{ form.store_time }}
        </el-form-item>
        <el-form-item label="店铺名称" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.bid" autocomplete="off"></el-input> -->
          {{ business }}
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <!-- <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button> -->
      </div>
    </el-dialog>
    <el-dialog title="预警信息" :visible.sync="dialogWarnVisible" style="width:80%;margin:0 auto">
      <el-input
        type="textarea"
        :autosize="{ minRows: 4, maxRows: 8}"
        placeholder="请输入内容"
        v-model="textarea2"
      ></el-input>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogWarnVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitWarn">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
import headTop from "../../components/headTop";
import { store, business } from "@/api/api.js";
export default {
  data() {
    return {
      tableData: [],
      search: "",
      dialogFormVisible: false,
      dialogWarnVisible: false,
      form: {},
      formLabelWidth: "120px",
      business: "",
      currpage: 1,
      pagesize: 10,
      textarea2: "",
      sid: ""
    };
  },
  components: {
    headTop
  },
  mounted() {
    this.initData();
  },
  computed: {
    dataList(){
          // this.tableData.filter(data => !search || data.store_name.toLowerCase().includes(search.toLowerCase()))
          return this.tableData.slice((this.currpage - 1)*this.pagesize,this.currpage*this.pagesize)
      }
  },
  methods: {
    // 初始化数据
    initData() {
      store.storeListAll().then(res => {
        if (res.code == "0000") {
          this.tableData = res.data;
        }
      });
    },
    // 商家详情
    handleClick(index, row) {
      // console.log(index, row);
      this.dialogFormVisible = true;
      this.form = row;
      business.bussinessListOne(this.form).then(res => {
        // console.log(res);
        if (res.code == "0000") {
          this.business = res.data[0].bus_name;
        }
      });
    },
    // 商家删除
    handleDelete(index, row) {
      // console.log(index, row);
      let params = row
      store.storeListDel(params).then(res => {
        if(res.code == "0000"){
          this.$message({
              type: "success",
              message: res.msg
            });
            this.initData()
        }else {
          this.$message({
              type: "error",
              message: res.msg
            });
        }
      })
    },
    // 分页方法
    handleCurrentChange(cpage) {
      this.currpage = cpage;
    },
    handleSizeChange(psize) {
      this.pagesize = psize;
    },
    // 商家预警
    handleWarn(index, row) {
      this.dialogWarnVisible = true;
      this.sid = row.sid;
    },
    // 删除预警
    handleWarnDel(index,row) {
      store.storeListWarnDel(row).then(res => {
        if(res.code == "0000"){
          this.$message({
          message: res.msg,
          type: 'success'
        });
        this.initData()
        } else {
          this.$message({
            type: "error",
            message: res.msg
          });
        }
      })
    },
    // 提交预警信息
    submitWarn() {
      if(this.sid == "" || this.store_content == ""){
          return
      }
      let params = {
        sid: this.sid,
        store_content: this.textarea2
      };
      store.storeListWarnAdd(params).then(res => {
        if (res.code == "0000") {
          this.dialogWarnVisible = false;
          this.$message({
            type: "success",
            message: res.msg
          });
        } else {
          this.$message({
            type: "error",
            message: res.msg
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
.elipu {
  width: 50%;
  margin: 20px auto;
}
</style>