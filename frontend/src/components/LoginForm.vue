<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <form @submit.prevent="submitForm" class="bg-white p-20 rounded shadow-sm">
      <div class="text-center mb-4">
        <h2 class="text-2xl font-semibold">Welcome Back!</h2>
      </div>
      <fieldset class="mb-4">
        <div class="mb-2">
          <label for="username" class="block text-sm font-medium text-[#10A37F]"
            >Username:</label
          >
          <input
            v-model="username"
            type="text"
            id="username"
            class="mt-1 px-3 py-2 w-full rounded border border-[#10A37F] focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200"
          />
        </div>
        <div class="mb-2">
          <label for="password" class="block text-sm font-medium text-[#10A37F]"
            >Password:</label
          >
          <input
            v-model="password"
            type="password"
            id="password"
            class="mt-1 px-3 py-2 w-full rounded border border-[#10A37F] focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200"
          />
        </div>
      </fieldset>
      <div class="flex items-center justify-center">
        <button
          type="submit"
          :disabled="loading"
          class="bg-[#10A37F] text-white px-4 py-2 rounded hover:bg-white hover:text-[#10A37F] focus:outline-none focus:ring focus:ring-blue-200 flex items-center"
        >
          <span v-if="loading" class="mr-2 animate-spin"> &#9696; </span>
          Log In
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import { ref } from "vue";
import { useRouter } from "vue-router"; // Import the useRouter function
import { useStore } from "vuex";  

export default {
  setup() {
    const router = useRouter(); // Use the useRouter function to get the router instance
    const store = useStore();
    
    const username = ref("");
    const password = ref("");
    const errorMessage = ref("");
    const errorMessageUsername = ref("");
    const errorMessagePassword = ref("");
    const loading = ref(false);

    const submitForm = async () => {
      loading.value = true;
      try {
        const response = await axios.post("http://localhost:8000/api/login/", {
          username: username.value,
          password: password.value,
        });
        // Store the token in localStorage
        localStorage.setItem("token", response.data.token);
        
        // Commit the mutation to set isLoggedIn to true
        store.commit("setLoggedIn", true);
        
        toast.success(response.data.message, {
          autoClose: 1000,
        });
        
        errorMessage.value = "";
        errorMessageUsername.value = "";
        errorMessagePassword.value = "";
        console.log(response);
        // Redirect to home page using the router instance
        setTimeout(() => {
          router.push("/");
        }, 1500);
      } catch (error) {
        console.log(error);
        toast.error("Invalid credentials", {
          autoClose: 1000,
        });
      } finally {
        loading.value = false;
      }
    };

    return { username, password, errorMessage, loading, submitForm };
  },
};
</script>
