<script setup>
import Priority from '@/components/Priority.vue';
import StatusButton from '@/components/StatusButton.vue';

    const props = defineProps({
        task: {
            type: Object,
            required: true,
            default: () => {}
        },
    })
</script>

<template>
    <div class="task">
        <div class="task__title">
            <Priority
                :priority="task.priority"
            />
            <div class="task__title_name">
                {{ task.name }}
            </div>
        </div>
        <div class="task__address">
            Адрес: {{ task.address }}
        </div>
        <div class="task__time">
            Время выполнения: {{ task.time }} час
        </div>
        <div class="task__status">
           Cтатус: <StatusButton
            class="taks__status_btn"
            :status="task.status"
           />
        </div>
        <div class="task__date">
            {{ task.date_of_pont }}
        </div>
        <ButtonUI class="task__button">Начать</ButtonUI>
    </div>
</template>

<style scoped>
    .task {
        border: 1px solid #fff;
        height: 18em;
        width: 23em;
        color: #FFFFFF;
        padding: 26px 30px;
        border-radius: 20px;
        border: 3px solid #646464;
        background: rgba(0, 9, 31, 0.8);
        backdrop-filter: blur(2px);
        font-size: 18px;
        display: flex;
        flex-direction: column;
    }

    .task__title {
        display: flex;
        gap: 15px;
        margin-bottom: 30px;
    }

    .task__status {
        display: flex;
        margin-bottom: 30px;
        font-family: 'MontseratReg';
    }

    .task__address {
        margin-bottom: 30px;
        font-weight: 100;
        font-family: 'MontseratReg';
    }

    .task__time {
        margin-bottom: 30px;
        font-family: 'MontseratReg';
    }

    .task__date {
        margin-bottom: 30px;
        font-family: 'MontseratReg';
    }

    .task__button {
        height: 25px;
        width: fit-content;
        min-width: 0;
        font-size: 20px;
        padding: 6px 20px;
        margin: auto;
    }

    .taks__status_btn {
        margin-left: 15px;
        font-family: 'Montserat';
    }
</style>