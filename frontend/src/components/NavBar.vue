<template>
  <nav
    class="sticky top-0 z-50 w-full bg-gray-200 p-4 flex items-center justify-between"
  >
    <div class="flex items-center ml-4 md:ml-20">
      <router-link :to="'/'">
        <h1 class="lg:text-2xl md:text-1xl font-semibold">RacipeRadar</h1>
      </router-link>
    </div>
    <div class="md:flex items-center space-x-4 mr-4 md:mr-20">
      <!-- Hamburger menu icon for medium and small screens -->
      <div class="md:hidden">
        <button @click="toggleMenu" class="text-black">
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
              d="M3.75 5.25h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5m-16.5 4.5h16.5"
            />
          </svg>
        </button>
      </div>
      <!-- Navigation links for medium and large screens -->
      <div class="hidden md:flex items-center space-x-4">
        <router-link to="/" class="text-black">Home</router-link>
        <router-link to="/recipe/create" class="text-black">Create</router-link>

        <router-link v-if="!isLoggedIn" to="/signup" class="text-black"
          >Signup</router-link
        >
        <!-- Display "Login" or "Logout" based on the isLoggedIn state -->
        <router-link v-if="!isLoggedIn" to="/login" class="text-black"
          >Login</router-link
        >
        <router-link v-else to="/" class="text-black" @click="logout"
          >Logout</router-link
        >
      </div>
    </div>
    <!-- Mobile menu (hidden by default) -->
    <div
      class="md:hidden absolute top-16 left-0 w-full bg-gray-200 text-black"
      v-show="isMobileMenuOpen"
    >
      <!-- Navigation links for small screens -->
      <div class="flex flex-col items-center py-4 space-y-4">
        <router-link to="/" class="text-black">Home</router-link>
        <router-link to="/recipe/create" class="text-black">Create</router-link>

        <router-link v-if="!isLoggedIn" to="/signup" class="text-black"
          >Signup</router-link
        >
        <!-- Display "Login" or "Logout" based on the isLoggedIn state -->
        <router-link v-if="!isLoggedIn" to="/login" class="text-black"
          >Login</router-link
        >
        <router-link v-else to="/" class="text-black" @click="logout"
          >Logout</router-link
        >
      </div>
    </div>
  </nav>
</template>

<script>
import { useStore } from "vuex"; // Import useStore here
import { useRouter } from "vue-router";
import { computed, ref } from "vue";
import { toast } from "vue3-toastify";
export default {
  setup() {
    const store = useStore(); // Access the Vuex store
    const router = useRouter();
    const isMobileMenuOpen = ref(false);

    const toggleMenu = () => {
      isMobileMenuOpen.value = !isMobileMenuOpen.value;
    };

    const logout = () => {
      // Clear the token from localStorage
      localStorage.removeItem("token");
      toast.success("Logged out successfully!", {
        autoClose: 1500,
      });
      // Use the store to commit the mutation
      store.commit("setLoggedIn", false);
      // Redirect to the home page
      router.push("/");
    };

    // Get the login status from the store
    const isLoggedIn = computed(() => store.state.isLoggedIn);

    return {
      toggleMenu,
      isMobileMenuOpen,
      logout,
      isLoggedIn,
    };
  },
};
</script>

<style scoped>
/* Add your Tailwind CSS classes here */
</style>
