<script setup>
import { ref, computed } from 'vue'
import { useTasksStore } from '../stores/TasksStore';
import { storeToRefs } from 'pinia';

const tasksStore = useTasksStore();
const {activeTab} = storeToRefs(tasksStore)


const changeTab = (id) => {
    tasksStore.setActiveTab(id);
}


</script>

<template>
    <div class="navbar">
        <div 
            @click="changeTab(1)" 
            class="navbar__current" 
            :class="(activeTab == 1) ? 'active' : ''"
        >
            Текущие
        </div>
        <div 
            @click="changeTab(2)" 
            class="navbar__map"
            :class="(activeTab == 2) ? 'active' : ''"
        >
            На карте
        </div>
        <!-- <div 
            @click="changeTab(3)" 
            class="navbar__week"
            :class="(activeTab == 3) ? 'active' : ''"
        >
            На неделю
        </div> -->
        <div 
            @click="changeTab(4)" 
            class="navbar__completed"
            :class="(activeTab == 4) ? 'active' : ''"
        >
            Выполненные
        </div>
        <div 
            @click="changeTab(5)" 
            class="navbar__favorites"
            :class="(activeTab == 5) ? 'active' : ''"
        >
            Избранные
        </div>
    </div>
</template>

<style scoped lang="scss">
.navbar {
    color: var(--font-color);
    font-size: 19px;
    padding: 0 37px 0 37px;
    display: flex;
    flex-direction: column;
    gap: 37px;
    margin-top: 24px;
    font-family: 'MontseratReg';
}

.active {
    color: #AA1418;
  }
.active::after {
    content: "\25CF";
    padding-left: 30px;
}

@media (max-width: $screen-md) { 
    .navbar:first-child {
        padding-top: 75px;
    }
}
</style>