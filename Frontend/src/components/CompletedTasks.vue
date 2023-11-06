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
    <template v-for="(task) in tasks">
        <Task v-if="task.status == 4" 
            :key="task.address"
            :task="task"
        />
    </template>
</template>

<style scoped>

</style>