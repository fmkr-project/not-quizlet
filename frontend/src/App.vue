<template>
  <div id="app">
    <HeaderComponent />
    <h1>Welcome to Vue</h1>
  </div>
</template>

<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';

export default {
  name: 'App',
  components: {
    HeaderComponent
  }
};
</script>

<style>
/* Global styles */
</style>