<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import DeckUsersComponent from '@/components/pages/DeckUsersComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        DeckUsersComponent,
        FooterComponent
    }
    // other options
};
</script>

<template>
    <body>
        <HeaderComponent/>
        <DeckUsersComponent/>
        <FooterComponent/>
    </body>
</template>
  

<style>
/* Styles specific to the login view */
</style>
  