<template>
<div class="content">
    <h1 class="content__title">Service</h1>
    <ul class="content__body">
        <li
        class="content__body-item"
        v-for="item in dataList"
        :key="item.id"
        :class="item.selected?'content__body-item-selected':'content__body-item-unselected'"
        @click.stop="item.selected=!item.selected"
        >
        {{ item.name }}
        <span class="content__body-item-spam">${{item.price}}</span>
        </li>
    </ul>
    <p class="content__total">
        Total:
        <span class="content__total-span">${{total}}</span>
        </p>

</div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      dataList: [
        {
          id: '1',
          name: 'Web Development',
          price: 300,
          selected: false
        }, {
          id: '2',
          name: 'Design',
          price: 410,
          selected: false
        }, {
          id: '3',
          name: 'Integration',
          price: 250,
          selected: false
        }, {
          id: '4',
          name: 'Training',
          price: 220,
          selected: false
        }
      ]
    }
  },
  computed: {
    total: function () {
      let _total = 0

      this.dataList.forEach((item) => {
        if (item.selected) {
          _total += item.price
        }
      })
      return _total
    }
  }
}
</script>
      }

<style scoped>
.content{
    background-color: #61a1bc;
    color: #ffffff;
}
.content__body-item-selected{
    background-color: #8ec16d;
}
.content__body-item-unselected{
    background-color: #e35885;
}
</style>
