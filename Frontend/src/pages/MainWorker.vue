<script setup>
import Header from '@/components/Header.vue'
import Task from '@/components/Task.vue'
import NavbarEmployee from '@/components/NavbarEmployee.vue';
import {ref, onMounted} from 'vue'
import { useTasksStore } from '../stores/TasksStore';
import TasksDependsTab from '@/components/TasksDependsTab.vue';


const tasksStore = useTasksStore();

onMounted(() => {
})

</script>

<template>
  <Header></Header>
  <div class="main-header">
    Мои задачи
  </div>
  <div class="container">
    <NavbarEmployee class="navbar"/>
    <div class="tasks-block tasks-block-current" v-if="tasksStore.activeTab == 1">
        <TasksDependsTab
          :tasks="tasksStore.currentTasks"
        />
    </div>
    <!-- <div class="tasks-block tasks-block-current" v-if="tasksStore.activeTab == 1">
        <TasksDependsTab
          :tasks="tasksStore.tasks"
        />
    </div> -->
    <div class="tasks-block tasks-block-week" v-if="tasksStore.activeTab == 3">
        <TasksDependsTab
          :tasks="tasksStore.weekTasks"
        />
    </div>
    <div class="tasks-block tasks-block-completed" v-if="tasksStore.activeTab == 4">
        <TasksDependsTab
          :tasks="tasksStore.completedTasks"
        />
    </div>
    <div class="tasks-block tasks-block-favorites" v-if="tasksStore.activeTab == 5">
        <TasksDependsTab
          :tasks="tasksStore.favoritesTasks"
        />
    </div>
  </div>
  <div class="navigation">
    <div class="navigation-left">
      <ArrowLeft/>
    </div>
    <div class="navigation-right">
      <ArrowRight/>
    </div>
  </div>
</template>

<style scoped lang="scss">
  body {
    background-position-y: 70%
  }
  .container {
    min-height: 80vh;
    display: grid;
    grid-template-columns: 2fr 10fr;
    grid-template-rows: 99% 1%;
    grid-template-areas: "navbar tasks" "navbar navigation";
  } 

  .navigation {
    grid-area: 'navigation';
  }

  .navbar {
    grid-area: 'navbar';
  }

  .tasks-block {
    grid-area: 'tasks';
    display: grid;
    grid-template-columns: 31% 31% 31%;
    grid-template-rows: 50% 50%;
    gap: 20px;
  }

  .main-header {
    height: 41px;
    margin-top: 10px;
    padding: 0 37px 0 37px;
    margin-bottom: 14px;
    font-size: 34px;
    color: var(--font-color);
    display: flex;
    justify-content: space-between;
  }

  .navigation {
    display: flex;
    justify-content: center;
    margin: 16px 0px 11px 195px;
  }

  .active {
    color: #AA1418;
  }
</style>
