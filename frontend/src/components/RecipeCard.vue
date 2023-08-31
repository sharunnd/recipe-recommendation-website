<template>
    <div class="bg-white rounded-lg shadow-md p-5">
        <img v-if="recipe.image_url" :src="recipe.image_url" alt="Recipe Image" class="w-full h-40 object-cover mb-4" />
      <h2 class="text-lg font-semibold mb-2">{{ recipe.heading }}</h2>
      <p class="text-gray-500">{{ recipe.ingredients }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      recipe: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add Tailwind classes here if needed */
  </style>
  