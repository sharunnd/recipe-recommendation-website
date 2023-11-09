<template>
    <footer class="bg-gray-200 text-black mt-10">
      <div class="container mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col sm:flex-row justify-between items-center">
          <div class="flex items-center">
            <router-link to="/" class="text-black font-semibold text-lg">
              RecipeRadar
            </router-link>           
            <div class="ml-4 space-x-4 mt-2 sm:mt-0">
              <router-link to="/" class="text-Black hover:text-white">About</router-link>
              <router-link to="/" class="text-Black hover:text-white">Blog</router-link>
              <router-link to="/" class="text-Black hover:text-white">Careers</router-link>
              <router-link to="/" class="text-Black hover:text-white">Charter</router-link>
            </div>
          </div>
          <div class="flex mt-4 sm:mt-0">
            <a
              href="#"
              class="text-gray-400 hover:text-white"
              target="_blank"
              rel="noopener noreferrer"
            >
              <i class="fab fa-twitter"></i>
            </a>
            <a
              href="#"
              class="text-gray-400 hover:text-white ml-4"
              target="_blank"
              rel="noopener noreferrer"
            >
              <i class="fab fa-github"></i>
            </a>
            <a
              href="#"
              class="text-gray-400 hover:text-white ml-4"
              target="_blank"
              rel="noopener noreferrer"
            >
              <i class="fab fa-linkedin"></i>
            </a>
          </div>
        </div>
        <hr class="my-8 border-gray-700" />
        <p class="text-center text-Black text-sm">
          &copy; {{ new Date().getFullYear() }} RecipeRadar. All rights reserved.
        </p>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: "FooterVue",
  };
  </script>
  
  <style scoped>
  /* Add any custom styles here */
  </style>
  