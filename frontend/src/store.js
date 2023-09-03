import { createStore } from "vuex";

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
          // Recipe deleted successfully, commit the mutation to clear recipeDetails
          commit("clearRecipeDetails");
          return response; // Return the response to handle success message in the component
        } else if (response.status === 403) {
          // Permission issue, throw an error with status 403
          throw new Error("Permission denied");
        } else {
          // Handle other errors
          throw new Error(`Error deleting recipe: ${response.statusText}`);
        }
      } catch (error) {
        console.error("Error deleting recipe:", error);
      }
    },
    async updateRecipe({ commit }, recipeId, updatedRecipeData) {
      try {
        console.log("...updated..",recipeId,updatedRecipeData);
        const response = await fetch(`http://localhost:8000/api/update_recipe/${recipeId}/`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
          body: JSON.stringify(updatedRecipeData),
        });
        console.log(response);
        if (response.ok) {
          commit("clearRecipeDetails");
          return response; // Return the response to handle success message in the component
        } else {
          // Handle other errors
          throw new Error(`Error updating recipe: ${response.statusText}`);
        }
      } catch (error) {
        console.error("Error updating recipe:", error);
      }
    },
    async createReview({ commit }, { recipeId, comment }) {
      try {
        const response = await fetch(`http://localhost:8000/api/recipe/reviews/${recipeId}/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
          body: JSON.stringify({ comment }),
        });
        if (response.ok) {
          // You can handle success actions here if needed
          return response;
        } else {
          commit
          throw new Error(`Error creating review: ${response.statusText}`);
        }
      } catch (error) {
        console.error("Error creating review:", error);
      }
    },    
    async createRating({commit}, { recipeId, rating }) {
      console.log("id", recipeId, rating);
      try {
        const response = await fetch(`http://localhost:8000/api/recipe/rate/${recipeId}/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
          body: JSON.stringify({ rating }),
        });
        if (response.ok) {
          // You can handle success actions here if needed
          return response;
        } else {
          commit
          throw new Error(`Error creating rating: ${response.statusText}`);
        }
      } catch (error) {
        console.error("Error creating rating:", error);
      }
    },
  },
  getters: {
    recipeDetails: (state) => state.recipeDetails,
  },
});
