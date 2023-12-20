<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import ProfileComponent from '@/components/pages/ProfileComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        ProfileComponent,
        FooterComponent
    }
    // other options
};
</script>

<template>
    <body>
        <HeaderComponent/>
        <ProfileComponent/>
        <FooterComponent/>
    </body>
</template>
  

<style>
/* Styles specific to the login view */
</style>
  