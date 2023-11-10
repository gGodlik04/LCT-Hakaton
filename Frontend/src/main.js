import '@/assets/css/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import components from '@/components/UI'
import icons from '@/components/icons'
import VueApexCharts from "vue3-apexcharts";

import App from './App.vue'
import router from './router'

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

app.mount('#app')
