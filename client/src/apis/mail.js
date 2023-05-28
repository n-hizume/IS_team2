import axios from 'axios'
import store from '@/store/index';

export const BASE_URL = 'http://kuisteam2.pythonanywhere.com'

export const getToken = async (code) => {
    const res = await axios.post(BASE_URL+'/mail/auth/', {
        "code": code,
        "redirect_url": "http://localhost:8081"
    });
    store.commit('setAuth', {
        access_token: res.data.access_token,
        refresh_token: res.data.refresh_token,
        expiry_date: res.data.expires_in,
    })
}

export const getMails = async () => {
    const auth = store.state.auth;
    const res = await axios.post(BASE_URL+'/mail/getall/', {
        "auth": {
            "token": auth.token,
            "refresh_token": auth.refresh_token,
            "expiry": auth.expiry,
        }
    })
    const mails = res.data["mails"]
    for (let mail of mails) {
        let body = mail.body;
        body = body.replace('\r\n', '<br>')
        body = body.replace('\n', '<br>')
        mail.body = body
    }

    store.commit('setMails', mails)
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

export const setExpiry = async (thread_id, expiry) => {
    const res = await axios.post(BASE_URL+'/mail/expiry/', {
        "thread_id": thread_id,
        "expiry": expiry
    })
    return res.data["result"]
}