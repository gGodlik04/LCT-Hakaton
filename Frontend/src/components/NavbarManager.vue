<script setup>
import { ref, computed } from 'vue'
import { useManagerStore } from '@/stores/ManagerStore';
import { storeToRefs } from 'pinia';

const managerStore = useManagerStore();
const {activeTab} = storeToRefs(managerStore)


const changeTab = (id) => {
    managerStore.setActiveTab(id);
}


</script>

<template>
    <div class="navbar">
        <div 
            @click="changeTab(1)" 
            class="navbar__points" 
            :class="(activeTab == 1) ? 'active' : ''"
        >
            Агентские точки
        </div>
        <div 
            @click="changeTab(2)" 
            class="navbar__directory-tasks"
            :class="(activeTab == 2) ? 'active' : ''"
        >
            Справочник задач
        </div>
        <div 
            @click="changeTab(3)" 
            class="navbar__directory-employees"
            :class="(activeTab == 3) ? 'active' : ''"
        >
            Справочник сотрудников
        </div>
        <div 
            @click="changeTab(4)" 
            class="navbar__completed"
            :class="(activeTab == 4) ? 'active' : ''"
        >
        Информационная панель
        </div>
    </div>
</template>

<style scoped>
.navbar {
    color: #FFFFFF;
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
</style>