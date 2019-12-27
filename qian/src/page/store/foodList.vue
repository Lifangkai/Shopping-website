<template>
  <div class="fillcontain">
    <head-top></head-top>
    <div class="table_container">
      <el-input v-model="search" class="elipu" placeholder="输入关键字搜索" />
      <el-table
        :data="dataList.filter(data => !search || data.food_name.toLowerCase().includes(search.toLowerCase()))"
        style="width: 100%"
      >
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="食品名称">
                <span>{{ props.row.food_name }}</span>
              </el-form-item>
              <el-form-item label="餐馆名称">
                <span>{{ props.row.bus_name }}</span>
              </el-form-item>
              <el-form-item label="食品 ID">
                <span>{{ props.row.fid }}</span>
              </el-form-item>
              <el-form-item label="餐馆 ID">
                <span>{{ props.row.bid }}</span>
              </el-form-item>
              <el-form-item label="食品介绍">
                <span>{{ props.row.food_introduction }}</span>
              </el-form-item>
              <el-form-item label="餐馆地址">
                <span>{{ props.row.bus_address }}</span>
              </el-form-item>
              <el-form-item label="食品评分">
                <span>{{ props.row.food_score }}</span>
              </el-form-item>
              <el-form-item label="食品分类">
                <span>{{ props.row.food_class }}</span>
              </el-form-item>
              <el-form-item label="月销量">
                <span>{{ props.row.food_sell }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="食品名称" prop="food_name"></el-table-column>
        <el-table-column label="食品介绍" prop="food_introduction"></el-table-column>
        <el-table-column label="评分" prop="food_score"></el-table-column>
        <el-table-column label="操作" width="160">
          <template slot-scope="scope">
            <el-button size="small" @click="handleEdit(scope.$index,scope.row)">编辑</el-button>
            <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="Pagination">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currpage"
          :page-size="20"
          layout="total, prev, pager, next, jumper"
          :total="tableData.length"
        ></el-pagination>
      </div>

      <el-dialog title="修改食品信息" v-model="dialogFormVisible">
        <el-form :model="selectTable">
          <el-form-item label="食品名称" label-width="100px">
            <el-input v-model="selectTable.food_name" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="食品介绍" label-width="100px">
            <el-input v-model="selectTable.food_introduction"></el-input>
          </el-form-item>
          <el-form-item label="食品分类" label-width="100px">
            <el-select v-model="SelectValue" @change="handleSelect">
              <el-option
                v-for="(item,index) in menuOptions"
                :key="index"
                :label="item.value"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="食品图片" label-width="100px">
            <el-upload
              class="avatar-uploader"
              :action="base + '/foodlist/queryimg/'"
              :data="selectTable"
              :show-file-list="false"
              :on-success="handleServiceAvatarScucess"
            >
              <img
                v-if="selectTable.food_avator"
                :src="foodImageUrl + selectTable.food_avator"
                class="avatar"
              />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
        </el-form>
        <el-row style="overflow: auto; text-align: center;">
          <el-table :data="specs" style="margin-bottom: 20px;" :row-class-name="tableRowClassName">
            <el-table-column prop="specs" label="规格"></el-table-column>
            <el-table-column prop="packing_fee" label="包装费"></el-table-column>
            <el-table-column prop="price" label="价格"></el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                <el-button size="small" type="danger" @click="deleteSpecs(scope.$index)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-button
            type="primary"
            @click="specsFormVisible = true"
            style="margin-bottom: 10px;"
          >添加规格</el-button>
        </el-row>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="updateFood">确 定</el-button>
        </div>
      </el-dialog>

      <el-dialog title="添加规格" v-model="specsFormVisible">
        <el-form :rules="specsFormrules" :model="specsForm">
          <el-form-item label="规格" label-width="100px" prop="specs">
            <el-input v-model="specsForm.specs" auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="包装费" label-width="100px">
            <el-input-number v-model="specsForm.packing_fee" :min="0" :max="100"></el-input-number>
          </el-form-item>
          <el-form-item label="价格" label-width="100px">
            <el-input-number v-model="specsForm.price" :min="0" :max="10000"></el-input-number>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="specsFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="addspecs">确 定</el-button>
        </div>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import headTop from "../../components/headTop";
import { deepClone } from "../comm_func.js";
import { food, comment, business, base, foodImageUrl } from "@/api/api.js";
export default {
  data() {
    return {
      base,
      foodImageUrl,
      search: "",
      restaurant_id: null,
      tableData: [],
      pagesize: 10,
      currpage: 1,
      selectTable: {},
      dialogFormVisible: false,
      specs: [],
      menuOptions: [
        {
          value: "食品区",
          label: "食品区",
          description: "shipin"
        },
        {
          value: "护肤品区",
          label: "护肤品区",
          description: "hufupin"
        },
        {
          value: "纺织区",
          label: "纺织区",
          description: "fangzhi"
        },
        {
          value: "妇婴区",
          label: "妇婴区",
          description: "fuying"
        },
        {
          value: "零食区",
          label: "零食区",
          description: "lingshi"
        },
        {
          value: "冻饮区",
          label: "冻饮区",
          description: "dongyin"
        },
        {
          value: "热饮区",
          label: "热饮区",
          description: "reyin"
        },
        {
          value: "日用品区",
          label: "日用品区",
          description: "riyongpin"
        }
      ],
      selectMenu: {},
      SelectValue: "",
      specsForm: {
        specs: "",
        packing_fee: 0,
        price: 20
      },
      specsFormrules: {
        specs: [{ required: true, message: "请输入规格", trigger: "blur" }]
      },
      specsFormVisible: false,
      expendRow: []
    };
  },
  mounted() {
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
  components: {
    headTop
  },
  watch: {
    $route() {
      this.initData();
    }
  },
  methods: {
    // 初始化数据
    initData() {
      let params = { bid: this.storeinfo.bid };
      let tableListData = [];
      food.foodListAll(params).then(res => {
        if (res.code == "0000") {
          let foodData = res.data;
          for (var i = 0; i < foodData.length; i++) {
            let e = foodData[i];
            comment.foodComm(e).then(res => {
              if (res.code == "0000") {
                let data = {};
                (data.fid = e["fid"]),
                  (data.bid = e["bid"]),
                  (data.food_name = e["food_name"]),
                  (data.food_avator = e["food_avator"]),
                  (data.food_introduction = e["food_introduction"]),
                  (data.food_other = e["food_other"]),
                  (data.food_class = e["food_class"]),
                  (data.food_score = res.data[0]["food_score"]),
                  (data.food_sell = res.data[0]["food_sell"]);
                  business.bussinessListOne(data).then(res => {
                  if (res.code == "0000") {
                    data.bus_name = res.data[0]["bus_name"];
                    data.bus_address = res.data[0]["bus_address"];
                    tableListData.push(data);
                    this.tableData = tableListData;
                    // console.log(this.tableData)
                  }
                });
              }
            });
          }
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
    // 规格信息提交
    addspecs() {
      this.specs.push({ ...this.specsForm });
      this.specsForm.specs = "";
      this.specsForm.packing_fee = 0;
      this.specsForm.price = 20;
      this.specsFormVisible = false;
    },
    deleteSpecs(index) {
      this.specs.splice(index, 1);
    },
    handleCurrentChange(cpage) {
      this.currpage = cpage;
    },
    handleSizeChange(psize) {
      this.pagesize = psize;
    },
    // 编辑食物数据
    handleEdit(index, row) {
      //   this.getSelectItemData(row, "edit");
      this.dialogFormVisible = true;
      this.selectTable = deepClone(row);
      // console.log(row)
      this.SelectValue = this.selectTable.food_class
      // console.log(this.SelectValue)
      this.specs = JSON.parse(this.selectTable.food_other);
    },
    handleSelect(val) {
    },
    // 删除食物数据
    handleDelete(index, row) {
      let params = { bid: row.bid, fid: row.fid };
      food.foodListDel(params).then(res => {
        if (res.code == "0000") {
          this.tableData.splice(index, 1);
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
    // 图片上传成功后
    handleServiceAvatarScucess(res) {
      if (res.code == "0000") {
        this.selectTable.food_avator = res.data;
      }
    },
    updateFood() {
      let data = JSON.stringify(this.specs);
      this.selectTable.food_other = data;
      this.selectTable.food_class = this.SelectValue
      food.foodListEdit(this.selectTable).then(res => {
        if (res.code == "0000") {
          this.initData();
          this.dialogFormVisible = false;
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
.table_container {
  padding: 20px;
}
.Pagination {
  display: flex;
  justify-content: flex-start;
  margin-top: 8px;
}
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #20a0ff;
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
.elipu {
  width: 50%;
  margin: 20px auto;
}
</style>
