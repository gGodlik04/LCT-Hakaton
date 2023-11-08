<script setup>
    const props = defineProps({
        dataTable: {
            type: Object,
            required: true,
            default: () => {}
        }
    })

</script>

<template>
    <div class="table-points">
        <table>
            <thead>
                <th>№ точки</th>
                <th>Адрес точки</th>
                <th>Когда подключена точка?</th>
                <th>Карты и материалы доставлены?</th>
                <th>Кол-во дней после выдачи последней карты</th>
                <th>Кол-во одобренных заявок</th>
                <th>Кол-во выданных карт</th>
            </thead>
            <tbody>
                <tr v-for="(point) in dataTable" :key="point.id_point">
                    <td v-for="(value) in point" :key="id_point">
                        {{ value }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
    .table-points {
        font-size: 14px;
        border: 1px solid #fff;
        height: 100%;
        font-family: 'MontseratReg';
        color: #FFFFFF;
        background: rgba(0, 9, 31, 0.8);
        backdrop-filter: blur(2px);
        margin-top: 24px;
        margin-right: 37px;
    }

    th,td {
        padding: 20px;
        height: 20px;
        text-align: center;
    }
</style>