import { createRouter, createWebHistory } from 'vue-router'
import MainWorker from '@/pages/MainWorker.vue'
import MainManager from '@/pages/MainManager.vue'
import Login from '@/pages/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'mainWorker',
      component: MainWorker
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/map',
      name: 'map',
      // component: Login
    },
    {
      path: '/manager',
      name: 'MainManager',
      // component: Login
    },
  ]
})


export default router
