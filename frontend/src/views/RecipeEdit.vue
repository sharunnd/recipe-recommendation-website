<template>
    <div>
      <h1>Edit Recipe</h1>
      <form @submit.prevent="submitUpdatedRecipe">
        <label for="heading">Heading</label>
        <input v-model="updatedRecipe.heading" type="text" id="heading" />
        <label for="ingredients">Ingredients</label>
        <textarea v-model="updatedRecipe.ingredients" id="ingredients"></textarea>
        <button type="submit">Update Recipe</button>
      </form>
    </div>
  </template>
  
  <script>
  import { mapActions, mapGetters } from "vuex";
  
  export default {
    computed: {
      ...mapGetters(["recipeDetails"]),
      originalRecipe() {
        return this.recipeDetails || {};
      },
    },
    data() {
      return {
        updatedRecipe: {
          heading: "",
          ingredients: "",
        },
      };
    },
    methods: {
      ...mapActions(["fetchRecipeDetails", "updateRecipe"]),
      async fetchRecipeData() {
        const recipeId = this.$route.params.id;
        await this.fetchRecipeDetails(recipeId);
        // Populate the form fields with the original recipe data
        this.updatedRecipe = { ...this.originalRecipe };
      },
      async submitUpdatedRecipe() {
  // Call the updateRecipe action in your Vuex store
  await this.updateRecipe(this.$route.params.id, this.updatedRecipe);
  // Redirect back to the recipe details page
  this.$router.push(`/recipe/details/${this.$route.params.id}`);
},
    },
    mounted() {
      this.fetchRecipeData();
    },
  };
  </script>
  