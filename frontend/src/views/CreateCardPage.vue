<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import CreateCardComponent from '@/components/pages/CreateCardComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        CreateCardComponent,
        FooterComponent
    }
    // other options
};
</script>
<template>
  <body>
    <HeaderComponent/>
    <CreateCardComponent/>
    <FooterComponent/>
  </body>
  <!-- Rest of your homepage content -->
</template>
<style scoped>
</style>