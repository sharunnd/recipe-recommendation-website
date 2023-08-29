import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginPage from '../views/LoginPage.vue'
import SignupPage from '../views/SignupPage.vue'

const routes = [
    { path: '/', component: HomeView },
    { path: '/login', component: LoginPage },
    { path: '/signup', component: SignupPage },
  ];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
