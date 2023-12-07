<script>
import HeaderComponent from '@/components/layout/HeaderComponent.vue';
import ResetPasswordComponent from '@/components/auth/ResetPasswordComponent.vue'
import FooterComponent from '@/components/layout/FooterComponent.vue';
export default {
    components: {
        HeaderComponent,
        ResetPasswordComponent,
        FooterComponent
    }
    // other options
};
</script>
<template>
    <HeaderComponent></HeaderComponent>
    <ResetPasswordComponent></ResetPasswordComponent>
    <FooterComponent></FooterComponent>
</template>