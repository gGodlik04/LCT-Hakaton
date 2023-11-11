<script setup>
import {onMounted, ref, onBeforeMount} from 'vue'
import { useManagerStore} from '../stores/ManagerStore';


    const props = defineProps({
        dataTable: {
            type: Object,
            required: true,
            default: () => {}
        }
    })
const managerStore = useManagerStore()
const dataTable = ref()

onBeforeMount(() => {
    managerStore.fetchAllEmployees()
    dataTable.value = managerStore.getDataEmployees;
    console.log(dataTable.value);
})

</script>

<template>
    <div class="table-employees">
        <table>
            <thead>
                <th>ФИО</th>
                <th>Адрес локации</th>
                <th>Email</th>
                <th>Грейд</th>
            </thead>
            <tbody>
                <tr v-for="(employee) in dataTable" :key="employee.uuid">
                    <td :key="employee.uuid">
                        {{ employee.first_name }} {{ employee.last_name }} {{ employee.middle_name }}
                    </td>
                    <td :key="employee.uuid">
                        {{ employee.address }}
                    </td>
                    <td :key="employee.uuid">
                        {{ employee.email }}
                    </td>
                    <td :key="employee.uuid">
                        {{ employee.grade }}
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
        color: var(--font-color);
        background: var(--color-accent);
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