<template>
  <div v-html="apply">{{ apply }}</div>
</template>

<script>
export default {
  name: "applyText",
  data() {
    return {
      apply: ""
    };
  },
  mounted() {
    let form = this.$route.query.htmls
    this.apply = form
    console.log(form)
    // this.apply = form;
    this.$nextTick(() => {
      document.forms[0].submit();
    });
  }
};
</script>

<style scoped>
</style>