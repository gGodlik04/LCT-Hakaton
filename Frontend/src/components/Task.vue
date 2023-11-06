<script setup>
    const props = defineProps({
        task: {
            type: Object,
            required: true,
            default: () => {}
        }
    })
</script>

<template>
    <div class="task">
        <div class="task__priority">
            {{ task.priority }}
        </div>
        <div class="task__name">
            {{ task.name }}
        </div>
        <div class="task__address">
            {{ task.address }}
        </div>
        <div class="task__time">
            {{ task.time }}
        </div>
        <div class="task_status">
            {{ task.status }}
        </div>
        <div class="task__date">
            {{ task.date_of_pont }}
        </div>
        <ButtonUI>Начать</ButtonUI>
    </div>
</template>

<style scoped>

</style>