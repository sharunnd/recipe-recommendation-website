<template>
  <div class="bg-white p-4 rounded-md shadow-md">
    <!-- Review form UI -->
    <div class="flex items-center justify-center">
      <textarea
        v-model="reviewText"
        class="w-full px-4 py-2 mr-2 border rounded-md border-gray-300 focus:outline-none focus:ring-1 focus:ring-[#10A37F]"
        placeholder="Write your review here"
      ></textarea>
      <button
        @click="submitReview"
        class="bg-gray-100 text-[#10A37F] font-semibold px-4 py-2 rounded-md focus:outline-[#10A37F]  mt-2"
      >
        <svg
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
            d="M6 12L3.269 3.126A59.768 59.768 0 0121.485 12 59.77 59.77 0 013.27 20.876L5.999 12zm0 0h7.5"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { toast } from "vue3-toastify";
export default {
  data() {
    return {
      reviewText: "",
    };
  },
  methods: {
    ...mapActions(["createReview"]),
    async submitReview() {
      try {
        const response = await this.createReview({
          recipeId: this.recipeId,
          comment: this.reviewText,
        });
        this.reviewText = "";
        // Show the message from the response
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
        console.error("Error creating review:", error);
      }
    },
  },
  props: {
    recipeId: Number,
  },
};
</script>
