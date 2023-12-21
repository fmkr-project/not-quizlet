<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import ViewCardComponent from '@/components/pages/ViewCardComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        ViewCardComponent,
        FooterComponent
    }
    // other options
};
</script>
<template>
  <body>
    <HeaderComponent/>
    <ViewCardComponent/>
    <FooterComponent/>
  </body>
  <!-- Rest of your homepage content -->
</template>
<style scoped>
</style>