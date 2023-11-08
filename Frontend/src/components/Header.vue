<script setup>
import Logo from '@/components/icons/Logo.vue'
import Profile from '@/components/icons/Profile.vue'
import Gps from '@/components/icons/Gps.vue'
import { onMounted } from 'vue';

function setTheme(themeName) {
  localStorage.setItem('theme', themeName);
  document.documentElement.className = themeName;
}

onMounted(() => {
  () => {
      if (localStorage.getItem('theme') === 'theme-light') {
          setTheme('theme-light');
          document.getElementById('slider').checked = true;
      } else {
          setTheme('theme-dark');
        document.getElementById('slider').checked = false;
      }
  };
})

function toggleTheme() {
  if (localStorage.getItem('theme') === 'theme-light') {
      setTheme('theme-dark');
  } else {
      setTheme('theme-light');
  }
}
</script>

<template>
    <div class="header">
        <div class="header__gps">
            <Gps/>
        </div>
        <div class="header__logo">
            <Logo/>
        </div>
        <div class="change-theme">
            <label id="switch" class="switch">
            <input type="checkbox" @change="toggleTheme" id="slider">
            <span class="slider round"></span>
        </label>
        </div>
        <div class="header__auth">
            <div class="header__auth_employee">Дерягин Н. В.</div>
            <div class="header__auth_icon">
                <Profile/>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
    .header {
        display: flex;
        justify-content: space-between;
        padding: 20px 50px 20px 50px;
        color: #FFFFFF;
        background-color: var(--color-header);
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 20px;
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
