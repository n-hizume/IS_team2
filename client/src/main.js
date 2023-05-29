import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import store from './store'
import './assets/tailwind.css'
import vue3GoogleLogin from 'vue3-google-login'

import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)

app.use(router)
app.use(pinia)
app.use(store)
app.use(ElementPlus)

const options = {
  clientId: '290280505278-jr662shaa29lke42ckon55fumjp8dn4b.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'slelect_account'
}

app.use(vue3GoogleLogin, options)

app.mount('#app')
