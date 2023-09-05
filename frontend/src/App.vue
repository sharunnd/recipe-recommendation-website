<template>
  <NavBar />
  <router-view/>
  <FooterVue />
</template>
<script>
import NavBar from './components/NavBar.vue';
import FooterVue from './components/FooterVue.vue';
export default {
  components: {
    NavBar,
    FooterVue
  },
};
</script>
<style>

</style>
