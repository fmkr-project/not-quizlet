import { createRouter, createWebHistory } from 'vue-router';

const HomePageRoutes = (prefix) => [
  {
    path: '',
    name: prefix + '.home',
    meta: {auth: true, name: 'Home'},
    component: () => import('@/views/HomePage.vue')
  }
]

const routes = [
  {
    path: '/',
    name: 'Home',
    children: HomePageRoutes('default')
  },
  // ... other routes ...
];

const router = createRouter({
  linkActiveClass: 'active',
  linkExactActiveClass: 'exact-active',
  history: createWebHistory(process.env.BASE_URL),
  base: process.env.BASE_URL,
  routes
});

export default router;
