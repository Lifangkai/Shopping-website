<template>
  <div class="fillcontain">
    <head-top></head-top>
    <div class="table_container">
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="admin_name" label="姓名" width="180"></el-table-column>
        <el-table-column prop="admin_registertime" label="注册日期" width="220"></el-table-column>
        <el-table-column prop="admin_address" label="地址" width="180"></el-table-column>
        <el-table-column prop="admin_authority" label="权限"></el-table-column>
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
  </div>
</template>

<script>
import headTop from "../../components/headTop";
import { admin } from "@/api/api.js";
export default {
  data() {
    return {
      pagesize: 10,
      tableData: [],
      currpage: 1
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
    initData() {
      admin.AdminListAll().then(res => {
        if (res.code == "0000") {
          this.tableData = res.data;
          console.log(this.tableData)
        }
      });
    },
    // 分页方法
    handleCurrentChange(cpage) {
      this.currpage = cpage;
    },
    handleSizeChange(psize) {
      this.pagesize = psize;
    }
  }
};
</script>

<style lang="less">
@import "../../style/mixin";
.table_container {
  padding: 20px;
}
</style>


