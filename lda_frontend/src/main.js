import { createApp } from 'vue'
import App from './App.vue'
import store from './storage';
import 'bootstrap/dist/css/bootstrap.min.css';



const app = createApp(App);
app.use(store);
app.mount('#app');