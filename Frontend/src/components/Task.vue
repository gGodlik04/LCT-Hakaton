<script setup>
import Priority from '@/components/Priority.vue';
import StatusButton from '@/components/StatusButton.vue';
import { useGlobalStore } from '../stores/GlobalStore';

    const props = defineProps({
        task: {
            type: Object,
            required: true,
            default: () => {}
        },
    })

    const globalStore = useGlobalStore();

    const openPopupInfo = () => {
        
    }
</script>

<template>
    <div class="task">
        <div class="task__title">
            <Priority
                :priority="task.priority"
            />
            <div class="task__title_name">
                {{ task.task_type.name }}
            </div>
        </div>
        <div class="task__address">
            Адрес: {{ task.agent_point.address }}
        </div>
        <div class="task__time">
            Время выполнения: {{ task.task_type.work_time }} час
        </div>
        <div class="task__status">
           Cтатус: <StatusButton
            class="taks__status_btn"
            :status="task.status"
           />
        </div>
        <div class="task__date">
            {{ task.appointment_date}}
        </div>
        <ButtonUI @click="openPopupInfo" class="task__button">Начать</ButtonUI>
    </div>
</template>

<style scoped lang="scss">
    .task {
        height: fit-content;
        width: 22em;
        min-height: 19em;
        color: var(--font-color);
        padding: 26px 30px;
        border-radius: 20px;
        background: var(--color-accent);
        backdrop-filter: blur(2px);
        font-size: 18px;
        font-family: 'MontseratReg';
        display: flex;
        flex-direction: column;
    }

    .task__date {
        margin-bottom: 0px !important;
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

    @media (max-width: $screen-lg) {
        .task {
            font-size: 15px;
            height: fit-content;
            min-height: 14em;
            width: 20em;
        }
    }

    @media (max-width: $screen-md) {
        .task {
            height: fit-content;
            min-height: 19em;
            width: 16em;
        }
    }

    @media (max-width: $screen-sm) {
        .task {
            height: fit-content;
            min-height: 19em;
            width: 16em;
        }
    }
</style>