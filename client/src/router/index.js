import { createRouter, createWebHistory } from 'vue-router'

import MailDetail from '../components/MailDetail.vue'
import EmailView from '../views/EmailView.vue'
import EmailWriteView from '../views/EmailWriteView.vue'
import AlarmView from '../views/AlarmView.vue'
import AlarmWriteView from '../views/AlarmWriteView.vue'
import SendView from '../views/SendView.vue'
import LoginView from '../views/LoginView.vue'
// import PageNotFound from '../views/PageNotFound.vue'


const routes = [
  {
    path: '/',
    component: LoginView
  },
  {
    path: '/email',
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
    path: '/write',
    component: EmailWriteView
  },
  {
    path: '/alarm',
    component: AlarmView,
    children: [
      {
        path: 'maildetail',
        
        component: MailDetail
      }
      
    ]
  },
  {
    path: '/alarm.write',
    component: AlarmWriteView
  },
  {
    path: '/send',
    component: SendView
  },
 
  
  // ,
  // { 
  //   path: '*', 
  //   component: PageNotFound
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
