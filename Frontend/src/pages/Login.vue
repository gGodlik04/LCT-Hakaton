<script setup>
import Header from '@/components/Header.vue'

</script>

<template>
  <Header></Header>
  <div class="login">
    <div class="login__title">Добро пожаловать!</div>
    <div class="login__role">
      <div class="login__role_manager active">Менеджер</div>
      <div class="login__role_worker">Сотрудник</div>
    </div>
    <div class="login__form"></div>
      <form class="login__form-auth" method="#">
        <input class="login__form-auth_input" type="text" autofocus placeholder="Введите логин">
        <input class="login__form-auth_input" type="password" placeholder="Введите пороль">
      </form>
  </div>
</template>

<style scoped>
  .login {
    padding: 43px 75px 43px 75px;
    margin-top: 200px;
    margin-left: auto;
    margin-right: auto;
    height: 400px;
    font-weight: 500;
    border-radius: 30px;
    width: 20%;
    background-color: #FFFFFF;
  }
  .login__title {
    font-size: 30px;
    text-align: center;
  }

  .login__role {
    display: flex;
    margin-top: 32px;
    font-size: 30px;
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
    height: 66px;
    width: 100%;
    margin-top: 36px;
    border-radius: 10px;
    border: none;
    background-color: #F1F1F1;
    text-align: center;
    font-size: 24px;
  }
  
  .active {
    color: #213A8B;
  }
  .active:after {
    content: '';
    display: block;
    height: 3px; 
    background: #213A8B; 
    width: 100%; 
    margin-top: 20px; 
	  transition: 1s; 
  }
</style>
