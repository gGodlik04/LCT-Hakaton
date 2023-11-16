<script setup>
import Priority from '@/components/Priority.vue';
import StatusButton from '@/components/StatusButton.vue';
import { useGlobalStore } from '../stores/GlobalStore';
import InfoTask from '@/components/InfoTask.vue';
import ModalUI from '@/components/UI/ModalUI.vue';
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { useTasksStore } from '@/stores/TasksStore';


const tasksStore = useTasksStore()


const props = defineProps({
    task: {
        type: Object,
        required: true,
        default: () => { }
    },
})

const status = ref(props.task.status)

const globalStore = useGlobalStore();
const modalVisible = ref(false);

const isTaskCompleted = ref(false)

const getStatus = computed(() => {
    switch (status.value) {
        case 1: {
            return 'Начать'
        }
        case 2: {
            return 'В пути'
        }
        case 3: {
            return 'В работе'
        }
        case 4: {
            isTaskCompleted.value = true;
            return 'Завершена'
        }
    }
})

const changeStatus = async () => {
    try {
        // if (status.value != 4) {
        // const res = await axios({
        // method: 'put',
        // url: `/api/task/task/${props.task.uuid}}/status/`,
        // data: {
        //     status: status.value + 1
        // },
        // headers: {
        //     Authorization: tasksStore.tokenLocalStorage
        // }
        // }).then((response) => {
        //     if (response.status == 200) {
        //         status.value = status.value + 1
        //     } 
        // })
        //}
        status.value = status.value + 1
        tasksStore.changeStatusTask(props.task.uuid)
    } catch (error) {

    }
}

const fetchData = (event) => {
    modalVisible.value = event
}

const test = () => {
    console.log('test');
}

</script>

<template>
    <!-- <ModalUI :show="modalVisible" class="modal-window-task" @visibleModal="fetchData($event)">
      <InfoTask
        task:task
      />
    </ModalUI> -->
    <div class="task">
        <div class="task__title">
            <Priority :priority="task.priority" />
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
            Cтатус:
            <StatusButton class="taks__status_btn" :status="status" />
        </div>
        <div class="task__date">
            {{ task.appointment_date }}
        </div>
        <ButtonUI 
            @click="changeStatus" class="task__button"
            v-bind:disabled="isTaskCompleted"
        >
                {{ getStatus }}
        </ButtonUI>
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

.task__button[disabled="true"] {
    pointer-events: none;
    background-color: #000;
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