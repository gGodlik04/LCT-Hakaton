<script setup>
import Task from '@/components/Task.vue'

const props = defineProps({
    tasks: {
        type: Object,
        required: true,
        default: () => {}
    }
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