<template>
<div id="banner">
  <div class="banner_child">
    <p class="subtitle">Why</p>
  </div>
  <div class="banner_child">
    <p class="subtitle">LinkedIn</p>
  </div>
  <div class="banner_child">
    <p class="subtitle">Github</p>
  </div>
</div>
<div class="section">
  <p class="subtitle">Phonology</p>
</div>
<div class="section">
  <p class="subtitle">Syntax</p>
  </div>
</template>

<style>
body {
  background-color: #24496b;
}
#banner {
  width: 100vw;
  height: 5vh;
  background-color: #f5e050;
  position: fixed;
  top: 0;
  left: 0;
}
.banner_child {
  display: inline;
  margin: 10vw;
}
.subtitle {
  color: #24496b;
  display: inline;
  padding-top: 10%;
}
.banner_child:hover {
  cursor: pointer;
}
.section {
  display: inline;
  margin: 10vh;
  padding: 2.5vh;
  background-color: #f5e050;
}
.section:hover {
  background-color: #f4e376;
  cursor: pointer;
}
</style>

<script>
export default {
  name: 'Home',
};
</script>
