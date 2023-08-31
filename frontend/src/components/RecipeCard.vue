<template>
  <div class="bg-white rounded-lg shadow-md p-5">
    <img
      v-if="recipe.image_url"
      :src="recipe.image_url"
      alt="Recipe Image"
      class="w-full h-40 object-cover mb-4"
    />
    <router-link
      :to="'/recipe/' + recipe.id"
      class="text-lg font-semibold flex items-center"
    >
      {{ recipe.heading }}
      <span class="ml-2"
        ><svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="w-6 h-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M11.25 4.5l7.5 7.5-7.5 7.5m-6-15l7.5 7.5-7.5 7.5"
          />
        </svg>
      </span>
    </router-link>
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
