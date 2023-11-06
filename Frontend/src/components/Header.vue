<script setup>
import Logo from '@/components/icons/Logo.vue'
import Profile from '@/components/icons/Profile.vue'
import Gps from '@/components/icons/Gps.vue'
</script>

<template>
    <div class="header">
        <div class="header__gps">
            <Gps/>
        </div>
        <div class="header__logo">
            <Logo/>
        </div>
        <div class="header__auth">
            <div class="header__auth_employee">Дерягин Н. В.</div>
            <div class="header__auth_icon">
                <Profile/>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .header {
        display: flex;
        justify-content: space-between;
        padding: 20px 50px 20px 50px;
        color: #FFFFFF;
    }

    .header__logo {
        position: relative;
        left: 75px;
    }
    
    .header__auth_employee {
        font-size: 20px;
        vertical-align: middle;
    }

    .header__auth {
        display: flex;
    }

    .header__auth_icon {
        position: relative;
        bottom: 1px;
        margin-left: 28px;
    }
</style>
