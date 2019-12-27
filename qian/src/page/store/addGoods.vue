<template>
  <div>
    <head-top></head-top>
    <el-row style="margin-top: 20px;">
      <el-col :span="14" :offset="4">
        <header class="form_header">选择商品种类</header>
        <el-form :model="categoryForm" ref="categoryForm" label-width="110px" class="form">
          <el-row class="category_select">
            <el-form-item label="商品种类">
              <el-select
                v-model="categoryValue"
                placeholder="请选择商品种类"
                style="width:100%;"
                @change="handleClick"
              >
                <el-option
                  v-for="(item,index) in categorySelect"
                  :key="index"
                  :label="item.label"
                  :value="index"
                ></el-option>
              </el-select>
            </el-form-item>
          </el-row>
          <el-row class="add_category_row" :class="showAddCategory? 'showEdit': ''">
            <div class="add_category">
              <el-form-item label="商品种类" prop="name">
                <el-input v-model="categoryForm.name"></el-input>
              </el-form-item>
              <el-form-item label="种类描述" prop="description">
                <el-input v-model="categoryForm.description"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitcategoryForm()">提交</el-button>
              </el-form-item>
            </div>
          </el-row>
          <div class="add_category_button" @click="addCategoryFun">
            <i class="el-icon-caret-top edit_icon" v-if="showAddCategory"></i>
            <i class="el-icon-caret-bottom edit_icon" v-else slot="icon"></i>
            <span>添加商品种类</span>
          </div>
        </el-form>
        <header class="form_header">添加商品</header>
        <el-form
          :model="foodForm"
          :rules="foodrules"
          ref="foodForm"
          label-width="110px"
          class="form food_form"
        >
          <el-form-item label="商品名称" prop="name">
            <el-input v-model="foodForm.food_name"></el-input>
          </el-form-item>
          <el-form-item label="商品活动" prop="activity">
            <el-input v-model="foodForm.food_activity"></el-input>
          </el-form-item>
          <el-form-item label="商品详情" prop="description">
            <el-input v-model="foodForm.food_introduction"></el-input>
          </el-form-item>
          <el-form-item label="上传商品图片">
            <el-upload
              class="avatar-uploader"
              :action="base + '/foodlist/queryimg/'"
              :data="foodForm"
              :show-file-list="false"
              :on-success="uploadImg"
            >
              <img
                v-if="foodForm.food_avator"
                :src="foodImageUrl + foodForm.food_avator"
                class="avatar"
              />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
          <el-form-item label="商品特点">
            <el-select v-model="foodForm.food_characteristic" multiple placeholder="请选择">
              <el-option
                v-for="item in attributes"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="商品规格">
            <el-radio class="radio" v-model="foodSpecs" label="one">单规格</el-radio>
            <el-radio class="radio" v-model="foodSpecs" label="more">多规格</el-radio>
          </el-form-item>
          <el-row v-if="foodSpecs == 'one'">
            <el-form-item label="包装费">
              <el-input-number v-model="specsForm.packing_fee" :min="0" :max="100"></el-input-number>
            </el-form-item>
            <el-form-item label="价格">
              <el-input-number v-model="specsFormrules.price" :min="0" :max="10000"></el-input-number>
            </el-form-item>
          </el-row>
          <el-row v-else style="overflow: auto; text-align: center;">
            <el-button
              type="primary"
              @click="dialogFormVisible = true"
              style="margin-bottom: 10px;"
            >添加规格</el-button>
            <el-table
              :data="foodForm.food_other"
              style="margin-bottom: 20px;"
              :row-class-name="tableRowClassName"
            >
              <el-table-column prop="specs" label="规格"></el-table-column>
              <el-table-column prop="packing_fee" label="包装费"></el-table-column>
              <el-table-column prop="price" label="价格"></el-table-column>
              <el-table-column label="操作">
                <template slot-scope="scope">
                  <el-button size="small" type="danger" @click="handleDelete(scope.$index)">删除</el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-row>
          <el-form-item>
            <el-button type="primary" @click="addFood()">确认添加商品</el-button>
          </el-form-item>
        </el-form>
        <el-dialog title="添加规格" v-model="dialogFormVisible">
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
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="addspecs">确 定</el-button>
          </div>
        </el-dialog>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import headTop from "@/components/headTop";
