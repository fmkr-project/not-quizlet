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
    <body>
    <HeaderComponent/>
    <ResetPasswordComponent/>
    <FooterComponent/>
    </body>
</template>