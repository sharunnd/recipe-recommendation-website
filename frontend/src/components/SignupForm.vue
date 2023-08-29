<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100">
      <form @submit.prevent="submitForm" class="bg-white p-20 rounded shadow-sm">
        <div class="text-center mb-4">
          <h2 class="text-2xl font-semibold">Create your account</h2>
        </div>
        <fieldset class="mb-4">
          <div class="mb-2">
            <label for="username" class="block text-sm font-medium text-[#10A37F]">Username:</label>
            <input v-model="username" type="text" id="username" class="mt-1 px-3 py-2 w-full rounded border border-[#10A37F] focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200" />
            <p v-if="errorMessageUsername" class="mt-4 text-red-600">{{ errorMessageUsername }}</p>
        </div>
          <div class="mb-2">
            <label for="email" class="block text-sm font-medium text-[#10A37F]">Email:</label>
            <input v-model="email" type="email" id="email" class="mt-1 px-3 py-2 w-full rounded border border-[#10A37F] focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200" />
          </div>
          <div class="mb-2">
            <label for="password" class="block text-sm font-medium text-[#10A37F]">Password:</label>
            <input v-model="password" type="password" id="password" class="mt-1 px-3 py-2 w-full rounded border border-[#10A37F] focus:outline-none focus:border-blue-500 focus:ring focus:ring-blue-200" />
            <p v-if="errorMessagePassword" class="mt-4 text-red-600">{{ errorMessagePassword }}</p>
            
        </div>
        </fieldset>
        <div class="flex items-center justify-center">
          <button
            type="submit"
            :disabled="loading"
            class="bg-[#10A37F] text-white px-4 py-2 rounded hover:bg-white hover:text-[#10A37F] focus:outline-none focus:ring focus:ring-blue-200 flex items-center"
          >
            <span v-if="loading" class="mr-2 animate-spin">
              &#9696;
            </span>
            Sign Up
          </button>
        </div>
        <p v-if="successMessage" class="mt-4 text-green-600">{{ successMessage }}</p>
        
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import { toast } from "vue3-toastify";
  import "vue3-toastify/dist/index.css";
  import { ref } from "vue";
import { useRouter } from "vue-router";
  
  export default {
    setup() {
      const username = ref("");
      const email = ref("");
      const password = ref("");
      const successMessage = ref("");
      const errorMessageUsername = ref("");
      const errorMessagePassword = ref("");
      const loading = ref(false);
      const router = useRouter();
      const submitForm = async () => {
        loading.value = true;
        try {
          const response = await axios.post("http://localhost:8000/api/register/", {
            username: username.value,
            email: email.value,
            password: password.value,
          });
          successMessage.value = response.data.message;
          errorMessageUsername.value = "";
          errorMessagePassword.value = "";
          toast.success(response.data.message, {
            autoClose: 1000,
          });
          setTimeout(() => {
            router.push("/login");
          }, 1500);
        } catch (error) {
            if (error.response.data.username && error.response.data.username.length > 0) {
          errorMessageUsername.value = error.response.data.username[0];
        } else {
          errorMessageUsername.value = "";
        }
        if (error.response.data.password && error.response.data.password.length > 0) {
          errorMessagePassword.value = error.response.data.password[0];
        } else {
          errorMessagePassword.value = "";
        }
        successMessage.value = "";
        toast.error("An error occurred!", {
          autoClose: 1000,
        });
        } finally {
          loading.value = false;
        }
      };
  
      return { username, email, password, successMessage, errorMessageUsername,errorMessagePassword, loading, submitForm };
    },
  };
  </script>
  