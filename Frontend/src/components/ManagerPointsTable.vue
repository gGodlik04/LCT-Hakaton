<script setup>
import { onMounted, ref, toRaw } from 'vue';
import { useManagerStore } from '@/stores/ManagerStore';
import FormEditPoint from '@/components/FormEditPoint.vue'
import ModalUI from '@/components/UI/ModalUI.vue';


const managerStore = useManagerStore()

const dataTable = ref()

onMounted(async () => {
    await managerStore.getAllPoints(1,2)
    dataTable.value = managerStore.allPoints
})

const fetchData = (event) => {
    modalVisible.value = event
}

const modalVisible = ref(false);

</script>

<template>
<ModalUI :show="modalVisible" class="modal-window-points" @visibleModal="fetchData($event)">
    <FormEditPoint/>
</ModalUI>
    <div class="table-points">
        <table>
            <thead>
                <th>Адрес точки</th>
                <th>Когда подключена точка?</th>
                <th>Карты и материалы доставлены?</th>
                <th>Кол-во дней после выдачи последней карты</th>
                <th>Кол-во одобренных заявок</th>
                <th>Кол-во выданных карт</th>
            </thead>
            <tbody>
                <tr v-for="(point) in dataTable" :key="point.uuid">
                    <td :key="point.uuid">
                        {{ point.address }}
                    </td>
                    <td :key="point.uuid">
                        {{ point.agent_point_date }}
                    </td>
                    <td :key="point.uuid">
                        {{ point.materials ? 'да' : 'нет' }}
                    </td>
                    <td :key="point.uuid">
                        {{ point.last_card_given }}
                    </td>
                    <td :key="point.uuid">
                        {{ point.approved_requests }}
                    </td>
                    <td :key="point.uuid">
                        {{ point.num_given_cards }}
                    </td>
                    <td>
                        <ButtonUI 
                            @click="modalVisible=true"
                            class="edit">
                            Редактировать
                        </ButtonUI>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped lang="scss">
    .table-points {
        font-size: 14px;
        height: 100%;
        font-family: 'MontseratReg';
        color: var(--font-color);
        background: var(--color-accent);
        backdrop-filter: blur(2px);
        margin-top: 24px;
        margin-right: 37px;
    }

    .edit{
        font-size: 14px;
    }

    th,td {
        padding: 20px;
        height: 20px;
        text-align: center;
        min-width: 50px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        table-layout: fixed;
    }

    @media (max-width: $screen-md) {
        .table-points {
            overflow-y: scroll;
            margin-left: 37px;
            font-size: 10px;
        }
    }
</style>