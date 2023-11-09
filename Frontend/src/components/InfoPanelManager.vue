<script setup>

const series = [44, 55, 13, 43, 22]
          const chartOptions = {
            chart: {
              width: 380,
              type: 'pie',
            },
            labels: ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
            responsive: [{
              breakpoint: 480,
              options: {
                chart: {
                  width: 200
                },
                legend: {
                  position: 'bottom'
                }
              }
            }]
          }
</script>

<template>
    <div class="chart">
        <apexchart type="pie" width="380" :options="chartOptions" :series="series"></apexchart>
    </div>
</template>

<style scoped lang="scss">
    @media (max-width: $screen-small) {
        .chart {
            display: none;
        }
    }
</style>