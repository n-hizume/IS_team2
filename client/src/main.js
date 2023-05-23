import { createApp } from 'vue'
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
app.use(vue3GoogleLogin, {
  clientId: '290280505278-mq7jf5gn8u5e2gssj3i27bf4r10v9o9k.apps.googleusercontent.com' // EG: 184413169503-jfhjjaskdfhdsakfhjsa.apps.googleusercontent.com
})

app.mount('#app')
