<template>
  <div class="content">
    <div class="content-1">
        <input
          class="input"
          type="text"
          placeholder="输入待办事项，回车添加"
          v-model="inputText"
          @keypress.enter="addlist"
        />
      <ul class="list-body">
        <li
          class="list-body-item"
          v-for="(item, index) in todolist"
          v-bind:class="item.isDone ? 'done' : 'doing'"
          v-bind:key="index"
          @click="item.isDone = !item.isDone"
        >
          {{ item.text }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      todolist: [],
      inputText: ''
    }
  },
  methods: {
    addlist: function () {
      this.todolist.push({ text: this.inputText, isDone: false })
      console.log(this.inputText)
      this.inputText = ''
    }
  }
}
</script>

<style>
/* 让灰色背景上下区域充满浏览器 */
html,
body,
.content {
  height: 100%;
  overflow: hidden;
}

.content {
  width: 1005px;
  border:2px solid #f7f7f7;
  margin:0 auto;
}

.content-1{
  width: 565px;
  margin:0 auto;
}

.input {
  width: 561px;
  height: 72px;
  font-size: 36px;
  color: #888888 100%;
  text-align: center;
  border: 1px solid #f7f7f7;
  margin-top: 98px;
}

.list-body{
  margin-top: 24px;
  text-align: left;
  /* 如果不设置 overflow margin-top 和父级的会塌陷 */
  overflow: hidden;
}

.list-body-item{
  margin-top: 30px;
  font-size: 36px;
  cursor:pointer;
}

.doing {
  color: red;
  font-weight: bolder;
}
.done {
  text-decoration-line: line-through;
  color: #939393 100%;
  font-weight: 200;
}
</style>
