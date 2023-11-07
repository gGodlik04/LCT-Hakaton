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

router.beforeEach((to, from, next) => {
  const tasksStore = useTasksStore();

  if (tasksStore.tokenLocalStorage && (tasksStore.roleLocalStorage == 2)) {
    next('/')
  }

  // if (tasksStore.tokenLocalStorage && (tasksStore.roleLocalStorage == 1)) {
  //   next({ name: 'MainManager' })
  // }
})

export default router
