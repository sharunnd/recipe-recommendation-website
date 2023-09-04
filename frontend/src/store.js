import { createStore } from "vuex";

export default createStore({
  state: {
    recipeDetails: null,
    recipeComments: [],
    isLoggedIn: !!localStorage.getItem("token"), // Check if the token exists in local storage
  },
  mutations: {
    setRecipeDetails(state, recipe) {
      state.recipeDetails = recipe;
    },
    clearRecipeDetails(state) {
      state.recipeDetails = null;
    },
    setToastMessage(state, message) {
      state.toastMessage = message;
    },
    setRecipeComments(state, comments) {
      state.recipeComments = comments;
    },
    setLoggedIn(state, value) {
      state.isLoggedIn = value;
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
    async fetchRecipeComments({ commit }, recipeId) {
      try {
        const response = await fetch(`http://localhost:8000/api/recipe/get/reviews/${recipeId}/`);
        const data = await response.json();
        commit("setRecipeComments", data); // Mutation to set comments in the state
      } catch (error) {
        console.error("Error fetching comments:", error);
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
    async createReview({ commit,dispatch  }, { recipeId, comment }) {
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
          await dispatch("fetchRecipeComments", recipeId); // Assuming you have the "fetchRecipeComments" action
          // You can handle success actions here if needed
           const res = await response.json();
           commit("setToastMessage", res);
          //  commit("setRecipeComments", res);
           return res
        } else {
          commit("setToastMessage", null);
          // commit("setRecipeComments", null);
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
          const res = await response.json();
          commit("setToastMessage", res);
          return res
        } else {
          commit("setToastMessage", null);
          throw new Error(`Error creating rating: ${response.statusText}`);
        }
      } catch (error) {
        console.error("Error creating rating:", error);
        commit("setBackendMessage", null); // Clear the previous message
      }
    },
  },
  getters: {
    recipeDetails: (state) => state.recipeDetails,
    recipeComments: (state) => state.recipeComments,
  },
});
