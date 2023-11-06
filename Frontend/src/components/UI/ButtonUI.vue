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
        border: 0.15em solid #ffffff;
        background-color: #DA5155;
        border-radius: 10px;
        font-size: 24px;
    }
</style>