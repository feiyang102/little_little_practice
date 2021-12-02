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
        <span class="content__body-item-spam">${{item.price.toFixed(2)}}</span>
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
*{
  margin: 0;
  padding: 0;
}
.content{
    background-color: #61a1bc;
    color: #ffffff;
    width: 520px;
    margin: 0 auto;
    overflow: hidden;
    font-size: 27px;
}
.content__title{
  font-weight: 200;
  margin-top: 30px;
}
.content__body{
  width: 400px;
  margin: 0 auto;
  margin-top: 10px;
  border-bottom: 2px solid #b0d0de;
}
.content__body-item{
  list-style: none;
  line-height: 30px;
  margin-bottom: 10px;
  font-size: 18px;
  padding: 20px;
  text-align: left;
}
.content__body-item-spam{
  float: right;
}
.content__body-item-selected{
    background-color: #8ec16d;
}
.content__body-item-unselected{
    background-color: #e35885;
}
.content__total{
  text-align: left;
  margin-left: 80px;
  font-size: 18px;
  margin-top: 12px;
}
.content__total-span{
  float: right;
  margin-right: 80px;
  margin-bottom: 40px;
}

</style>
