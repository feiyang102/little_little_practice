<template>
    <div>Component2_{{config.deviceType}}</div>
</template>

<script>
// import { defineComponent } from '@vue/composition-api'
import Base from '../utils/BaseModules.vue'

// props 支持2种属性
export default({
  name: 'Component2',
  mixins: [Base],
  data () {
    return {}
  }
})
</script>

<style scoped>

</style>
