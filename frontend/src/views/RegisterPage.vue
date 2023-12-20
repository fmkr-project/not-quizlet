<template>
  <div>
    <HeaderComponent />
    <RegisterComponent />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from "@/components/layout/HeaderComponent.vue";
import RegisterComponent from "@/components/auth/RegisterComponent.vue";
import FooterComponent from "@/components/layout/FooterComponent.vue";

export default {
  components: {
    HeaderComponent,
    RegisterComponent,
    FooterComponent,
  },
};
</script>

<style>
/* Add any additional styles for the RegisterPage here */
</style>
