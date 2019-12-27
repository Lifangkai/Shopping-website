<template>
  <div>
    <head-top></head-top>
    <el-row style="margin-top: 20px;">
      <el-col :span="12" :offset="4">
        <el-form
          :model="formData"
          :rules="rules"
          ref="formData"
          label-width="110px"
          class="demo-formData"
        >
          <el-form-item label="店铺名称" prop="bus_name">
            <el-input v-model="formData.bus_name"></el-input>
          </el-form-item>
          <el-form-item label="详细地址" prop="bus_address">
            <!-- <el-autocomplete -->
            <!-- v-model="formData.address" -->
            <!-- :fetch-suggestions="querySearchAsync" -->
            <!-- placeholder="请输入地址" -->
            <!-- style="width: 100%;" -->
            <!-- @select="addressSelect" -->
            <!-- ></el-autocomplete> -->
            <el-input v-model="formData.bus_address"></el-input>
            <!-- <span>当前城市：{{city.name}}</span> -->
          </el-form-item>
          <el-form-item label="联系电话" prop="bus_phone">
            <el-input v-model.number="formData.bus_phone"></el-input>
          </el-form-item>
          <el-form-item label="店铺简介" prop="bus_introduction">
            <el-input v-model="formData.bus_introduction"></el-input>
          </el-form-item>
          <el-form-item label="店铺标语" prop="bus_slogan">
            <el-input v-model="formData.bus_slogan"></el-input>
          </el-form-item>
          <el-form-item label="店铺分类">
            <el-cascader :options="categoryOptions" v-model="value"></el-cascader>
          </el-form-item>
          <el-form-item label="店铺特点" style="white-space: nowrap;">
            <span>品牌保证</span>
            <el-switch on-text off-text v-model="delivery_count.is_premium"></el-switch>
            <span>蜂鸟专送</span>
            <el-switch on-text off-text v-model="delivery_count.delivery_mode"></el-switch>
            <span>新开店铺</span>
            <el-switch on-text off-text v-model="delivery_count.new"></el-switch>
          </el-form-item>
          <el-form-item style="white-space: nowrap;">
            <span>外卖保</span>
            <el-switch on-text off-text v-model="delivery_count.bao"></el-switch>
            <span>准时达</span>
            <el-switch on-text off-text v-model="delivery_count.zhun"></el-switch>
            <span>开发票</span>
            <el-switch on-text off-text v-model="delivery_count.piao"></el-switch>
          </el-form-item>
          <el-form-item label="配送费" prop="bus_delivery">
            <el-input-number v-model="formData.bus_delivery" :min="0" :max="20"></el-input-number>
          </el-form-item>
          <el-form-item label="起送价" prop="bus_start_delivery">
            <el-input-number v-model="formData.bus_start_delivery" :min="0" :max="100"></el-input-number>
          </el-form-item>
          <el-form-item label="营业时间" style="white-space: nowrap;">
            <el-time-select
              placeholder="起始时间"
              v-model="formData.bus_start_time"
              :picker-options="{
							start: '05:30',
							step: '00:15',
							end: '23:30'
							}"
            ></el-time-select>
            <el-time-select
              placeholder="结束时间"
              v-model="formData.bus_end_time"
              :picker-options="{
							start: '05:30',
							step: '00:15',
							end: '23:30',
							minTime: formData.bus_start_time
							}"
            ></el-time-select>
          </el-form-item>

          <el-form-item label="上传店铺头像">
            <el-upload
              class="avatar-uploader"
              :action="base + '/businesslist/queryimg/'"
              :data="formData"
              :show-file-list="false"
              :on-success="handleShopAvatarScucess"
            >
              <img
                v-if="formData.bus_avator"
                :src="bussinessImageUrl + formData.bus_avator"
                class="avatar"
              />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
          <el-form-item label="上传营业执照">
            <el-upload
              class="avatar-uploader"
              :data="formData"
              :action="base + '/businesslist/querypermit/'"
              :show-file-list="false"
              :on-success="handleBusinessAvatarScucess"
            >
              <img
                v-if="formData.bus_permit"
                :src="bussinessImageUrl + formData.bus_permit"
                class="avatar"
              />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
          <el-form-item label="上传餐饮服务许可证">
            <el-upload
              class="avatar-uploader"
              :data="formData"
              :action="base + '/businesslist/querycater/'"
              :show-file-list="false"
              :on-success="handleServiceAvatarScucess"
            >
              <img
                v-if="formData.bus_cater"
                :src="bussinessImageUrl + formData.bus_cater"
                class="avatar"
              />
              <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
          </el-form-item>
          <el-form-item label="优惠活动">
            <el-select
              v-model="activityValue"
              @change="selectActivity"
              :placeholder="activityValue"
            >
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              ></el-option>
            </el-select>
          </el-form-item>
          <el-table
            :data="activities"
            style="min-width: 600px;margin-bottom: 20px;"
            align="center"
            :row-class-name="tableRowClassName"
          >
            <el-table-column prop="icon_name" label="活动标题" align="cneter" width="120"></el-table-column>
            <el-table-column prop="name" label="活动名称" align="cneter" width="120"></el-table-column>
            <el-table-column prop="description" align="cneter" label="活动详情"></el-table-column>
            <el-table-column label="操作" width="120">
              <template slot-scope="scope">
                <el-button size="small" type="danger" @click="handleDelete(scope.$index)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <el-form-item class="button_submit">
            <el-button type="primary" @click="submitForm()">立即创建</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import headTop from "@/components/headTop";
