<script setup>
import Header from '@/components/Header.vue'
import Task from '@/components/Task.vue'
import {ref, onMounted} from 'vue'
import { useTasksStore } from '../stores/TasksStore';


const tasksStore = useTasksStore();

onMounted(() => {
})

</script>

<template>
  <Header></Header>
  <div class="container">
    <div class="tasks">
      <div class="tasks__title">
        Мои задачи
      </div>
      <div class="tasks__date">
        <div class="tasks__date_today">
          Сегодня
        </div>
        <div class="tasks__date_week">
          Неделя
        </div>
      </div>
    </div>
    <div class="map">
      <div class="map__time-to-end-day">
        До конца рабочего дня: 8 часов
      </div>
    </div>
    <Task v-for="(task) in tasksStore.tasks" 
      :key="task.address"
      :task="task"
    />
  </div>
</template>

<style scoped>

</style>
