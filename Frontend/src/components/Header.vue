<script setup>
import Logo from '@/components/icons/Logo.vue'
import Profile from '@/components/icons/Profile.vue'
</script>

<template>
    <div class="header">
        <div class="header__logo">
            <Logo/>
        </div>
        <div class="header__auth">
            <div class="header__auth_employee">Василий Петрович</div>
            <div class="header__auth_icon">
                <Profile/>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .header {
        background-color: #FFFFFF;
        display: flex;
        justify-content: space-between;
        padding: 20px;
        color: #213A8B;
    }
    
    .header__auth_employee {
        font-size: 25px;
        vertical-align: middle;
    }

    .header__auth {
        display: flex;
    }
</style>
