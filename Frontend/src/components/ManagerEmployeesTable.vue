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
    <div class="table-employees">
        <table>
            <thead>
                <th>ФИО</th>
                <th>Адрес локации</th>
                <th>Грейд</th>
            </thead>
            <tbody>
                <tr v-for="(employee) in dataTable" :key="employee.full_name">
                    <td v-for="(value) in employee" :key="full_name">
                        {{ value }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
    .table-employees {
        font-size: 14px;
        height: 100%;
        font-family: 'MontseratReg';
        color: #FFFFFF;
        background: rgba(0, 9, 31, 0.8);
        backdrop-filter: blur(2px);
        margin-top: 24px;
        margin-right: 37px;
    }
    
    table {
        width: 100%;
    }

    th,td {
        max-width: 1px;
        padding: 20px;
        height: 20px;
        text-align: center;
    }
</style>