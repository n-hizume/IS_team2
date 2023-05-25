import { createStore } from 'vuex'

const store = createStore({
    state () {
        return {
            auth: {
                access_token: null,
                refresh_token: null,
                expiry_date: null,
            },
            mails: [],
            focus_mail_id: null
        }
    },
    mutations: {
        setAuth (state, auth) {
            state.auth.access_token = auth.access_token
            state.auth.refresh_token = auth.refresh_token
            state.auth.expiry_date = auth.expiry_date
        },
        setMails (state, mails) {
            state.mails = mails
        },
        setFocusMailId (state, id) {
            state.focus_mail_id = id
        }
    },
    getters: {
        getMailById: (state) => (id) => {
            return state.mails.find(mail => mail.id === id)
        },
    }
})

export default store