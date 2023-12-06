import { createApp } from 'vue';
import App from './App.vue';
import AOS from 'aos';
import 'aos/dist/aos.css'


const app = createApp(App)

app.use(
    {
        install: (app) => {
            app.config.globalProperties.$AOS = AOS.init();
        }
    }
);

// If you have a router or store, they would be initialized here.
// app.use(router);
// app.use(store);

app.mount('#app');
