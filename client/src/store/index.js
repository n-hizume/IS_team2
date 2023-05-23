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
            state.auth = auth
        },
        setMails (state, mails) {
            state.mails = mails
        },
        setFocusMailId (state, id) {
            state.focus_mail_id = id
        }
    }
})

export default store