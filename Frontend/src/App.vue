<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useTasksStore } from '@/stores/TasksStore';
import { onMounted } from 'vue';
import { useGlobalStore } from '@/stores/GlobalStore';
import router from '@/router';

const globalStore = useGlobalStore();

const tasksStore = useTasksStore();
</script>

<template>
  <div class="app">
    <ModalLoading v-show="globalStore.isLoading" class="loading"></ModalLoading>
    <RouterView></RouterView>
  </div>
  
</template>

<style scoped>
  .loading {
    position: absolute;
    top: 40%;
    left: 40%;
  }
</style>
