<template>
  <div>
    <nav v-bind:class="active">
      <a href="#" class="HOME" @click="isActive('HOME')">HOME</a>
      <a href="#" class="PROJECTS" @click="isActive('PROJECTS')">PROJECTS</a>
      <a href="#" class="SERVICE" @click="isActive('SERVICE')">SERVICE</a>
      <a href="#" class="CONTACT" @click="isActive('CONTACT')">CONTACT</a>
    </nav>
    <div>
      <p class="content">
        你选择了<b>{{ active }}菜单</b>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      active: "HOME",
    };
  },
  methods: {
    isActive: function (text) {
      this.active = text;
    },
  },
};
</script>

<style scoped>
nav {
  /* 为了去除 a 标签之间的空隙 */
  font-size: 0px;
}
nav > a {
  background-color: #5597b4;
  display: inline-block;
  height: 100px;
  padding: 0 20px;
  text-decoration: none;
  font-weight: bold;
  line-height: 100px;
  font-size: 36px;
  color: white;
}

nav.HOME .HOME,
nav.PROJECTS .PROJECTS,
nav.SERVICE .SERVICE,
nav.CONTACT .CONTACT {
  background-color: #e35885;
}

p.content{
  font-size: 36px;
  color: #7d9098;
}

p.content>b{
  color: white;
  display: inline-block;
  background-color: #c4d7e0;
  padding:2px 12px
}
</style>