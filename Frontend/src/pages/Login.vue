<script setup>
import Header from '@/components/Header.vue'

  const loginFormSubmit = (e) => {
    document.querySelector('.login__from-auth_submit-button').click();
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
      <form class="login__form-auth" method="post" action="">
        <input class="login__form-auth_input" type="text" autofocus placeholder="Введите логин">
        <input class="login__form-auth_input" type="password" placeholder="Введите пороль">
        <input type="submit" class="login__from-auth_submit-button"/>
        <ButtonUI @click="loginFormSubmit" class="login__from-auth_submit-buttonUI">Войти</ButtonUI>
      </form>
  </div>
</template>

<style scoped>
  .login-wrapper {
    height: 15vh;
  }
  .login {
    padding: 43px 75px 43px 75px;
    margin-top: auto;
    margin-bottom: auto;
    color: #FFFFFF;
    margin-left: auto;
    margin-right: auto;
    height: 350px;
    font-weight: 500;
    border-radius: 30px;
    width: 15%;
    border: 3px solid #646464;
    background: rgba(0, 9, 31, 0.8);
    backdrop-filter: blur(2px);
  }
  .login__title {
    font-size: 23px;
    text-align: center;
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
    background-color: #D0D0D0;
    text-align: center;
    font-size: 19px;
  }
  
  .active {
    color: #AA1418;
  }
  .active:after {
    content: '';
    display: block;
    height: 3px; 
    background: #AA1418; 
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
</style>
