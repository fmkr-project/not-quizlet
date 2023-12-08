<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import HomeComponent from '@/components/pages/HomeComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        HomeComponent,
        FooterComponent
    }
    // other options
};
</script>
<template>
  <body>
    <HeaderComponent/>
    <HomeComponent/>
    <FooterComponent/>
  </body>
  <!-- Rest of your homepage content -->
</template>
<style scoped>
</style>