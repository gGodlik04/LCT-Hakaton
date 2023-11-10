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
    <div class="table-tasks">
        <table>
            <thead>
                <th>Тип</th>
                <th>Название задачи</th>
                <th>Приоритет</th>
                <th>Время выполнения</th>
                <th>Условие назначения</th>
                <th>Требуемый уровень сотрудника</th>
            </thead>
            <tbody>
                <tr v-for="(taskType) in dataTable" :key="taskType.type">
                    <td v-for="(value) in taskType" :key="type">
                        {{ value }}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
    .table-tasks {
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
    }
</style>