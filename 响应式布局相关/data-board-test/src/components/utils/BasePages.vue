<template>
  <div>
    <div>Home</div>
    <!-- <div v-for="item in modules" :key="item.name">
      <div>{{ idParseComponent(item)}}</div>
    </div> -->
    <div v-for="item in fetchData" :key="item.id">
      <component :is="idParseComponent(item)" :config="config" />
    </div>
  </div>
</template>

<script>
// import { defineComponent } from '@vue/composition-api'
import modules from '@/components/modules'

// props 支持2种属性
export default {
  name: '',
  data () {
    return {
      config: {
        deviceType: 'pc'
      },
      comsObj: {
        id_com1: 'Component1',
        id_com2: 'Component2',
        id_com3: 'Component3'
      },
      fetchData: [
        {
          id: 'id_com1',
          data: 'data_com2'
        },
        {
          id: 'id_com3',
          data: 'data_com3'
        }
      ],
      modules: modules
    }
  },
  components: {
    ...modules
  },
  mounted () {},
  methods: {
    idParseComponent (item) {
      return this.comsObj[item.id]
    }
  }
}
</script>

<style scoped>
</style>
