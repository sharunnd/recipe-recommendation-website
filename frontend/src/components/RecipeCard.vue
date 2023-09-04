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
          class="w-6 h-6 animate-arrow"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M11.25 4.5l7.5 7.5-7.5 7.5m-6-15l7.5 7.5-7.5 7.5"
          />
        </svg>
      </span>
    </router-link>
    <div class="flex">
        <h3 class="mr-1">Rating: {{ recipe.average_rating }}</h3>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="gold"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            class="w-6 h-6"
            style="stroke: gold"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.040.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
            />
          </svg>
        </div>
      </div>
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
/* CSS for the continuous animation */
@keyframes moveRight {
  0% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(1rem); /* Adjust the distance as needed */
  }
  100% {
    transform: translateX(0);
  }
}

.animate-arrow {
  animation: moveRight 2s linear infinite; /* Adjust the duration as needed */
}
</style>
