import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router';
import AOS from 'aos';
import 'aos/dist/aos.css';
import store from './store/store'; // Import the store

const app = createApp(App);

app.use(router);  // Add this line to use the router
app.use(store)
app.config.globalProperties.$AOS = AOS.init();

app.mount('#app');
