<template>
  <div class="content" @click="toggleEditInput">
    <div class="content__editinput" v-show="isShow">
      <input type="content__text" name="" id="" v-model="val" @click.stop="showEditInput" />
    </div>
    <p class="content__edittext" @click.stop="toggleEditInput">{{ val }}</p>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      isShow: false,
      val: '点我，并编辑内容。'
    }
  },
  methods: {
    toggleEditInput: function () {
      this.isShow = !this.isShow
    },
    showEditInput: function () {
      this.isShow = true
    }
  }
}
</script>

<style scope>
body{
  font: 15px/1.3 'Open Sans', sans-serif;
}
.content{
  position: relative;
}
.content__editinput {
  width: 250px;
  position: absolute;
  left: 50%;
  bottom: 40px;
  transform: translateX(-50%);
  background-color: #5897b2;
  padding: 10px;
  border-radius: 3px;
}
.content__editinput>input{
  text-align: center;
  width: 240px;
  border:none;
  border-radius: 3px;
  line-height: 34px;
  box-shadow: 0 2px 6px #bbb inset;
  font-size: 16px;
  color: #8d9395;
  font-weight: bold;
}
.content__editinput::after{
    content: '';
    position: absolute;
    border: 6px solid #5190ac;
    border-color: #5190ac transparent transparent;
    width: 0;
    height: 0;
    bottom: -12px;
    left: 50%;
    margin-left: -6px;
}
.content__edittext{
  font-size: 22px;
  font-weight: bold;
  color: #6d8088;
  text-align: center;
}
.content__edittext::before {
  content: "✎";
  margin-right: 5px;
}

</style>
