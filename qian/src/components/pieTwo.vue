<template>
  <div class="visitorpie">
    <div id="visitorpietwo" class style="width: 90%;height:450px;"></div>
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
    this.myChart = echarts.init(document.getElementById("visitorpietwo"));
    this.initData();
  },
  props: ["pieData", "legendData", "title"],
  methods: {
    // 用户数据分布
    initData() {
      const option = {
        title: {
          text: this.title,
          subtext: "",
          x: "center"
        },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          left: "left",
          data: this.legendData
        },
        series: [
          {
            type: "pie",
            radius: "55%",
            center: ["50%", "60%"],
            roseType: 'angle',
            data: this.pieData,
          }
        ]
      };

      this.myChart.setOption(option);
    }
  },
  watch: {
    pieData: function() {
      this.initData();
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
