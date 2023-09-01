import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginPage from '../views/LoginPage.vue'
import SignupPage from '../views/SignupPage.vue'
import RecipeDetails from "../views/RecipeDetails.vue"
import RecipeEdit from "../views/RecipeEdit.vue"
import RecipeCreate from "../views/RecipeCreate.vue"
import AiRecipe from "../views/AiRecipe.vue"
const routes = [
    { path: '/', component: HomeView },
    { path: '/login', component: LoginPage },
    { path: '/signup', component: SignupPage },
    { path: "/recipe/:id", component: RecipeDetails },
    {path: "/recipe/edit/:id",component: RecipeEdit},
    { path: "/recipe/create", component: RecipeCreate },
    { path: "/ai/suggestions", component: AiRecipe },
  ];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
