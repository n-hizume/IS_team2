import { createStore } from 'vuex'

const store = createStore({
    state () {
        return {
            auth: {
                access_token: null,
                refresh_token: null,
                expiry_date: null,
            },
            focus_mail: null
        }
    },
    mutations: {
        setAuth (state, auth) {
            state.auth = auth
        },
        setFocusMail (state, mail) {
            state.focus_mail = mail
        }
    }
})

export default store