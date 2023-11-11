<script setup>
import Logo from '@/components/icons/Logo.vue'
import Profile from '@/components/icons/Profile.vue'
import Gps from '@/components/icons/Gps.vue'
import NavbarIcon from '@/components/icons/NavbarIcon.vue'
import { useGlobalStore } from '@/stores/GlobalStore';
import { useTasksStore } from '../stores/TasksStore';
import { onMounted, computed, ref} from 'vue';

const tasksStore = useTasksStore();
const globalStore = useGlobalStore();

const setTheme = (themeName) => {
  localStorage.setItem('theme', themeName);
  document.documentElement.className = themeName;
}

const flagTheme = ref('theme-dark')
const employeeInfo = ref();

onMounted(() => {
    employeeInfo.value = tasksStore.getEmployeeInfo
    console.log(employeeInfo.value.first_name);
    if (localStorage.getItem('theme') === 'theme-light') {
        setTheme('theme-light');
        document.getElementById('slider').checked = true;
    } else {
        setTheme('theme-dark');
        document.getElementById('slider').checked = false;
    }
    flagTheme.value = localStorage.getItem('theme');
})

const isLoginPage = computed(() => {
    return (window.location.pathname == '/login') ? true : false
})

const toggleTheme = () => {
  if (localStorage.getItem('theme') === 'theme-light') {
      setTheme('theme-dark');
  } else {
      setTheme('theme-light');
  }
  flagTheme.value = localStorage.getItem('theme');
}

</script>

<template>
    <div class="header" :class="isLoginPage ? 'header-login' : ''">
        <div 
            class="header__gps-navbar" 
            :class="isLoginPage ? 'header__gps-navbar-hidden' : ''"
            @click="openNavbarMobile"
        >
            <NavbarIcon 
                @click="globalStore.toggleNavbar" 
                class="header__gps-navbar_navbar" 
            />
            <Gps
                class="header__gps-navbar_gps"
                :theme="flagTheme"
            />
        </div>
        <div class="header__gps-navbar_logo">
            <Logo
                :theme="flagTheme"
            />
        </div>
        <div class="header__auth">
            <div class="header__auth-employee">
                {{ employeeInfo?.first_name }} {{ employeeInfo?.last_name }}
            </div>
            <div class="header__auth_icon">
                <Profile
                    :theme="flagTheme"
                />
            </div>
            <div class="change-theme">
                <label id="switch" class="switch">
                <input type="checkbox" @change="toggleTheme" id="slider">
                <span class="slider round"></span>
            </label>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">

    .header {
        margin-left: auto;
    }
    .header {
        display: flex;
        justify-content: space-between;
        padding: 20px 50px 20px 50px;
        color: var(--font-color);
        border-bottom-left-radius: 20px;
        border-bottom-right-radius: 20px;
    }

    .header__gps-navbar_logo {
        position: relative;
        bottom: 4px;
        left: 140px;
    }

    .header__gps-navbar {
        display: flex;
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

    .header__gps-navbar_navbar {
        margin-right: 20px;
        display: none;
    }

    .header__gps-navbar_gps {
        position: relative;
        bottom: 5px;
    }

    .change-theme {
        position: relative;
        bottom: 5px;
        margin-left: 15px;
    }

    .switch {
        position: relative;
        display: inline-block;
        width: 60px;
        height: 34px;
    }

/* Hide default HTML checkbox */
    .switch input {
    opacity: 0;
    width: 0;
    height: 0;
    }

/* The slider */
    .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    -webkit-transition: 0.4s;
    transition: 0.4s;
    }

    .slider:before {
    position: absolute;
    content: "";
    height: 40px;
    width: 40px;
    left: 0px;
    bottom: 4px;
    top: 0;
    bottom: 0;
    margin: auto 0;
    -webkit-transition: 0.4s;
    transition: 0.4s;
    box-shadow: 0 0px 15px #2020203d;
    background: white url('https://i.ibb.co/FxzBYR9/night.png');
    background-repeat: no-repeat;
    background-position: center;
    }

    input:checked + .slider {
    background-color: #213A8B;
    }

    input:focus + .slider {
    box-shadow: 0 0 1px #F1F1F1
    }

    input:checked + .slider:before {
    -webkit-transform: translateX(24px);
    -ms-transform: translateX(24px);
    transform: translateX(24px);
    background: white url('https://i.ibb.co/7JfqXxB/sunny.png');
    background-repeat: no-repeat;
    background-position: center;
    }

    /* Rounded sliders */
    .slider.round {
    border-radius: 34px;
    }

    .slider.round:before {
    border-radius: 50%;
    }

    @media (max-width: $screen-sm) {
        .header-login {
            justify-content: center;
        }
        .header__gps-navbar-hidden {
            display: none;
        }
        .header__gps-navbar_navbar {
            display: block;
        }

        .header__auth {
            display: none;
        }

        .header__gps-navbar_logo {
            position: relative;
            left: 0px;
        }
        
        
        @media (max-width: $screen-small) {
        .header__gps-navbar_gps {
            display: none;
        }
    }
    }
</style>
