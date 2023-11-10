<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useTasksStore } from '@/stores/TasksStore';
import { onMounted } from 'vue';
import { useGlobalStore } from '@/stores/GlobalStore';


const globalStore = useGlobalStore();

const tasksStore = useTasksStore();
</script>

<template>
  <div class="app">
    <ModalLoading v-show="globalStore.isLoading"></ModalLoading>
    <RouterView></RouterView>
  </div>
  
</template>

<style scoped>

</style>
