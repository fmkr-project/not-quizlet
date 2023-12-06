<template>
  <div id="app">
    <HeaderComponent/>
    <h1>Welcome to Vue</h1>
    <FooterComponent/>
  </div>
</template>

<script>
import "@/assets/bootstrap/css/bootstrap.min.css";
import "@/assets/css/bs-theme-overrides.css";
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
  name: 'App',
  components: {
    HeaderComponent,
    FooterComponent
  }
};
</script>

<style>
/* Global styles */
</style>