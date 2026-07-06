import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { VueQueryPlugin } from '@tanstack/vue-query'
import { test_env } from './common/test_env.ts'
import { createPinia } from 'pinia'
import { useAuthStore } from './common/auth.ts'


const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)
app.use(VueQueryPlugin)

//load our auth right at the start in case there's a valid token in localstorage 
useAuthStore().init()

app.mount('#app')

//optional - just printing some environment variables as a test
test_env()