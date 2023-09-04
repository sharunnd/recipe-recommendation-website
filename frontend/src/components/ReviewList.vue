<template>
  <div class="bg-white p-4 rounded-md shadow-md">
    <h3 class="text-xl font-semibold mb-2">Reviews:</h3>
    <ul v-if="Array.isArray(reviews)" class="list-disc pl-4">
      <li
        v-for="review in reviews"
        :key="review.id"
        class="mb-2 bg-slate-100 list-none p-2 rounded-lg flex items-center"
      >  <div class="mr-2">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            :stroke="randomColor"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            class="w-6 h-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z"
            />
          </svg></div>
        <div>
          <p class="text-sm">{{ review.user_name }}</p>
          <p class="text-black">
          {{ review.comment }}
        </p>
        </div>
      </li>
    </ul>
    <p v-else class="text-gray-500">No reviews available.</p>
  </div>
</template>

<script>
export default {
  props: {
    reviews: Array, // An array of review objects
  },
  computed: {
    randomColor() {
      // Generate a random color in hexadecimal format
      const randomHexColor = `#${Math.floor(Math.random()*16777215).toString(16)}`;
      return randomHexColor;
    }
  }
};
</script>

<style scoped>
/* Your styling here */
</style>
