<template>
    <div class="btn">
        <slot></slot>
    </div>
</template>
<script>

export default {
    name: 'ButtonUI'
}
</script>
<style>
    .btn {
        width: max-content;
        text-align: center;
        min-width: 40%;
        color: #ffffff;
        padding: 0.5em;
        background-color: #AA1418;;
        border-radius: 10px;
        font-size: 20px;
    }
</style>