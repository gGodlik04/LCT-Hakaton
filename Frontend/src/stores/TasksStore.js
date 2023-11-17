import { ref, computed, toRaw } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useGlobalStore } from '@/stores/GlobalStore';
import router from '@/router';


export const useTasksStore = defineStore('tasksStore', {
  state: () => ({
    tasks: [],
    employeeInfo:[],
    activeTab: 1,
  }),
  getters: {
    currentTasks() {
      return this.tasks.filter(el => el.favorites != 4)
    },
    weekTasks() {
      return this.tasks.filter(el => el.status != 4)
    },
    completedTasks() {
      return this.tasks.filter(el => el.status == 4)
    },
    favoritesTasks() {
        const rawTasks = toRaw(this.tasks)
        const filteredTasks = rawTasks.filter(el => el.favorite == true)
        return new Proxy(filteredTasks, {})
    },
    getAllTasks() {
      return this.tasks
    },
    tokenLocalStorage() {
      return window.localStorage.getItem('token', JSON.stringify())
    },
    roleLocalStorage() {
      return window.localStorage.getItem('role', JSON.stringify())
    },
    getEmployeeInfo() {
      return JSON.parse(window.localStorage.getItem("employeeInfo"))
    }
  },
  actions: {
    setActiveTab(id) {
      this.activeTab = id
    },
    
    changeStatusTask(uuid) {
        this.tasks.find(el => el.uuid == uuid).status++;       
        console.log(this.tasks);
    },

    async login(email, password) {
      try {
        const globalStore = useGlobalStore();
        globalStore.toggleLoading(true)
        const resToken = await axios.post('/api/accounts/auth/token/login/', {
          password: `${password}`,
          email: `${email}`
        })
        await window.localStorage.setItem('token', `Token ${resToken.data.auth_token}`)
        const resRole = await axios.get('/api/accounts/users/me/', {
          headers: {
            Authorization: `Token ${resToken.data.auth_token}`
          }
        })
        await window.localStorage.setItem('role', resRole.data.role)
        localStorage.setItem("employeeInfo",JSON.stringify(resRole.data));
        location.reload()
        globalStore.toggleLoading(false)
      } catch (error) {
        console.log(error);
        globalStore.toggleLoading(false)
      }
    },

    async fetchTasks() {
      try {
        const globalStore = useGlobalStore();
        globalStore.toggleLoading(true)
        const resTasks = await axios.get('/api/task/task/', {
          headers: {
            Authorization: this.tokenLocalStorage
          }
        })
        this.tasks = resTasks.data;
        globalStore.toggleLoading(false)    
      } catch (error) {
        globalStore.toggleLoading(false)    
        console.log(error);
      }
    }
  }
});
