<script setup>
import { ref, computed } from 'vue'
import { useManagerStore } from '@/stores/ManagerStore';
import { storeToRefs } from 'pinia';
import { useGlobalStore } from '@/stores/GlobalStore';


const globalStore = useGlobalStore();

const managerStore = useManagerStore();
const {activeTab} = storeToRefs(managerStore)

</script>

<template>
    <div class="navbar-manager">
        <Close 
            class="navbar-manager-close"
            @click="globalStore.toggleNavbar()"
            />
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

<style scoped lang="scss">

.active {
    color: #AA1418;
}
.active::after {
    content: "\25CF";
    padding-left: 30px;
}
.navbar-manager-close {
    display: none;
}

.navbar-manager {
    color: var(--font-color) !important;
}

@media (max-width: $screen-md) { 
    .navbar-manager-close {
        display: block;
        align-self: end;
        margin-top: 20px;
    }
    .navbar-manager:nth-child(2n){
        padding-top: 75px;
    }
}
</style>