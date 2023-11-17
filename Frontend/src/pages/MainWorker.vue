<script setup>
import Header from '@/components/Header.vue'
import Task from '@/components/Task.vue'
import NavbarEmployee from '@/components/NavbarEmployee.vue';
import {ref, onMounted, computed, toRaw} from 'vue'
import { useTasksStore } from '../stores/TasksStore';
import { useGlobalStore } from '../stores/GlobalStore';
import TasksDependsTab from '@/components/TasksDependsTab.vue';
import YandexMapBlock from '@/components/YandexMapBlock.vue';


const tasksStore = useTasksStore();
const globalStore = useGlobalStore();

const tasks = ref()
const show = ref(false)

onMounted(async () => {
  await tasksStore.fetchTasks()
  tasks.value = tasksStore.getAllTasks
})

</script>

<template>
  <Header></Header>
  <!-- <ModalWindow v-model:show="modalVisible">
  </ModalWindow> -->
  <div class="main-header">
    Мои задачи
  </div>
  <div class="container">
    <NavbarEmployee 
      class="navbar"
      :class="globalStore.getFlagNavbar ? 'active-navbar' : 'inactive-navbar'"
    />
    <div class="tasks-block tasks-block-current" v-if="tasksStore.activeTab == 1">
        <TasksDependsTab
         :tasks="tasks" 
        />
    </div>
    <div class="tasks-block map-block" v-if="tasksStore.activeTab == 2">
        <YandexMapBlock/>
    </div>
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

  .navbar {
    grid-area: 'navbar';
  }

  .tasks-block {
    grid-area: 'tasks';
    // display: grid;
    // grid-template-columns: 31% 31% 31%;
    // grid-template-rows: 50% 50%;
    // gap: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    // flex: 1 266.66px 266.66px;
    gap: 20px;
  }

  @media (max-width: $screen-md) {
    .container {
      display: block;
    }
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
    margin-right: 10px;
    margin-top: 10px;
  }

  .active {
    color: #AA1418;
  }

  @media (max-width: $screen-md) {
    .navbar {
        position: absolute;
        margin-top: 0;
        top: 0;
        z-index: 999;
        height: 100vh;
        width: fit-content;
        background: var(--color-accent-mobile);
        backdrop-filter: blur(20px);
        display: none;
    }
    // .tasks-block {
    //   grid-area: 'tasks';
    //   display: grid;
    //   grid-template-columns: 50% 50%;
    //   grid-template-rows: fit-content;
    //   gap: 20px;
    //   justify-items: center;
    // }

    // .container {
    //   grid-template-rows: fit-content 1%;
    //   grid-template-areas: "navbar tasks" "navbar navigation";
    // }
    
    .navigation {
      margin: 16px 0px 11px 135px;
    }
  }
  // @media (max-width: $screen-sm) {
  //   .tasks-block {
  //     grid-area: 'tasks';
  //     display: grid;
  //     grid-template-columns: 50% 50%;
  //     grid-template-rows: fit-content fit-content;
  //     gap: 20px;
  //     justify-items: center;
  //   }

  //   .container {
  //     align-content: center;
  //     grid-template-columns: 100% 50%;
  //     grid-template-rows: fit-content 1%;
  //     grid-template-areas: "tasks tasks" "navigation navigation";
  //   } 

  // @media (max-width) {
    
  // }

  // @media (max-width: $screen-small) {
  //   .tasks-block {
  //     grid-area: 'tasks';
  //     display: grid;
  //     grid-template-columns: 100%;
  //     grid-template-rows: fit-content fit-content;
  //     gap: 20px;
  //     justify-items: center;
  //   }

  //   .container {
  //     align-content: center;
  //     grid-template-columns: 100% 50%;
  //     grid-template-rows: fit-content 1%;
  //     grid-template-areas: "tasks tasks" "navigation navigation";
  //   } 

  //   .navigation {
  //     margin: 16px 0px 11px 20px;
  //   }

  //   .main-header {
  //     justify-content: center;
  //   }
  // }
// }
@media (max-width: $screen-md) {
    .main-header {
        flex-wrap: wrap;
    }
    .active-navbar {
        display: flex;
    }

    .inactive-navbar {
        display: none;
    }
    .main-header__buttons {
        min-width: 5%;
        font-size: 1px;
    }
    .container-wrapper {
        display: block;
    }
}

@media (max-width: $screen-small) {
    .navbar {
        width: 60%;
    }  
  }
</style>
