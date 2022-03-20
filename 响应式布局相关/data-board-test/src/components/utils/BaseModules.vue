<template>
  <div>Component3</div>
</template>

<script>
// import { defineComponent } from '@vue/composition-api'

// props 支持2种属性
export default {
  name: 'BaseModules',
  props: {
    config: {
      type: Object,
      default: function () {
        return {
          // 设备类型: mobile、pc
          deviceType: ''
        }
      }
    },
    data: null
  },
  data () {
    return {
      hello: 'dasdf'
    }
  }
}
</script>

<style scoped>
</style>
