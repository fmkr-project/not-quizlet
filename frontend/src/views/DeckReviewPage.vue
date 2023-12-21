<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import DeckReviewComponent from '@/components/pages/DeckReviewComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        DeckReviewComponent,
        FooterComponent
    }
    // other options
};
</script>
<template>
  <body>
    <HeaderComponent/>
    <DeckReviewComponent/>
    <FooterComponent/>
  </body>
  <!-- Rest of your homepage content -->
</template>
<style scoped>
</style>