import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useGlobalStore = defineStore('globalStore', {
  state: () => ({
    flagNavbar: false,
    loading: false,
    token: '',
    role: 0,
  }),
  getters: {
    getFlagNavbar() {
      return this.flagNavbar
    },
    isLoading() {
      return this.loading
    },
    getRole() {
      return this.role
    },
    getToken() {
      return this.token
    }
  },
  actions: {
    toggleNavbar() {
      this.flagNavbar = !this.flagNavbar
    },
    toggleLoading() {
      this.loading = !this.loading
    },
    setRole(role) {
      this.role = role
    },
    setToken(token) {
      this.token = token
    }
  }
});