import { store,comment, business, base, bussinessImageUrl } from "@/api/api.js";
// import { baseUrl, baseImgPath } from "@/config/env";
import { deepClone, createId } from "../comm_func.js";
export default {
  data() {
    return {
      city: {},
      formData: {
        sid: "", //商家id
        bid: "", //商铺id
        bus_name: "", //店铺名称
        bus_address: "", //地址
        bus_introduction: "", //介绍
        bus_class: "", //分类
        bus_characteristic: "", //特点
        bus_phone: "", //商铺电话
        bus_slogan: "", //商铺标语
        bus_delivery: 5, //运费
        bus_start_delivery: 20, //起价
        bus_start_time: "", //营业时间
        bus_end_time: "", //闭店时间
        bus_avator: "", //店铺头像
        bus_permit: "", //营业执照
        bus_cater: "", //许可证
        bus_discount: "" //优惠活动
      },
      delivery_count: {
        is_premium: true,
        delivery_mode: true,
        new: true,
        bao: true,
        zhun: true,
        piao: true
      },
      rules: {
        name: [{ required: true, message: "请输入店铺名称", trigger: "blur" }],
        address: [
          { required: true, message: "请输入详细地址", trigger: "blur" }
        ],
        phone: [
          { required: true, message: "请输入联系电话" },
          { type: "number", message: "电话号码必须是数字" }
        ]
      },
      value: [],
      categoryOptions: [
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
      ],
      options: [
        {
          value: "满减优惠",
          label: "满减优惠"
        },
        {
          value: "优惠大酬宾",
          label: "优惠大酬宾"
        },
        {
          value: "新用户立减",
          label: "新用户立减"
        },
        {
          value: "进店领券",
          label: "进店领券"
        }
      ],
      activityValue: "满减优惠",
      activities: [
        {
          icon_name: "减",
          name: "满减优惠",
          description: "满30减5，满60减8"
        }
      ],
      base,
      bussinessImageUrl,
      selectedCategory: ["快餐便当", "简餐"]
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
    },
    dataList() {
      return this.tableData.slice(
        (this.currpage - 1) * this.pagesize,
        this.currpage * this.pagesize
      );
    }
  },
  watch: {
  },
  methods: {
    //初始化数据
    initData(){
      this.formData = {
        sid: "",
        bid: "",
        bus_name: "",
        bus_address: "",
        bus_introduction: "",
        bus_class: "",
        bus_characteristic: "",
        bus_phone: "",
        bus_slogan: "",
        bus_delivery: 5,
        bus_start_delivery: 20,
        bus_start_time: "",
        bus_end_time: "",
        bus_avator: "",
        bus_permit: "",
        bus_cater: "", 
        bus_discount: ""
      },
      this.activities = [
        {
          icon_name: "减",
          name: "满减优惠",
          description: "满30减5，满60减8"
        }
      ]
      this.delivery_count = {
        is_premium: true,
        delivery_mode: true,
        new: true,
        bao: true,
        zhun: true,
        piao: true
      },
      this.formData.sid = this.storeinfo.sid;
      this.formData.bid = createId();
    },
    //商铺头像上传成功
    handleShopAvatarScucess(res) {
      // console.log(res);
      if (res.code == "0000") {
        this.formData.bus_avator = res.data;
      }
    },
    //营业执照上传成功
    handleBusinessAvatarScucess(res) {
      if (res.code == "0000") {
        this.formData.bus_permit = res.data;
      }
    },
    //服务许可证上传成功
    handleServiceAvatarScucess(res) {
      if (res.code == "0000") {
        this.formData.bus_cater = res.data;
      }
    },
    // 优惠活动
    tableRowClassName(row, index) {
      if (index === 1) {
        return "info-row";
      } else if (index === 3) {
        return "positive-row";
      }
      return "";
    },
    selectActivity() {
      this.$prompt("请输入活动详情", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消"
      })
        .then(({ value }) => {
          if (value == null) {
            this.$message({
              type: "info",
              message: "请输入活动详情"
            });
            return;
          }
          let newObj = {};
          switch (this.activityValue) {
            case "满减优惠":
              newObj = {
                icon_name: "减",
                name: "满减优惠",
                description: value
              };
              break;
            case "优惠大酬宾":
              newObj = {
                icon_name: "特",
                name: "优惠大酬宾",
                description: value
              };
              break;
            case "新用户立减":
              newObj = {
                icon_name: "新",
                name: "新用户立减",
                description: value
              };
              break;
            case "进店领券":
              newObj = {
                icon_name: "领",
                name: "进店领券",
                description: value
              };
              break;
          }
          this.activities.push(newObj);
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消输入"
          });
        });
    },
    // 活动列表删除
    handleDelete(index) {
      this.activities.splice(index, 1);
    },
    // 立即创建
    submitForm() {
      let activities = JSON.stringify(this.activities);
      let delivery_count = JSON.stringify(this.delivery_count);
      let params = deepClone(this.formData);
      params.bus_characteristic = delivery_count;
      params.bus_discount = activities;
      params.bus_class = JSON.stringify(this.value);
      new Promise((resolve,reject) => {
        business.bussinessAdd(params).then(res => {
        if (res.code == "0000") {
          let ret = deepClone(this.storeinfo);
          ret.bid = params.bid;
          // this.$store.commit("setUserInfo", ret);
          sessionStorage.setItem("storeinfo",JSON.stringify(deepClone(ret)))
          this.$store.commit("setStoreInfo",JSON.stringify(deepClone(ret)))
          this.$store.commit("setIsShow",true)
          sessionStorage.setItem("isShowShop",true)
          resolve([params,ret])
        }
      });
      }).then(([params,ret]) => {
          store.storeListEdit(ret).then(res => {
            if(res.code == "0000"){
              // sessionStorage.setItem("userinfo",JSON.stringify(ret))
              sessionStorage.setItem("storeinfo",JSON.stringify(deepClone(ret)))
            }
          })
        comment.bussAdd(params).then(res => {
            if (res.code == "0000") {
              this.$message({
                type: "success",
                message: res.msg
              });
              this.$router.push({path:"/shopList"})
            } else {
              this.$message({
                type: "error",
                message: res.msg
              });
            }
          });
      })
    }
  }
};
</script>

<style lang="less">
@import "../../style/mixin";
.button_submit {
  text-align: center;
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
.el-table .info-row {
  background: #c9e5f5;
}

.el-table .positive-row {
  background: #e2f0e4;
}
</style>
