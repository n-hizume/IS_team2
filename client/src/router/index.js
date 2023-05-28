import { createRouter, createWebHistory } from 'vue-router'

import MailDetail from '../components/MailDetail.vue'
import EmailView from '../views/EmailView.vue'
import AlarmView from '../views/AlarmView.vue'
import LoginView from '../views/LoginView.vue'


const routes = [
  {
    path: '/',
    component: LoginView
  },
  {
    path: '/email',
    name: 'email',
    component: EmailView,
    children: [
      {
        path: 'maildetail',
        name: 'maildetail',
        component: MailDetail,
      }
     
    ]
  },
  {
    path: '/alarm',
    component: AlarmView,
    children: [
      {
        path: 'maildetail',
        name: 'maildetailforalarm',
        component: MailDetail
      }
      
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
