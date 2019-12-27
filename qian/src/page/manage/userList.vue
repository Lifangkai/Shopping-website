<template>
  <div class="fillcontain">
    <head-top></head-top>
    <div class="table_container">
      <el-input v-model="search" class="elipu" placeholder="输入关键字搜索" />
      <el-table
        :data="dataList.filter(data => !search || data.user_name.toLowerCase().includes(search.toLowerCase()))"
        highlight-current-row
        style="width: 100%"
      >
        <el-table-column type="index" width="100"></el-table-column>
        <el-table-column property="user_time" label="注册日期" width="220"></el-table-column>
        <el-table-column property="user_name" label="用户姓名" width="220"></el-table-column>
        <el-table-column property="user_address" label="注册地址"></el-table-column>
        <el-table-column label="操作" align="right">
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
    <el-dialog title="用户信息" :visible.sync="dialogFormVisible" style="width:80%;margin:0 auto">
      <el-form :model="form">
        <el-form-item label="用户姓名" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.store_name" autocomplete="off"></el-input> -->
          {{ form.user_name }}
        </el-form-item>
        <el-form-item label="用户地址" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.store_address" autocomplete="off"></el-input> -->
          {{ form.user_address }}
        </el-form-item>
        <el-form-item label="用户密码" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.store_pwd" autocomplete="off" type="password" disabled></el-input> -->
          {{ form.user_pwd }}
        </el-form-item>
        <el-form-item label="创建时间" :label-width="formLabelWidth">
          <!-- <el-input v-model="form.store_time" autocomplete="off"></el-input> -->
          {{ form.user_time }}
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
import { user } from "@/api/api.js";
export default {
  data() {
    return {
      tableData: [],
      currpage: 1,
      pagesize: 10,
      search: "",
      dialogFormVisible: false,
      dialogWarnVisible: false,
      form: {},
      textarea2: "",
      formLabelWidth: "120px",
      uid: ""
    };
  },
  components: {
    headTop
  },
  created() {
    this.initData();
  },
  methods: {
    // 初始化数据
    initData() {
      user.userListAll().then(res => {
        // console.log(res);
        if (res.code == "0000") {
          this.tableData = res.data;
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
    // 用户详情
    handleClick(index, row) {
      // console.log(index, row);
      this.dialogFormVisible = true;
      this.form = row;
    },
    // 用户删除
    handleDelete(index, row) {
      // console.log(index, row);
      let params = row;
      user.userListDel(params).then(res => {
        if (res.code == "0000") {
          this.initData();
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
    },
    // 用户预警
    handleWarn(index, row) {
      this.dialogWarnVisible = true;
      this.uid = row.uid;
    },
    // 提交预警信息
    submitWarn() {
      if (this.uid == "" || this.user_content == "") {
        return;
      }
      let params = {
        uid: this.uid,
        user_content: this.textarea2
      };
      user.userListWarnAdd(params).then(res => {
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
    },
    // 删除预警
    handleWarnDel(index, row) {
      console.log(row);
      user.userListWarnDel(row).then(res => {
        if (res.code == "0000") {
          this.$message({
            message: res.msg,
            type: "success"
          });
          this.initData()
        } else {
          this.$message({
            type: "error",
            message: res.msg
          });
        }
      });
    }
  },
  computed: {
    dataList() {
      return this.tableData.slice(
        (this.currpage - 1) * this.pagesize,
        this.currpage * this.pagesize
      );
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
