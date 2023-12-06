<template>
    <div class="login-container">
      <h1>Login</h1>
      <LoginForm></LoginForm>
      <!-- You can add more content or navigation links here -->
    </div>
  </template>
  
  <script>
  import LoginForm from '@/components/auth/LoginForm.vue';
  
  export default {
    components: {
      LoginForm
    }
  };
  </script>
  
  <style>
  /* Styles specific to the login view */
  </style>
  