import { createRouter, createWebHistory } from 'vue-router'
import MainWorker from '@/pages/MainWorker.vue'
import MainManager from '@/pages/MainManager.vue'
import Login from '@/pages/Login.vue'
import { useTasksStore } from '../stores/TasksStore';


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

router.beforeEach( async(to, from) => {
  const tasksStore = await useTasksStore();
  console.log(!tasksStore.tokenLocalStorage);
  if (!tasksStore.tokenLocalStorage && to.name !== 'login') {
    return { name: 'login' }
  } else if (tasksStore.tokenLocalStorage && tasksStore.roleLocalStorage == 2 && to.name !== 'mainWorker') {
    return { name: 'mainWorker' }
  } else if (tasksStore.tokenLocalStorage && tasksStore.roleLocalStorage == 3 && to.name !== 'MainManager') {
    return { name: 'MainManager' }
  }
})

export default router
