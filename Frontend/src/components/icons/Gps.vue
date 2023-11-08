<template>
   <div  v-if="theme == 'theme-dark'" class="icon-gps">
      <svg width="21" height="26" viewBox="0 0 21 26" fill="none" xmlns="http://www.w3.org/2000/svg">
         <path d="M10.2222 24C14.5 19.6 18.7778 15.66 18.7778 10.8C18.7778 5.93989 14.9474 2 10.2222 2C5.49714 2 1.66669 5.93989 1.66669 10.8C1.66669 15.66 5.94446 19.6 10.2222 24Z" stroke="white" stroke-linecap="round" stroke-linejoin="round"/>
         <path d="M10.2222 13C11.5723 13 12.6667 11.9056 12.6667 10.5555C12.6667 9.2055 11.5723 8.11108 10.2222 8.11108C8.87215 8.11108 7.77777 9.2055 7.77777 10.5555C7.77777 11.9056 8.87215 13 10.2222 13Z" stroke="white" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
   </div>
   <div v-else class="icon-gps">
      <svg width="21" height="26" viewBox="0 0 21 26" fill="none" xmlns="http://www.w3.org/2000/svg">
         <path d="M10.2222 24C14.5 19.6 18.7778 15.66 18.7778 10.8C18.7778 5.93989 14.9474 2 10.2222 2C5.49714 2 1.66669 5.93989 1.66669 10.8C1.66669 15.66 5.94446 19.6 10.2222 24Z" stroke="black" stroke-linecap="round" stroke-linejoin="round"/>
         <path d="M10.2222 13C11.5723 13 12.6667 11.9056 12.6667 10.5555C12.6667 9.2055 11.5723 8.11108 10.2222 8.11108C8.87215 8.11108 7.77777 9.2055 7.77777 10.5555C7.77777 11.9056 8.87215 13 10.2222 13Z" stroke="black" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
   </div>
</template>

<script setup>
    const props= defineProps({
        theme:{
            type:String,
            required:true,
            default:'theme-dark'
        }
    })
</script>