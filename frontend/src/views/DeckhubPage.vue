<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import DeckhubComponent from '@/components/pages/DeckhubComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        DeckhubComponent,
        FooterComponent
    }
    // other options
};
</script>
<template>
  <body>
    <HeaderComponent/>
    <DeckhubComponent/>
    <FooterComponent/>
  </body>
  <!-- Rest of your homepage content -->
</template>
<style scoped>
</style>