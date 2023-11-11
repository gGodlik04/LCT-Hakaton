<script setup>
import { onMounted, ref, toRaw } from 'vue';
import { useManagerStore } from '@/stores/ManagerStore';

const managerStore = useManagerStore()

const dataTable = ref()

onMounted(() => {
    managerStore.getAllPoints(1,2)
    dataTable.value = managerStore.allPoints
})

</script>

<template>
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

    th,td {
        padding: 20px;
        height: 20px;
        text-align: center;
        min-width: 100px;
    }

    table {
        // table-layout: fixed;
        // width: 100%;
        border-collapse: collapse;
        overflow: auto;
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