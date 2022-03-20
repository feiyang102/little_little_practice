<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  mounted () {
    // 判断设备类型等
    this.redirect()
    // 页面宽度获取等等
    // var c= ()=>{
    //     let w = document.documentElement.clientWidth;
    //     let n = (20*(w/320)>40?40+'px':(20*(w/320)+'px'));
    //     document.documentElement.style.fontSize = n;
    // }
    // window.addEventListener('load',c);
    // window.addEventListener('resize',c);
  },
  methods: {
    redirect () {
      // 获取设备信息
      let userAgent = navigator.userAgent.toLowerCase()
      let device = /ipad|iphone|midp|rv:1.2.3.4|ucweb|android|windows ce|windows mobile/
      if (device.test(userAgent)) {
        console.log('手机端')
        // window.location.href='move.html';
      } else {
        console.log('PC端')
        // window.location.href = 'pc.html';
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
