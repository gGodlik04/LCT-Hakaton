<script setup>
import Header from '@/components/Header.vue'
import {ref, onMounted} from 'vue'
import { useTasksStore } from '../stores/TasksStore';


const tasksStore = useTasksStore();


const email = ref('');
const password = ref('');

const loginFormSubmit = () => {
  tasksStore.login(email.value, password.value)
}


</script>

<template>
  <Header></Header>
  <div class="login-wrapper"></div>
  <div class="login login-bg">
    <div class="login__title">Добро пожаловать!</div>
    <div class="login__role">
      <div class="login__role_manager active">Менеджер</div>
      <div class="login__role_worker">Сотрудник</div>
    </div>
    <div class="login__form"></div>
      <form class="login__form-auth">
        <input class="login__form-auth_input" v-model="email" type="text" autofocus placeholder="Введите email">
        <input class="login__form-auth_input" v-model="password" type="password" placeholder="Введите пороль">
        <ButtonUI @click="loginFormSubmit" class="login__from-auth_submit-buttonUI">Войти</ButtonUI>
      </form>
  </div>
</template>

<style scoped lang="scss">
  .login-wrapper {
    height: 15vh;
  }
  .login {
    padding: 43px 75px 43px 75px;
    margin-top: auto;
    margin-bottom: auto;
    color: var(--color-secondary);
    margin-left: auto;
    margin-right: auto;
    height: 350px;
    font-weight: 500;
    border-radius: 30px;
    width: 15%;
    border: 3px solid #646464;
    background: var(--color-accent);
    backdrop-filter: blur(2px);
    color: var(--font-color-inactive);
  }
  .login__title {
    font-size: 23px;
    text-align: center;
    color: var(--font-color);
  }

  .login__role {
    opacity: initial;
    display: flex;
    margin-top: 32px;
    font-size: 20px;
    justify-content: space-between;
    align-self: center;
  }

  .login__form-auth {
    display: flex;
    margin-top: 18px;
    flex-direction: column;
    align-items: center;
  }

  .login__form-auth_input {
    height: 45px;
    width: 100%;
    margin-top: 25px;
    border-radius: 10px;
    border: none;
    color: var(--input-color-text);
    background-color: var(--input-color);
    text-align: center;
    font-size: 19px;
  }
  
  .active {
    color: var(--button-color);
  }
  .active:after {
    content: '';
    display: block;
    height: 3px; 
    background: var(--button-color);
    width: 100%; 
    margin-top: 20px; 
	  transition: 1s; 
  }

  .login__from-auth_submit-button {
    display: none;
  }

  .login__from-auth_submit-buttonUI {
    scale: 0.9;
    margin-top: 35px;
  }
  .login__from-auth_submit-buttonUI:hover {
    scale: 1;
  }

  .theme-light {
    .login {
      border: 0px; 
      box-shadow: 0px 0px 17px rgba(0, 0, 0, 0.25);
    }
  }
</style>
