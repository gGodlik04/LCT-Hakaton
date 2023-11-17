import '@/assets/css/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import components from '@/components/UI'
import icons from '@/components/icons'
import VueApexCharts from "vue3-apexcharts"
import YmapPlugin from 'vue-yandex-maps'


import App from './App.vue'
import router from './router'

const settingsYMaps = {
    apiKey: 'ac1f444f-d60e-4e4b-ace7-e440a18fa420',
    lang: 'ru_RU',
    coordorder: 'latlong',
    enterprise: false,
    version: '2.1'
}

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
});

icons.forEach(icon => {
    app.component(icon.name, icon)
});

app.use(createPinia())
app.use(router)
app.use(VueApexCharts)
app.use(YmapPlugin, settingsYMaps)

app.mount('#app')
