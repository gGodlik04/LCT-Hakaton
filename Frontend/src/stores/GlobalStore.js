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
  },
  actions: {
    toggleNavbar() {
      this.flagNavbar = !this.flagNavbar
    },
    toggleLoading(flag) {
      this.loading = flag
    },
  }
});
