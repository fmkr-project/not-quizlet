<template>
    <form @submit.prevent="register">
      <input v-model="user.username" type="text" placeholder="Username">
      <input v-model="user.email" type="email" placeholder="Email">
      <input v-model="user.password" type="password" placeholder="Password">
      <button type="submit">Register</button>
    </form>
  </template>
  
  <script>
  import AuthService from '@/services/authService';
  
  export default {
    name: "RegisterComponent",
    data() {
      return {
        user: {
          username: '',
          email: '',
          password: ''
        }
      };
    },
    methods: {
      async register() {
        const response = await AuthService.register(this.user);
        if (response.success) {
          // Handle success scenario
        } else {
          // Handle failure scenario
        }
      }
    },

  };
  </script>