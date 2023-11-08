<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useTasksStore } from '@/stores/TasksStore';
import { onMounted } from 'vue';

const tasksStore = useTasksStore();
</script>

<template>
  <div class="app">
    <RouterView></RouterView>
  </div>
  
</template>

<style scoped>

</style>
