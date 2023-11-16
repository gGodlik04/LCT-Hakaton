<script setup>
import {ref, onMounted} from 'vue';
import axios from 'axios';
import Priority from '@/components/Priority.vue';
import { useTasksStore } from '../stores/TasksStore';

const address = ref()
const dateOfConnect = ref()
const dateFromDelivery = ref()
const delivery = ref()
const approved = ref()
const cardIssue = ref()

const tasksStore = useTasksStore()


const props = defineProps({
    task: {
        type: Object,
        required:false,
        default: () => {}
    }
})

onMounted(() => {
    console.log(props.task);
})

const changeStatus = async (form) => {
    const res =  await axios.post('/api/directories/agent_points/',{
       
    }, 
    {
        headers:{
            Authorization: tasksStore.tokenLocalStorage
        }
    }).then((response) => {
        if (response.status == 201) {
            alert('Точка успешно добавлена')
        } else {
            alert('Вы ввели не верные данные')
        }
    })
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
        <ButtonUI class="task__button">Начать</ButtonUI>
    </div>
</template>

<style scoped lang="scss">
    .form__add-point {
        padding: 35px;
    }
    .form__add-point-title {
        font-size: 20px;
        text-align: center;
        margin-bottom: 1em;
    }
    
    .form__add-point-input-title{
        font-size: 12px;
        margin-bottom: 10px;
        border-bottom: 1px solid #fff;
        display: flex;
        flex-direction: column;
    }

    .form__add-point-input {
        font-size: 12px;
        margin-top: 10px;
        margin-bottom: 10px;
        color: var(--color-secondary);
        border: none;
        background: var(--color-primary);
    }

    input:active, :hover, :focus {
        outline: none;
    }

    .form__add-point_submit-buttonUI {
        margin: auto;
        margin-top: 32px;
        height: 20px;
        padding: 6px 20px;
        width: fit-content;
        min-width: 0;
        border-radius: 5px;
        font-size: 14px;
    }
</style>