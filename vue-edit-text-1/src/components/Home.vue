<template>
  <div class="content" @click="toggleEditInput">
    <div class="editinput" v-show="isShow">
      <input type="text" name="" id="" v-model="val" @click.stop="showEditInput" />
    </div>
    <div class="edittext" @click.stop="toggleEditInput">{{ val }}</div>
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

<style>
.content {
  width: 300px;
}
.editinput {
  width: 250px;
}
.edittext {
  font-size: 36px;
  color: #9c9891;
  font-weight: 700;
}
.edittext::before {
  content: "✎";
  margin-right: 5px;
}
</style>
