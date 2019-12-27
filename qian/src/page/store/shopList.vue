<template>
  <div class="fillcontain">
    <head-top></head-top>
    <div class="form_container">
      <el-form label-position="right" label-width="80px" :model="formLabelAlign">
        <h2 style="width:100%;textAlign:center;marginBottom:20px">店铺详情</h2>
        <el-form-item label="店铺id">
          <el-input v-model="formLabelAlign.bid" disabled></el-input>
        </el-form-item>
        <el-form-item label="店铺名称">
          <el-input v-model="formLabelAlign.bus_name"></el-input>
        </el-form-item>
        <el-form-item label="店铺分类">
          <!-- <el-input v-model="formLabelAlign.bus_class"></el-input> -->
          <el-cascader v-model="value" :options="options" @change="handleChange"></el-cascader>
        </el-form-item>
        <el-form-item label="店铺介绍">
          <el-input v-model="formLabelAlign.bus_introduction"></el-input>
        </el-form-item>
        <el-form-item label="店铺地址">
          <el-input v-model="formLabelAlign.bus_address"></el-input>
        </el-form-item>
        <el-form-item label="店铺电话">
          <el-input v-model="formLabelAlign.bus_phone"></el-input>
        </el-form-item>
        <el-form-item label="店铺评分">
          <el-input v-model="formLabelAlign.bus_score" disabled></el-input>
        </el-form-item>
        <el-form-item label="店铺月销量">
          <el-input v-model="formLabelAlign.bus_sell" disabled></el-input>
        </el-form-item>
        <el-form-item label="店铺头像">
          <!-- <el-input v-model="formLabelAlign.bus_avator"></el-input> -->
          <el-upload
            class="avatar-uploader"
            :action="base + '/businesslist/queryimg/'"
            :data="formLabelAlign"
            :on-success="uploadImg"
            :show-file-list="false"
          >
            <img
              v-if="formLabelAlign.bus_avator"
              :src="bussinessImageUrl + formLabelAlign.bus_avator"
              class="avatar"
            />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="updateShop">立即修改</el-button>
          <el-button type="danger" @click="handleDelete">删除店铺</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import headTop from "../../components/headTop";
import { deepClone } from "../comm_func.js";
import {
  store,
  business,
  comment,
  base,
  bussinessImageUrl
} from "@/api/api.js";
export default {
  data() {
    return {
      base,
      bussinessImageUrl,
      formLabelAlign: {},
      value: [],
      options: [
        {
          value: "fushi",
          label: "服饰",
          children: [
            {
              value: "nanzhuang",
              label: "男装"
            },
            {
              value: "nvzhuang",
              label: "女装"
            },
            {
              value: "nanxie",
              label: "男鞋"
            },
            {
              value: "nvxie",
              label: "女鞋"
            },
            {
              value: "huwai",
              label: "户外"
            }
          ]
        },
        {
          value: "meizhuang",
          label: "美妆",
          children: [
            {
              value: "hufu",
              label: "护肤"
            },
            {
              value: "caizhuang",
              label: "彩妆"
            },
            {
              value: "xiangshui",
              label: "香水"
            },
            {
              value: "nanshi",
              label: "男士"
            }
          ]
        },
        {
          value: "chaoshi",
          label: "超市",
          children: [
            {
              value: "shipinyinliao",
              label: "食品饮料"
            },
            {
              value: "liangyoufushi",
              label: "粮油副食"
            },
            {
              value: "jiajuqingjie",
              label: "家居清洁"
            },
            {
              value: "jujiashenghuo",
              label: "居家生活"
            }
          ]
        },
        {
          value: "quanqiugou",
          label: "全球购",
          children: [
            {
              value: "naifenfushi",
              label: "奶粉辅食"
            },
            {
              value: "xihuyongpin",
              label: "洗护用品"
            },
            {
              value: "yingyangbaojian",
              label: "营养保健"
            },
            {
              value: "zhongbiaoshoushi",
              label: "钟表首饰"
            }
          ]
        }
      ]
    };
  },
  mounted() {
    this.initData();
    // console.log(this.formLabelAlign);
  },
  components: {
    headTop
  },
  computed: {
    storeinfo() {
      return JSON.parse(this.$store.state.storeinfo);
    },
    userroot() {
      return this.$store.state.userroot;
    }
  },
  methods: {
    //级联选择器
    handleChange(value) {},
    //图片上传成功
    uploadImg(res) {
      if (res.code == "0000") {
        this.formLabelAlign.bus_avator = res.data;
      }
    },
    //初始化数据
    initData() {
      let params = { sid: this.storeinfo.sid };
      let data = [];
      new Promise((resolve, reject) => {
        business.bussinessListAll(params).then(res => {
          if (res.code == "0000") {
            let tableData = res.data[0];
            resolve(tableData);
          }
        });
      }).then(tableData => {
        comment.bussComm(tableData).then(res => {
          if (res.code == "0000") {
            let datas = res.data[0];
            data.push({
              bid: tableData["bid"],
              sid: tableData["sid"],
              bus_address: tableData["bus_address"],
              bus_avator: tableData["bus_avator"],
              bus_class: tableData["bus_class"],
              bus_introduction: tableData["bus_introduction"],
              bus_name: tableData["bus_name"],
              bus_phone: tableData["bus_phone"],
              bus_score: datas["bus_score"],
              bus_sell: datas["bus_sell"]
            });
            this.formLabelAlign = data[0];
            this.value = JSON.parse(this.formLabelAlign.bus_class);
          }
        });
      });
    },
    // 删除商家
    handleDelete() {
      business.bussinessDel(this.formLabelAlign).then(res => {
        if (res.code == "0000") {
          this.$store.commit("setIsShow", false);
          sessionStorage.setItem("isShowShop",false)
          let params = deepClone(this.storeinfo);
          params.bid = "";
          store.storeListEdit(params).then(res => {
            if (res.code == "0000") {
              // debugger
              console.log(JSON.stringify(params))
              this.$store.commit("setStoreInfo", JSON.stringify(params));
              sessionStorage.setItem("storeinfo",JSON.stringify(params));
              // this.initData();
              this.$message({
                type: "success",
                message: res.msg
              });
              this.$router.push({ path: "/addShop" });
            }
          });
        } else {
          this.$message({
            type: "error",
            message: res.msg
          });
        }
      });
    },
    // 提交修改表格
    updateShop() {
      let params = deepClone(this.formLabelAlign);
      params.bus_class = JSON.stringify(this.value);
      business.bussinessEdit(params).then(res => {
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
    }
  }
};
</script>

<style lang="less">
@import "../../style/mixin";
.form_container {
  width: 50%;
  margin: 50px auto 0;
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
</style>
