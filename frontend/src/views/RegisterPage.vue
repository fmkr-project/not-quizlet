<template>
    <div class="register-container">
      <h1>Register</h1>
      <RegisterForm></RegisterForm>
      <!-- Additional content or links -->
    </div>
  </template>
  
  <script>
  import RegisterForm from '@/components/auth/RegisterForm.vue';
  
  export default {
    components: {
      RegisterForm
    }
  };
  </script>
  
  <style>
  /* Styles for the register view */
  </style>
  