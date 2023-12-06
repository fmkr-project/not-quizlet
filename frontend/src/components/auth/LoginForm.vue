<template>
    <form @submit.prevent="login">
      <input v-model="user.username" type="text" placeholder="Username or Email" />
      <input v-model="user.password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
  </template>
  
  <script>
  import AuthService from '@/services/authService';
  
  export default {
    data() {
      return {
        user: {
          username: '',
          password: ''
        }
      };
    },
    methods: {
      async login() {
        try {
          const response = await AuthService.login(this.user);
          if (response.success) {
            this.$router.push('/home');
          } else {
            alert(response.message);
          }
        } catch (error) {
          alert('Login failed');
        }
      }
    }
  };
  </script>
  