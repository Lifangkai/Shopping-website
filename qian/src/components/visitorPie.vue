<template>
  <div class="visitorpie">
    <div id="visitorpie" class style="width: 100%;height:500px;"></div>
  </div>
</template>

<script>
import echarts from "echarts/lib/echarts";
// 引入柱状图
import "echarts/lib/chart/pie";
import "echarts/lib/component/title";
import "echarts/lib/component/legend";

export default {
  mounted() {
    this.myChart = echarts.init(document.getElementById("visitorpie"));
    // console.log(this.pieData,this.legendData,this.storepieData,this.storelegendData)
    this.initData();
  },
  props: ["pieData", "legendData", "storepieData", "storelegendData"],
  methods: {
    // 用户数据分布
    initData() {
      const option = {
        // color: ["#86dad2", "#00abea", "#f5c801", "#ef6007"],
        title: [
          {
            text: "用户分布",
            textStyle: {
              color: "rgb(16,70,200)",
              fontSize: 20,
              fontWeight: "normal"
            },
            left: "16%"
          },
          {
            text: "商家分布",
            textStyle: {
              color: "rgb(16,70,200)",
              fontSize: 20,
              fontWeight: "normal"
            },
            left: "56%"
          },
          // {
          //   text: "用户分布",
          //   textStyle: {
          //     color: "rgb(16,70,200)",
          //     fontSize: 20,
          //     fontWeight: "normal"
          //   },
          //   left: "16%",
          //   bottom: "10%"
          // },
          // {
          //   text: "商家分布",
          //   textStyle: {
          //     color: "rgb(16,70,200)",
          //     fontSize: 20,
          //     fontWeight: "normal"
          //   },
          //   left: "56%",
          //   bottom: "10%"
          // }
        ],
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: [
          {
            orient: "vertical",
            left: "0%",
            data: this.legendData
          },
          {
            orient: "vertical",
            left: "40%",
            data: this.storelegendData
          },
          // {
          //   orient: "horizontal",
          //   left: "0%",
          //   bottom: "10%",
          //   data: this.legendData
          // },
          // {
          //   orient: "horizontal",
          //   left: "40%",
          //   bottom: "10%",
          //   data: this.storelegendData
          // }
        ],
        // xAxis: [
        //   { gridIndex: 0, show: false },
        //   { gridIndex: 1, show: false },
        //   {
        //     gridIndex: 2,
        //     axisLabel: {
        //       show: false
        //     },
        //     axisTick: {
        //       show: false
        //     },
        //     splitLine: {
        //       show: false
        //     },
        //     data: this.legendData
        //   },
        //   {
        //     gridIndex: 3,
        //     axisLabel: {
        //       show: false
        //     },
        //     axisTick: {
        //       show: false
        //     },
        //     splitLine: {
        //       show: false
        //     },
        //     data: this.storelegendData
        //   }
        // ],
        // grid: [
        //     {top: '3%', left: '3%', width: '20%', height: '40%'},
        //     {top: '9%', left: '24%', width: '34%', height: '36%'},
        //     {top: '3%', left: '62%', width: '37%', height: '92%'},
        //     {top: '58%', left: '3%', width: '53%', height: '37%'}
        // ],
        // yAxis: [
        //   { gridIndex: 0, show: false },
        //   { gridIndex: 1, show: false },
        //   {
        //     gridIndex: 2,
        //     type: "value",
        //     axisLabel: {
        //       show: false
        //     },
        //     axisTick: {
        //       show: false
        //     },
        //     splitLine: {
        //       show: false
        //     }
        //   },
        //   {
        //     gridIndex: 3,
        //     type: "value",
        //     axisLabel: {
        //       show: false
        //     },
        //     axisTick: {
        //       show: false
        //     },
        //     splitLine: {
        //       show: false
        //     }
        //   }
        // ],
        series: [
          {
            type: "pie",
            radius: "55%",
            center: ["20%", "60%"],
            labelLine: {
                    normal: {
                        show: false
                    }
                },
            data: this.pieData
          },
          {
            type: "pie",
            radius: "55%",
            center: ["60%", "60%"],
            labelLine: {
                    normal: {
                        show: false
                    }
                },
            data: this.storepieData
          },
          // {
          //   type: "bar",
          //    xAxisIndex: 2,
          //    yAxisIndex: 2,
          //   data: this.pieData
          // },
          // {
          //   type: "bar",
          //    xAxisIndex: 3,
          //    yAxisIndex: 3,
          //   data: this.storepieData
          // }
        ]
      };

      this.myChart.setOption(option);
    }
  },
  watch: {
    pieData: function() {
      this.initData();
    },
    storepieData() {
      this.initData();
      console.log(this.pieData,this.storepieData)
    }
  }
};
</script>

<style lang="less">
@import "../style/mixin";
.visitorpie {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>
