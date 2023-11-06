<template>
    <div class="status-btn">
        {{ status }}
        <slot></slot>
    </div>
</template>
<script setup>
    const props = defineProps ({
        status: {
            type: String,
            required: true,
            default: () => {}
        }
    })

</script>
<style>
    .status-btn {
        color: #00091F;
        font-size: 14px;
        font-weight: 500;
        width: fit-content;
        padding: 2px 8px;
        text-align: center;
        border-radius: 10px;
        background-color: #FFFFFF;
    }
</style>