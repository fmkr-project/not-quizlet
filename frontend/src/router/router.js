import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/views/HomePage.vue';
import LoginPage from '@/views/LoginPage.vue';
import ResetPasswordPage from '@/views/ResetPasswordPage';
import TestPage from '@/views/TestPage.vue';
const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/reset-password',
    name: 'Reset Password',
    component: ResetPasswordPage
  },
  {
    path:'/test',
    name: 'test',
    component: TestPage
  }

  // ... other routes ...
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
