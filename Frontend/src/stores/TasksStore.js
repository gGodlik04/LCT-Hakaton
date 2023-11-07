import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useTasksStore = defineStore('tasksStore', {
  state: () => ({
    tasks: [
      {
        name: 'Обучений агента',
        address: 'ул. Ставропольская, д. 140',
        time: 4,
        priority: 1,
        date_of_pont: '05.11.2023',
        status: 1,
        about: 'Более подробная информация',
      },
      {
        name: 'Стимулирование работы',
        address: 'ул. им. Максима Горького, д. 128',
        time: 2,
        priority: 2,
        date_of_pont: '10.11.2023',
        status: 2,
        about: 'Более подробная информация22222',
      },
      {
        name: 'Доставка карт и материалов',
        address: 'ул. им. Петрова, д. 321',
        time: 1,
        priority: 3,
        date_of_pont: '11.12.2023',
        status: 3,
        about: 'Более подробная информация3333',
      },
      {
        name: 'Обучений агента',
        address: 'ул. Ставропольская, д. 140',
        time: 4,
        priority: 1,
        date_of_pont: '05.11.2023',
        status: 4,
        about: 'Более подробная информация',
      },
      {
        name: 'Стимулирование работы',
        address: 'ул. им. Максима Горького, д. 128',
        time: 2,
        priority: 2,
        date_of_pont: '10.11.2023',
        status: 2,
        about: 'Более подробная информация22222',
      },
      {
        name: 'Доставка карт и материалов',
        address: 'ул. им. Петрова, д. 321',
        time: 1,
        priority: 3,
        date_of_pont: '11.12.2023',
        status: 3,
        about: 'Более подробная информация3333',
      },
    ],
    activeTab: 1,
  }),
  getters: {
    currentTasks() {
      return this.tasks.filter(el => el.status != 4)
    },
    weekTasks() {
      return this.tasks.filter(el => el.status != 4)
    },
    completedTasks() {
      return this.tasks.filter(el => el.status == 4)
    },
    favoritesTasks() {
      return this.tasks.filter(el => el.status != 4)
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
    async login(email, password) {
      const resToken = await axios.post('/api/accounts/auth/token/login/', {
        password: `${password}`,
        email: `${email}`
      }).then((response) => {
        window.localStorage.setItem('token', response.data.auth_token)
      }).then(async () => {
        const resRole = await axios.get('/api/accounts/users/me/', {
          headers: {
            Authorization: `Token ${this.tokenLocalStorage}`
          }
        }).then((response) => {
          window.localStorage.setItem('role', response.data.role)
        })
      })
    }
  }
});
