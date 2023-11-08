<script setup>
import Priority from '@/components/Priority.vue';
import StatusButton from '@/components/StatusButton.vue';

const props = defineProps({
    task: {
        type: Object,
        required: true,
        default: () => { }
    }
})
</script>

<template>
    <div class="modal" @click="hideModal" v-if="show === true">
        <div @click.stop class="modal__content-dialog">
            <div class="task">
                <div class="task__title">
                    <Priority :priority="task.priority" />
                    <div class="task__title_name">
                        {{ task.name }}
                    </div>
                </div>
                <div class="task__address-start">
                    Адрес: {{ task.address_start }}
                </div>
                <div class="task__address-end">
                    Адрес: {{ task.address }}
                </div>
                <div class="task__time">
                    Время выполнения: {{ task.time }} час
                </div>
                <div class="task__status">
                    Cтатус:
                    <StatusButton class="taks__status_btn" :status="task.status" />
                </div>
                <div class="task__date">
                    {{ task.date_of_pont }}
                </div>
                <ButtonUI @click="openPopupInfo" class="task__button">Начать</ButtonUI>
                <div class="map">
                </div>
            </div>
        </div>
    </div>
</template>

<style>

</style>