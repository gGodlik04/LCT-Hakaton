import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useManagerStore = defineStore('managerStore', {
  state: () => ({
    dataTable: [
      {
        id_point: 32146,
        address: 'ул. Ставропольская, д. 140',
        date_of_connect: 'вчера',
        materials_deliviry: false,
        last_cart_date: 0,
        amount_success: 0,
        amount_cart_gives: 0,
      },
      {
        id_point: 65423,
        address: 'ул. им. Максима Горького, д. 128',
        date_of_connect: 'давно',
        materials_deliviry: true,
        last_cart_date: 3,
        amount_success: 15,
        amount_cart_gives: 3,
      },
      {
        id_point: 56437,
        address: 'ул. им. Дзержинского, д. 100',
        date_of_connect: 'давно',
        materials_deliviry: true,
        last_cart_date: 3,
        amount_success: 9,
        amount_cart_gives: 1,
      },
      {
        id_point: 32146,
        address: 'ул. Красноармейская, д. 126',
        date_of_connect: 'вчера',
        materials_deliviry: false,
        last_cart_date: 0,
        amount_success: 0,
        amount_cart_gives: 0,
      },
      {
        id_point: 32146,
        address: 'тер. Пашковский жилой массив, ул. Крылатая, д. 2',
        date_of_connect: 'вчера',
        materials_deliviry: false,
        last_cart_date: 0,
        amount_success: 0,
        amount_cart_gives: 0,
      },
      {
        id_point: 32146,
        address: 'ул. им. Дзержинского, д. 165',
        date_of_connect: 'вчера',
        materials_deliviry: false,
        last_cart_date: 0,
        amount_success: 0,
        amount_cart_gives: 0,
      },
      {
        id_point: 32146,
        address: 'ул. Таманская, д. 153 к. 3, кв. 2',
        date_of_connect: 'вчера',
        materials_deliviry: false,
        last_cart_date: 0,
        amount_success: 0,
        amount_cart_gives: 0,
      },
      {
        id_point: 32146,
        address: 'х. Ленина, п/о. 37',
        date_of_connect: 'вчера',
        materials_deliviry: false,
        last_cart_date: 0,
        amount_success: 0,
        amount_cart_gives: 0,
      },
      {
        id_point: 32146,
        address: 'ул. Ставропольская, д. 140',
        date_of_connect: 'вчера',
        materials_deliviry: false,
        last_cart_date: 0,
        amount_success: 0,
        amount_cart_gives: 0,
      },
      {
        id_point: 32146,
        address: 'ул. Красноармейская, д. 126',
        date_of_connect: 'вчера',
        materials_deliviry: false,
        last_cart_date: 0,
        amount_success: 0,
        amount_cart_gives: 0,
      },
    ],
    taskDirectory: [
      {
        type: 1,
        name: 'Выезд на точку для стимулирования выдач',
        priority: 'Высокий',
        time_complete: '4 часа',
        assignment: 'Дата выдачи последней карты более 7 дней назад, при этом есть одобренные заявки',
        employee_grade: 'Только синьор'
      },
      {
        type: 2,
        name: 'Обучение агента',
        priority: 'Средний',
        time_complete: '2 часа',
        assignment: 'Отношение кол-ва выданных карт к одобренным заявкам менее 50%, если выдано больше 0 карт',
        employee_grade: 'Синьор или мидл'
      },
      {
        type: 3,
        name: 'Доставка карт и материалов',
        priority: 'Низкий',
        time_complete: '1,5 часа',
        assignment: 'Точка подключена вчера',
        employee_grade: 'Все уровни'
      },
    ],
    employees: [
      {
        full_name: 'Дерягин Никита Владимирович',
        addres_of_location: 'Краснодар, Красная, д. 139',
        grade: 'Синьор'
      },
      {
        full_name: 'Петрошев Валерий Павлович',
        addres_of_location: 'Краснодар, Красная, д. 139',
        grade: 'Мидл'
      },
      {
        full_name: 'Евдокимов Давид Тихонович',
        addres_of_location: 'Краснодар, Красная, д. 139',
        grade: 'Джун'
      },
      {
        full_name: 'Андреев Гордий Данилович',
        addres_of_location: 'Краснодар, В.Н. Мачуги, 41',
        grade: 'Синьор'
      },
      {
        full_name: 'Иванов Адам Федорович',
        addres_of_location: 'Краснодар, В.Н. Мачуги, 41',
        grade: 'Мидл'
      },
      {
        full_name: 'Бобылёв Ипполит Альбертович',
        addres_of_location: 'Краснодар, В.Н. Мачуги, 41',
        grade: 'Джун'
      },
      {
        full_name: 'Беляева Евгения Антоновна',
        addres_of_location: 'Краснодар, Красных Партизан, 321',
        grade: 'Мидл'
      },
      {
        full_name: 'Николаев Азарий Платонович',
        addres_of_location: 'Краснодар, Красных Партизан, 321',
        grade: 'Джун'
      },
    ],
    activeTab: 1,
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
