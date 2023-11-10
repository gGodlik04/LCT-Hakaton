import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useGlobalStore = defineStore('globalStore', {
  state: () => ({
    flagNavbar: false,
  }),
  getters: {
    getFlagNavbar() {
      return this.flagNavbar
    },
  },
  actions: {
    setFlagNavbar(flag) {
      this.flagNavbar = flag
    },
    toggleNavbar() {
      this.flagNavbar = !this.flagNavbar
    }
  }
});
