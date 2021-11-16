<template>
  <div>
    <nav v-bind:class="active">
      <a href="#" class="HOME" @click="isActive('HOME')">HOME</a>
      <a href="#" class="PROJECTS" @click="isActive('PROJECTS')">PROJECTS</a>
      <a href="#" class="SERVICE" @click="isActive('SERVICE')">SERVICE</a>
      <a href="#" class="CONTACT" @click="isActive('CONTACT')">CONTACT</a>
    </nav>
    <div>
      <p>
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
nav > a {
  background-color: #5597b4;
}

nav.HOME .HOME,
nav.PROJECTS .PROJECTS,
nav.SERVICE .SERVICE,
nav.CONTACT .CONTACT {
  background-color: #e35885;
}
</style>