import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useTasksStore } from './TasksStore';
import { useGlobalStore } from './GlobalStore';

export const useManagerStore = defineStore('managerStore', {
  state: () => ({
    employees: [],
    points: [],
    activeTab: 1,
  }),
  getters: {
    allPoints() {
      return this.points
    },
    getDataEmployees() {
      return this.employees
    },
    tokenLocalStorage() {
      return window.localStorage.getItem('token', JSON.stringify())
    },
    roleLocalStorage() {
      return window.localStorage.getItem('role', JSON.stringify())
    },
  },
  actions: {
    setActiveTab(id) {
      this.activeTab = id
    },

    async getAllPoints(page, limit) {
      try {
        const globalStore = useGlobalStore()
        const tasksStore = useTasksStore()
        globalStore.toggleLoading(true)
        const resPoints = await axios.get(`/api/directories/agent_points/?${page}`, {
          headers: {
            Authorization: tasksStore.tokenLocalStorage
          }
        })
        this.points = resPoints.data.results
        globalStore.toggleLoading(false)
      } catch (error) {
        globalStore.toggleLoading(false)
        console.log(error);
      }
    },

    async fetchAllEmployees() {
      const globalStore = useGlobalStore()
      const tasksStore = useTasksStore()
      try {
        const resEmployees = await axios.get('/api/accounts/users/', {
          headers: {
            Authorization: tasksStore.tokenLocalStorage
          }
        })
        this.employees = resEmployees.results
        globalStore.toggleLoading(false)
      } catch (error) {
        globalStore.toggleLoading(false)
        console.log(error);
      }
    }
  }
});
