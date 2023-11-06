<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useTasksStore } from '@/stores/TasksStore';


const tasksStore = useTasksStore();
</script>

<template>
  <div class="app">
    <RouterView></RouterView>
  </div>
  
</template>

<style scoped>

</style>
