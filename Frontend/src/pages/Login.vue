<script setup>
import Header from '@/components/Header.vue'

</script>

<template>
  <Header></Header>
  <div class="login">
    <div class="login__title">Добро пожаловать!</div>
    <div class="login__role">
      <div class="login__role_manager">Менеджер</div>
      <div class="login__role_worker">Сотрудник</div>
    </div>
    <div class="login__form"></div>
      <form method="#">
        <input type="text" autofocus placeholder="Введите логин">
        <input type="password" placeholder="Введите пороль">
      </form>
  </div>
</template>

<style scoped>
  .login {
    height: 200px;
    weight: 300px;
    background-color: #FFFFFF;
  }
</style>
