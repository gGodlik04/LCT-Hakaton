<script setup>

</script>

<template>
    <div class="navbar">
        <div class="navbar__current active">
            Текущие
        </div>
        <div class="navbar__map">
            На карте
        </div>
        <div class="navbar__week">
            На неделю
        </div>
        <div class="navbar__completed">
            Выполненные
        </div>
        <div class="navbar__favorites">
            Избранные
        </div>
    </div>
</template>

<style scoped>
.navbar {
    color: #FFFFFF;
    font-size: 19px;
    padding: 0 37px 0 37px;
    display: flex;
    flex-direction: column;
    gap: 37px;
    margin-top: 24px;
    font-family: 'MontseratReg';
}

.active {
    color: #AA1418;
  }
.active::after {
    content: "\25CF";
    padding-left: 30px;
  }
</style>