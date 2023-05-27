import { createStore } from 'vuex'

const store = createStore({
    state () {
        return {
            auth: {
                token: null,
                refresh_token: null,
                expiry: null,
            },
            mails: [],
            focus_mail_id: null
        }
    },
    mutations: {
        setAuth (state, auth) {
            state.auth.token = auth.access_token
            state.auth.refresh_token = auth.refresh_token
            state.auth.expiry = auth.expiry_date
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