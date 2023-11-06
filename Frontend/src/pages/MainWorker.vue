<script setup>
import Header from '@/components/Header.vue'
import Task from '@/components/Task.vue'
import Navbar from '@/components/Navbar.vue';
import {ref, onMounted} from 'vue'
import { useTasksStore } from '../stores/TasksStore';


const tasksStore = useTasksStore();

onMounted(() => {
})

</script>

<template>
  <Header></Header>
  <div class="main-header">
    <div class="main-header__tasks active">
      Мои задачи
    </div>
  </div>
  <div class="container">
    <Navbar class="navbar"/>
    <div class="tasks-block tasks-block-current" v-if="tasksStore.activeTab == 1">
      <template v-for="(task) in tasksStore.currentTasks">
        <Task v-if="task.status != 4" 
          :key="task.address"
          :task="task"
        />
      </template>
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

<style scoped>
  body {
    background-position-y: 70%
  }
  .container {
    display: grid;
    grid-template-columns: 2fr 10fr;
    grid-template-rows: 100%;
    grid-template-areas: "navbar tasks";
  }

  .navbar {
    grid-area: 'navbar';
  }

  .tasks-block {
    grid-area: 'tasks';
    display: grid;
    grid-template-columns: 30% 30% 30%;
    grid-template-rows: fit-content fit-content;
    gap: 15px;
  }

  .main-header {
    height: 41px;
    margin-top: 10px;
    padding: 0 37px 0 37px;
    margin-bottom: 14px;
    font-size: 34px;
    color: #FFFFFF;
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
