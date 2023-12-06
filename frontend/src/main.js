import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router';
import AOS from 'aos';
import 'aos/dist/aos.css';

const app = createApp(App);

app.use(router);  // Add this line to use the router
app.config.globalProperties.$AOS = AOS.init();

app.mount('#app');
