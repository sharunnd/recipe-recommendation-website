<!-- AddRating.vue -->
<template>
  <div class="flex items-center space-x-4 p-4 rounded-lg">
    <!-- Rating form UI -->
    <p class="text-gray-500">Rate from 1 to 5</p>
    <input
      v-model="ratingValue"
      placeholder="1-5"
      type="number"
      min="1"
      max="5"
      class="w-12 px-2 py-1 border border-gray-300 rounded-md focus:outline-none"
    />
    <button
      @click="submitRating"
      class="bg-gray-100 text-[#10A37F] rounded-md p-2"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-5 h-5"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"
        />
      </svg>
    </button>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { toast } from "vue3-toastify";

export default {
  data() {
    return {
      ratingValue: 1,
    };
  },
  methods: {
    ...mapActions(["createRating"]),
    async submitRating() {
      try {
        const response = await this.createRating({
          recipeId: this.recipeId,
          rating: this.ratingValue,
        });
        this.ratingValue = "";
        // Clear the input field or handle success/error messages
        if (response) {
          toast.success(response.message, {
            autoClose: 2000,
          });
        } else {
          toast.error(response.message, {
            autoClose: 2000,
          });
        }
      } catch (error) {
        toast.error("Please Login!", {
          autoClose: 2000,
        });
        console.error("Error creating rating:", error);
      }
    },
  },
  props: {
    recipeId: Number,
  },
};
</script>
