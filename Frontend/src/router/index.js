import { createRouter, createWebHistory } from 'vue-router'
import MainWorker from '@/pages/MainWorker.vue'
import MainManager from '@/pages/MainManager.vue'
import Login from '@/pages/Login.vue'
import { useGlobalStore } from '@/stores/GlobalStore';
import { useTasksStore } from '@/stores/TasksStore';


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
      component: MainManager
    },
  ]
})

router.beforeEach( async(to, from) => {
  const globalStore = await useGlobalStore();
  const taskStore = await useTasksStore();
  if (!globalStore.getToken && to.name !== 'login') {
    return { name: 'login' }
  } else if (globalStore.getToken && globalStore.getRole == 2 && to.name !== 'mainWorker') {
    return { name: 'mainWorker' }
  } else if (globalStore.getToken && globalStore.getRole == 3 && to.name !== 'MainManager') {
    return { name: 'MainManager' }
  }
})

export default router
