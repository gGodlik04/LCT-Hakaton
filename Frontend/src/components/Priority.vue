<script setup>
    const props = defineProps ({
        priority: {
            type: Number,
            required: true,
            default: () => {},
        }
    })
</script>

<template>
    <div v-if="priority == 1" class="priority-icon">
        <HighPriority/>
    </div>
    <div v-if="priority == 2" class="priority-icon">
        <MediumPriority/>
    </div>
    <div v-if="priority == 3" class="priority-icon">
        <LowPriority/>
    </div>
</template>