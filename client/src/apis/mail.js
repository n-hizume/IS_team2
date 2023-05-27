import axios from 'axios'
import store from '@/store/index';

const BASE_URL = 'http://kuisteam2.pythonanywhere.com'

export const getToken = (code) => {
    axios.post(BASE_URL+'/mail/auth/', {
        "code": code,
        "redirect_url": "http://localhost:8082"
    }).then((res) => {
        store.commit('setAuth', {
            access_token: res.data.access_token,
            refresh_token: res.data.refresh_token,
            expiry_date: res.data.expires_in,
        })
    })

}

export const getMails = () => {
    axios.post(BASE_URL+'/mail/getall/', {
        "auth": store.state.auth
    }).then((res) => {
        store.commit('setMails', res.data["mails"])
    })
}

export const sendMail = (to, subject, body) => {
    axios.post(BASE_URL+'/mail/send/', {
        "auth": store.state.auth,
        "mail": {
            "to": to,
            "subject": subject,
            "body": body
        }
    }).then((res) => {
        console.log(res.data)
    })
}