<script setup>
import {ref} from 'vue'
import axios from 'axios'
import { useTasksStore } from '../stores/TasksStore';

const address = ref()
const dateOfConnect = ref()
const dateFromDelivery = ref()
const delivery = ref()
const approved = ref()
const cardIssue = ref()

const tasksStore = useTasksStore()

const addPointFormSubmit = async (form) => {
    const res =  await axios.post('/api/directories/agent_points/',{
        address: address.value,
        agent_point_date: dateOfConnect.value,
        materials: dateFromDelivery.value ,
        last_card_given: delivery.value,
        approved_requests: approved.value,
        num_given_cards: Number(cardIssue.value)
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
    <div class="form__add-point">
        <div class="form__add-point-title">Добавить агентскую точку</div>

            <form>
                <div class="form__add-point-input-title">Адрес точки:
                    <input 
                    type="text" 
                    class="form__add-point-input form__add-point-address" 
                    v-model="address" 
                    autofocus 
                    placeholder="Введите адрес" 
                    >
                </div>
            <div class="form__add-point-input-title">Когда подключена точка? (вчера/давно)
                <input 
                type="text" 
                class="form__add-point-input form__add-point-dateOfConnect" 
                v-model="dateOfConnect" 
                autofocus 
                placeholder="Укажите значение" 
                >
            </div>
                <div class="form__add-point-input-title">Карты и материалы доставлены? (1/0)
                <input 
                type="text" 
                class="form__add-point-input form__add-point-dateFromDelivery" 
                v-model="dateFromDelivery" 
                autofocus 
                placeholder="Укажите значение" 
                >
            </div>
                <div class="form__add-point-input-title">Кол-во дней после выдачи последней карты (YYYY-MM-DD)
                <input 
                type="text" 
                class="form__add-point-input form__add-point-delivery" 
                v-model="delivery" 
                autofocus 
                placeholder="Укажите значение" 
                >
            </div>
            <div class="form__add-point-input-title">Кол-во одобренных заявок
                <input 
                type="text" 
                class="form__add-point-input form__add-point-approved" 
                v-model="approved" 
                autofocus 
                placeholder="Укажите значение" 
                >
            </div>
            <div class="form__add-point-input-title">Кол-во выданных карт
                <input 
                type="text" 
                class="form__add-point-input form__add-point-cardIssue" 
                v-model="cardIssue" 
                autofocus 
                placeholder="Укажите значение" 
                >
            </div>
            <ButtonUI @click="addPointFormSubmit" class="form__add-point_submit-buttonUI">Добавить</ButtonUI>
        </form>
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