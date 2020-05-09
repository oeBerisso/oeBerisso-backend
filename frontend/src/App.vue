<template>
  <div class="app">
    <Navbar />
    <div class="component">
      <router-view/>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from './components/Footer.vue';
import Navbar from './components/Navbar.vue';

export default {
  components: {
    Footer,
    Navbar,
  },
};
</script>

<style>
  .component {
    min-height: 69vh;
  }

  body {
    background-color: #cacaca;
  }
</style>
