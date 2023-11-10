import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useGlobalStore = defineStore('globalStore', {
  state: () => ({
    
  }),
  getters: {
    getDataPoints() {
      return this.dataTable
    },
    getDataTasks() {
      return this.taskDirectory
    },
    getDataEmployees() {
      return this.employees
    },
    tokenLocalStorage() {
      return window.localStorage.getItem('token', JSON.stringify())
    },
    roleLocalStorage() {
      return window.localStorage.getItem('role', JSON.stringify())
    }
  },
  actions: {
    setActiveTab(id) {
      this.activeTab = id
    },
  }
});
