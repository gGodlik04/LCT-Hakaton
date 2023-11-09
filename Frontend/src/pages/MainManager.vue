<script setup>
import NavbarManager from '../components/NavbarManager.vue';
import { useManagerStore } from '../stores/ManagerStore';
import Header from '@/components/Header.vue'
import ManagerPointsTable from '@/components/ManagerPointsTable.vue'
import ManagerTaskDirectoryTable from '@/components/ManagerTaskDirectoryTable.vue'
import ManagerEmployeesTable from '@/components/ManagerEmployeesTable.vue'
import InfoPanelManager from '../components/InfoPanelManager.vue';


const managerStore = useManagerStore();

</script>

<template>
<Header></Header>
<div class="main-header">
    <div class="main-header__title">
        Задачи
    </div>
    <div class="main-header__buttons">
        <ButtonUI class="main-header__button main-header__buttons-create-point" v-if="managerStore.activeTab == 1">Добавить точку</ButtonUI>
        <ButtonUI class="main-header__button main-header__buttons-create-employee" v-if="managerStore.activeTab == 3">Добавить сотрудника</ButtonUI>
        <ButtonUI class="main-header__button main-header__buttons-upload-file">
            <UploadFile/>
            Добавить точку
        </ButtonUI>
    </div>
</div>
<div class="container-wrapper">
    <NavbarManager class="navbar"/>
    <div class="content-main" v-if="managerStore.activeTab == 1">
        <ManagerPointsTable
            :dataTable="managerStore.getDataPoints"
        />
    </div>
    <div class="content-main" v-if="managerStore.activeTab == 2">
        <ManagerTaskDirectoryTable
            :dataTable="managerStore.getDataTasks"
        />
    </div>
    <div class="content-main" v-if="managerStore.activeTab == 3">
        <ManagerEmployeesTable
            :dataTable="managerStore.getDataEmployees"
        />
    </div>
    <div class="content-main" v-if="managerStore.activeTab == 4">
        <InfoPanelManager/>
    </div>
  </div>
</template>

<style scoped lang="scss">

.container-wrapper {
    display: grid;
    grid-template-columns: 2fr 10fr;
    grid-template-rows: 100%;
    grid-template-areas: "navbar content";
  }

.content-main {
    grid-area: "content";
}
.navbar {
    grid-area: 'navbar';
    color: #FFFFFF;
    font-size: 19px;
    padding: 0 37px 0 37px;
    display: flex;
    flex-direction: column;
    gap: 37px;
    margin-top: 24px;
    font-family: 'MontseratReg';
}

.main-header {
    display: flex;
    margin: 0 37px;
    justify-content: space-between;
    color: #FFFFFF;
}

.main-header__title {
    font-size: 34px;
}
.main-header__buttons {
    display: flex;
    gap: 11px;
}

.main-header__button {
    padding: 10px 38px !important;
    min-width: fit-content;
    font-size: 16px;
    border-radius: 5px;
}

.main-header__buttons-upload-file {
    display: flex;
    background-color: #FFFFFF;
    color: #000;
}

.active {
    color: #AA1418;
  }
.active::after {
    content: "\25CF";
    padding-left: 30px;
  }

@media (max-width: $screen-md) {

    html {
        height: 100;
    }
    .main-header {
        flex-wrap: wrap;
    }
    
    
    .main-header__buttons {
        min-width: 5%;
        font-size: 1px;
    }
    .navbar-manager {
        position: absolute;
        margin-top: 0;
        top: 0;
        z-index: 999;
        height: 100vh;
        width: 100vw;
        background: var(--color-accent-mobile);
        backdrop-filter: blur(20px);
        // display: none;
    }
    .container-wrapper {
        display: block;
    }
}


@media (max-width: $screen-sm) {
    .main-header__title {
        font-size: 26px;
    }

    .main-header__button {
        padding: 10px 15px !important;
        font-size: 14px;
    }
}

@media (max-width: $screen-small) {
    .main-header__button {
        display: block;
        margin-top: 10px;
        text-align: center;
        border-radius: 5px;
        width: 90%;
        min-width: 0;
    }
    .main-header__buttons {
        display: block;
        margin-top: 10px;
    }
    .main-header {
        display: block;
        justify-content: center;
    }
}
</style>