import { comment, food, base, foodImageUrl } from "@/api/api.js";
// import { baseUrl, baseImgPath } from "@/config/env";
import { deepClone, createId } from "../comm_func.js";
export default {
  data() {
    return {
      base,
      foodImageUrl,
      categoryValue: "",
      categorySelect: [
        {
          value: "",
          label: "食品区",
          description: "shipin"
        },
        {
          value: "",
          label: "护肤品区",
          description: "hufupin"
        },
        {
          value: "",
          label: "纺织区",
          description: "fangzhi"
        },
        {
          value: "",
          label: "妇婴区",
          description: "fuying"
        },
        {
          value: "",
          label: "零食区",
          description: "lingshi"
        },
        {
          value: "",
          label: "冻饮区",
          description: "dongyin"
        },
        {
          value: "",
          label: "热饮区",
          description: "reyin"
        },
        {
          value: "",
          label: "日用品区",
          description: "riyongpin"
        }
      ],
      categoryForm: {
        name: "",
        description: ""
      },
      foodForm: {
        fid: "",
        bid: "",
        food_name: "",
        food_activity: "",
        food_introduction: "",
        food_class: "",
        food_class_detail: "",
        food_characteristic: [],
        food_other: [],
        food_avator: ""
      },
      foodrules: {
        food_name: [
          { required: true, message: "请输入商品名称", trigger: "blur" }
        ]
      },
      attributes: [
        {
          value: "新品",
          label: "新品"
        },
        {
          value: "招牌",
          label: "招牌"
        }
      ],
      showAddCategory: false,
      foodSpecs: "one",
      dialogFormVisible: false,
      specsForm: {
        specs: "",
        packing_fee: 0,
        price: 20
      },
      specsFormrules: {
        specs: [{ required: true, message: "请输入规格", trigger: "blur" }]
      },
    };
  },
  components: {
    headTop
  },
  mounted() {
    this.initData()
  },
  computed: {
    storeinfo(){
      return JSON.parse(this.$store.state.storeinfo)
    },
    userroot() {
      return this.$store.state.userroot;
    }
  },
  watch: {},
  methods: {
    // 选中商品种类
    handleClick(index) {
      // console.log(index)
      this.foodForm.food_class = this.categorySelect[index].label;
      this.foodForm.food_class_detail = this.categorySelect[index].description;
    },
    // 初始化数据
    initData() {
      this.foodForm = {
        fid: "",
        bid: "",
        food_name: "",
        food_activity: "",
        food_introduction: "",
        food_class: "",
        food_class_detail: "",
        food_characteristic: [],
        food_other: [],
        food_avator: ""
      }
      this.specsForm = {
        specs: "",
        packing_fee: 0,
        price: 20
      }
      this.foodForm.bid = this.storeinfo.bid;
      this.foodForm.fid = createId();
      this.categoryValue = ""
    },
    // 添加商品种类
    addCategoryFun() {
      this.showAddCategory = !this.showAddCategory;
    },
    // 提交商品种类
    submitcategoryForm() {
      this.categorySelect.push({
        label: this.categoryForm.name,
        description: this.categoryForm.description
      });
      this.$message({
        message: "添加商品种类成功",
        type: "success"
      });
    },
    // 上传图片
    uploadImg(res) {
      if (res.code == "0000") {
        this.foodForm.food_avator = res.data;
      }
    },
    // 添加规格
    addspecs() {
      this.foodForm.food_other.push({ ...this.specsForm });
      this.specsForm.specs = "";
      this.specsForm.packing_fee = 0;
      this.specsForm.price = 20;
      this.dialogFormVisible = false;
    },
    // 删除规格
    handleDelete(index) {
      this.foodForm.food_other.splice(index, 1);
    },
    tableRowClassName(row, index) {
      if (index === 1) {
        return "info-row";
      } else if (index === 3) {
        return "positive-row";
      }
      return "";
    },
    // 确认添加商品
    addFood() {
      let params = deepClone(this.foodForm);
      if (this.foodSpecs == "one") {
        (params.food_other = []), params.food_other.push(this.specsForm);
        params.food_other[0].specs = "one";
      }
      params.food_other = JSON.stringify(params.food_other);
      params.food_characteristic = JSON.stringify(params.food_characteristic);
      new Promise((resolve, reject) => {
        food.foodListAdd(params).then(res => {
          if (res.code == "0000") {
            resolve(params);
          }
        });
      }).then(params => {
        comment.foodAdd(params).then(res => {
          if (res.code == "0000") {
            this.initData()
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
      });
    }
  }
};
</script>

<style lang="less">
@import "../../style/mixin";
.form {
  min-width: 400px;
  margin-bottom: 30px;
  &:hover {
    box-shadow: 0 0 8px 0 rgba(232, 237, 250, 0.6),
      0 2px 4px 0 rgba(232, 237, 250, 0.5);
    border-radius: 6px;
    transition: all 400ms;
  }
}
.food_form {
  border: 1px solid #eaeefb;
  padding: 10px 10px 0;
}
.form_header {
  text-align: center;
  margin-bottom: 10px;
}
.category_select {
  border: 1px solid #eaeefb;
  padding: 10px 30px 10px 10px;
  border-top-right-radius: 6px;
  border-top-left-radius: 6px;
}
.add_category_row {
  height: 0;
  overflow: hidden;
  transition: all 400ms;
  background: #f9fafc;
}
.showEdit {
  height: 185px;
}
.add_category {
  background: #f9fafc;
  padding: 10px 30px 0px 10px;
  border: 1px solid #eaeefb;
  border-top: none;
}
.add_category_button {
  text-align: center;
  line-height: 40px;
  border-bottom-right-radius: 6px;
  border-bottom-left-radius: 6px;
  border: 1px solid #eaeefb;
  border-top: none;
  transition: all 400ms;
  &:hover {
    background: #f9fafc;
    span,
    .edit_icon {
      color: #20a0ff;
    }
  }
  span {
    .sc(14px, #999);
    transition: all 400ms;
  }
  .edit_icon {
    color: #ccc;
    transition: all 400ms;
  }
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
.cell {
  text-align: center;
}
</style>
