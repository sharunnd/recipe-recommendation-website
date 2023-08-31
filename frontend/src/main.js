import { createApp } from 'vue'
import App from './App.vue'
import './tailwind.css'
import router from './router'
import store from "./store"; // Import the Vuex store instance
createApp(App).use(store).use(router).mount('#app')
