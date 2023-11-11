<script setup>
import {ref} from 'vue'

const address = ref()
const dateOfConnect = ref()
const dateFromDelivery = ref()
const delivery = ref()
const approved = ref()
const cardIssue = ref()



const addPointFormSubmit = (form) => {
    
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
            <div class="form__add-point-input-title">Когда подключена точка?
                <input 
                type="text" 
                class="form__add-point-input form__add-point-dateOfConnect" 
                v-model="dateOfConnect" 
                autofocus 
                placeholder="Введите адрес" 
                >
            </div>
                <div class="form__add-point-input-title">Карты и материалы доставлены?
                <input 
                type="text" 
                class="form__add-point-input form__add-point-dateFromDelivery" 
                v-model="dateFromDelivery" 
                autofocus 
                placeholder="Введите адрес" 
                >
            </div>
                <div class="form__add-point-input-title">Кол-во дней после выдачи последней карты
                <input 
                type="text" 
                class="form__add-point-input form__add-point-delivery" 
                v-model="delivery" 
                autofocus 
                placeholder="Введите адрес" 
                >
            </div>
            <div class="form__add-point-input-title">Кол-во одобренных заявок
                <input 
                type="text" 
                class="form__add-point-input form__add-point-approved" 
                v-model="approved" 
                autofocus 
                placeholder="Введите адрес" 
                >
            </div>
            <div class="form__add-point-input-title">Кол-во выданных карт
                <input 
                type="text" 
                class="form__add-point-input form__add-point-cardIssue" 
                v-model="cardIssue" 
                autofocus 
                placeholder="Введите адрес" 
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