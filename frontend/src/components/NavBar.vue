<template>
  <nav class="sticky top-0 z-50 w-full bg-gray-200 p-4 flex items-center justify-between">
    <div class="flex items-center ml-20">
      <router-link :to="'/'">
        <h1 class="text-2xl font-semibold">RacipeRadar</h1>
      </router-link>
    </div>
    <div class="flex items-center space-x-4 mr-20">
      <router-link to="/" class="text-black">Home</router-link>
      <router-link to="/recipe/create" class="text-black">Create</router-link>
      
      <router-link v-if="!isLoggedIn" to="/signup" class="text-black">Signup</router-link>
      <!-- Display "Login" or "Logout" based on the isLoggedIn state -->
    <router-link v-if="!isLoggedIn" to="/login" class="text-black">Login</router-link>
    <router-link v-else to="/" class="text-black" @click="logout">Logout</router-link>
    </div>
  </nav>
</template>

<script>
import { useStore } from "vuex"; // Import useStore here
import { useRouter } from "vue-router";
import { computed } from "vue";
import { toast } from "vue3-toastify";
export default {
  setup() {
    const store = useStore(); // Access the Vuex store
    const router = useRouter();

    const logout = () => {
      // Clear the token from localStorage
      localStorage.removeItem("token");
      toast.success("Logged out successfully!",{
        autoClose:1500
      })
      // Use the store to commit the mutation
      store.commit("setLoggedIn", false);
      // Redirect to the home page
      router.push("/");
    };

    // Get the login status from the store
    const isLoggedIn = computed(() => store.state.isLoggedIn);

    return {
      logout,
      isLoggedIn,
    };
  },
};
</script>

<style scoped>
/* Add your Tailwind CSS classes here */
</style>
