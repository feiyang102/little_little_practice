<template>
  <div class="content">
    <div class="content-1">
      <div class="input">
        <input
          type="text"
          placeholder="输入内容"
          v-model="inputText"
          @keypress.enter="addlist"
        />
      </div>
      <div class="list-body">
        <div
          v-for="(item, index) in todolist"
          v-bind:class="item.isDone ? 'done' : 'doing'"
          v-bind:key="index"
          @click="item.isDone = !item.isDone"
        >
          {{ item.text }}
        </div>
      </div>
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
html,
body,
.content {
  height: 100%;
  overflow: hidden;
}

.content {
  width: 80%;
  background-color: darkgrey;
}
.doing {
  color: red;
  font-weight: bolder;
}
.done {
  text-decoration-line: line-through;
  color: black;
  font-weight: 200;
}
</style>
