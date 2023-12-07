<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import LoginComponent from '@/components/auth/LoginComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        LoginComponent,
        FooterComponent
    }
    // other options
};
</script>

<template>
    <body>
        <HeaderComponent/>
        <LoginComponent/>
        <FooterComponent/>
    </body>
</template>
  

<style>
/* Styles specific to the login view */
</style>
  