import { createStore } from "vuex";
import { createApp } from 'vue';
export default createStore({
  state: {
    recipeDetails: null,
  },
  mutations: {
    setRecipeDetails(state, recipe) {
      state.recipeDetails = recipe;
    },
    clearRecipeDetails(state) {
      state.recipeDetails = null;
    },
  },
  actions: {
    async fetchRecipeDetails({ commit }, recipeId) {
      try {
        const response = await fetch(`http://localhost:8000/api/recipe/${recipeId}/`);
        const data = await response.json();
        commit("setRecipeDetails", data);
      } catch (error) {
        console.error("Error fetching recipe details:", error);
      }
    },
    async deleteRecipe({ commit }, recipeId) {
        try {
          const response = await fetch(`http://localhost:8000/api/delete_recipe/${recipeId}/`, {
            method: "DELETE",
            headers: {
              Authorization: `Token ${localStorage.getItem("token")}`, // Include the auth token here
            },
          });
          if (response.ok) {
            commit("clearRecipeDetails");
            createApp().config.globalProperties.$router.push('/'); // Emit event to navigate
          } else {
            console.error("Error deleting recipe");
          }
      } catch (error) {
        console.error("Error deleting recipe:", error);
      }
    },
    async updateRecipe({ commit }, recipeId, updatedRecipe) {
        try {
          const response = await fetch(`http://localhost:8000/api/update_recipe/${recipeId}/`, {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
            body: JSON.stringify(updatedRecipe),
          });
      
          if (response.ok) {
            commit("clearRecipeDetails");
          } else {
            console.error("Error updating recipe:", response.statusText);
          }
        } catch (error) {
          console.error("Error updating recipe:", error);
        }
      }
      
  },
  getters: {
    recipeDetails: (state) => state.recipeDetails,
  },
});
