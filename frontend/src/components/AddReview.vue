<!-- AddReview.vue -->
<template>
    <div>
      <!-- Review form UI -->
      <textarea v-model="reviewText"></textarea>
      <button @click="submitReview">Submit Review</button>
    </div>
  </template>
  
  <script>
  import { mapActions } from "vuex";
  
  export default {
    data() {
      return {
        reviewText: "",
      };
    },
    methods: {
      ...mapActions(["createReview"]),
      submitReview() {
        this.createReview({ recipeId: this.recipeId, comment: this.reviewText });
        // Clear the input field or handle success/error messages
      },
    },
    props: {
      recipeId: Number,
    },
  };
  </script>
  