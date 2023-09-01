<template>
  <nav class="sticky top-0 z-50 w-full bg-gray-200 p-4 flex items-center justify-between">
    <div class="flex items-center ml-20">
      <h1 class="text-2xl font-semibold">RacipeRadar</h1>
    </div>
    <div class="flex items-center space-x-4 mr-20">
      <router-link to="/" class="text-black">Home</router-link>
      <router-link to="/recipe/create" class="text-black">Create</router-link>
      <router-link to="/login" class="text-black">Login</router-link>
      <router-link to="/signup" class="text-black">Signup</router-link>
    </div>
  </nav>
</template>

  
  <script>
  export default {};
  </script>
  
  <style scoped>
  /* Add your Tailwind CSS classes here */
  </style>
  