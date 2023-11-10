<script setup>
import Task from '@/components/Task.vue'
import { onMounted } from 'vue';

const props = defineProps({
    tasks: {
        type: Object,
        required: true,
        default: () => {}
    },
    // screenWidth: {
    //     type: Number,
    //     required: true,
    //     default: 1980
    // }
})

onMounted (() => {
})

</script>

<template>
    <Task v-for="(task) in tasks"
        :key="task.address"
        :task="task"
    />
</template>

<style scoped>

</style>