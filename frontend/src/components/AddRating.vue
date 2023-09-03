<!-- AddRating.vue -->
<template>
    <div>
      <!-- Rating form UI -->
      <input v-model="ratingValue" type="number" min="1" max="5">
      <button @click="submitRating">Submit Rating</button>
    </div>
  </template>
  
  <script>
  import { mapActions } from "vuex";
  
  export default {
    data() {
      return {
        ratingValue: 1,
      };
    },
    methods: {
      ...mapActions(["createRating"]),
      submitRating() {
        this.createRating({ recipeId: this.recipeId, rating: this.ratingValue });
        // Clear the input field or handle success/error messages
      },
    },
    props: {
      recipeId: Number,
    },
  };
  </script>
  