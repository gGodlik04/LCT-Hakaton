<script setup>

function generateData(count, yrange) {
var i = 0;
var series = [];
while (i < count) {
  var x = (i + 1).toString();
  var y =
  Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

  series.push({
    x: x,
    y: y
  });
  i++;
}
return series;
}

const series1 = [44, 55, 13, 43, 22]
          const chartOptions1 = {
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

        const  series2 = [{
            name: 'PRODUCT A',
            data: [44, 55, 41, 67, 22, 43, 21, 49]
          }, {
            name: 'PRODUCT B',
            data: [13, 23, 20, 8, 13, 27, 33, 12]
          }, {
            name: 'PRODUCT C',
            data: [11, 17, 15, 15, 21, 14, 15, 13]
          }]
        const  chartOptions2 = {
            chart: {
              type: 'bar',
              height: 350,
              stacked: true,
              stackType: '100%'
            },
            responsive: [{
              breakpoint: 480,
              options: {
                legend: {
                  position: 'bottom',
                  offsetX: -10,
                  offsetY: 0
                }
              }
            }],
            xaxis: {
              categories: ['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2',
                '2012 Q3', '2012 Q4'
              ],
            },
            fill: {
              opacity: 1
            },
            legend: {
              position: 'right',
              offsetX: 0,
              offsetY: 50
            }
          }



        const  series3 = [
            // George Washington
            {
              name: 'George Washington',
              data: [
                {
                  x: 'President',
                  y: [
                    new Date(1789, 3, 30).getTime(),
                    new Date(1797, 2, 4).getTime()
                  ]
                },
              ]
            },
            // John Adams
            {
              name: 'John Adams',
              data: [
                {
                  x: 'President',
                  y: [
                    new Date(1797, 2, 4).getTime(),
                    new Date(1801, 2, 4).getTime()
                  ]
                },
                {
                  x: 'Vice President',
                  y: [
                    new Date(1789, 3, 21).getTime(),
                    new Date(1797, 2, 4).getTime()
                  ]
                }
              ]
            },
            // Thomas Jefferson
            {
              name: 'Thomas Jefferson',
              data: [
                {
                  x: 'President',
                  y: [
                    new Date(1801, 2, 4).getTime(),
                    new Date(1809, 2, 4).getTime()
                  ]
                },
                {
                  x: 'Vice President',
                  y: [
                    new Date(1797, 2, 4).getTime(),
                    new Date(1801, 2, 4).getTime()
                  ]
                },
                {
                  x: 'Secretary of State',
                  y: [
                    new Date(1790, 2, 22).getTime(),
                    new Date(1793, 11, 31).getTime()
                  ]
                }
              ]
            },
            // Aaron Burr
            {
              name: 'Aaron Burr',
              data: [
                {
                  x: 'Vice President',
                  y: [
                    new Date(1801, 2, 4).getTime(),
                    new Date(1805, 2, 4).getTime()
                  ]
                }
              ]
            },
            // George Clinton
            {
              name: 'George Clinton',
              data: [
                {
                  x: 'Vice President',
                  y: [
                    new Date(1805, 2, 4).getTime(),
                    new Date(1812, 3, 20).getTime()
                  ]
                }
              ]
            },
            // John Jay
            {
              name: 'John Jay',
              data: [
                {
                  x: 'Secretary of State',
                  y: [
                    new Date(1789, 8, 25).getTime(),
                    new Date(1790, 2, 22).getTime()
                  ]
                }
              ]
            },
            // Edmund Randolph
            {
              name: 'Edmund Randolph',
              data: [
                {
                  x: 'Secretary of State',
                  y: [
                    new Date(1794, 0, 2).getTime(),
                    new Date(1795, 7, 20).getTime()
                  ]
                }
              ]
            },
            // Timothy Pickering
            {
              name: 'Timothy Pickering',
              data: [
                {
                  x: 'Secretary of State',
                  y: [
                    new Date(1795, 7, 20).getTime(),
                    new Date(1800, 4, 12).getTime()
                  ]
                }
              ]
            },
            // Charles Lee
            {
              name: 'Charles Lee',
              data: [
                {
                  x: 'Secretary of State',
                  y: [
                    new Date(1800, 4, 13).getTime(),
                    new Date(1800, 5, 5).getTime()
                  ]
                }
              ]
            },
            // John Marshall
            {
              name: 'John Marshall',
              data: [
                {
                  x: 'Secretary of State',
                  y: [
                    new Date(1800, 5, 13).getTime(),
                    new Date(1801, 2, 4).getTime()
                  ]
                }
              ]
            },
            // Levi Lincoln
            {
              name: 'Levi Lincoln',
              data: [
                {
                  x: 'Secretary of State',
                  y: [
                    new Date(1801, 2, 5).getTime(),
                    new Date(1801, 4, 1).getTime()
                  ]
                }
              ]
            },
            // James Madison
            {
              name: 'James Madison',
              data: [
                {
                  x: 'Secretary of State',
                  y: [
                    new Date(1801, 4, 2).getTime(),
                    new Date(1809, 2, 3).getTime()
                  ]
                }
              ]
            },
          ]
        const  chartOptions3 =  {
            chart: {
              height: 350,
              type: 'rangeBar'
            },
            plotOptions: {
              bar: {
                horizontal: true,
                barHeight: '50%',
                rangeBarGroupRows: true
              }
            },
            colors: [
              "#008FFB", "#00E396", "#FEB019", "#FF4560", "#775DD0",
              "#3F51B5", "#546E7A", "#D4526E", "#8D5B4C", "#F86624",
              "#D7263D", "#1B998B", "#2E294E", "#F46036", "#E2C044"
            ],
            fill: {
              type: 'solid'
            },
            xaxis: {
              type: 'datetime'
            },
            legend: {
              position: 'right'
            },
            tooltip: {
              custom: function(opts) {
                const fromYear = new Date(opts.y1).getFullYear()
                const toYear = new Date(opts.y2).getFullYear()
                const values = opts.ctx.rangeBar.getTooltipValues(opts)
            
                return (
                  ''
                )
              }
            }
          }



        const  series4 = [{
            name: 'Metric1',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          },
          {
            name: 'Metric2',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          },
          {
            name: 'Metric3',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          },
          {
            name: 'Metric4',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          },
          {
            name: 'Metric5',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          },
          {
            name: 'Metric6',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          },
          {
            name: 'Metric7',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          },
          {
            name: 'Metric8',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          },
          {
            name: 'Metric9',
            data: generateData(18, {
              min: 0,
              max: 90
            })
          }
          ]
        const  chartOptions4= {
            chart: {
              height: 350,
              type: 'heatmap',
            },
            dataLabels: {
              enabled: false
            },
            colors: ["#008FFB"],
            title: {
              text: 'HeatMap Chart (Single color)'
            }
          }
</script>

<template>
    <div class="chart">
        <apexchart class="chart__pie" type="pie" width="380" :options="chartOptions1" :series="series1"></apexchart>
        <apexchart class="chart__tooltip" type="rangeBar" height="350" :options="chartOptions3" :series="series3"></apexchart>
      </div>
      <apexchart type="bar" height="350" :options="chartOptions2" :series="series2"></apexchart>
      <apexchart type="heatmap" height="350" :options="chartOptions4" :series="series4"></apexchart>
</template>

<style scoped lang="scss">

.chart {
  display: flex;
}

.chart__pie {
  position: relative;
  top: 70px;
}

.chart__tooltip {
  width: 100%;
}
    @media (max-width: $screen-small) {
        .chart {
            // display: none;
        }
    }
</style>