import { createStore } from 'vuex'
import { formatDate } from '@/utils/index.js'

const store = createStore({
    state: {
        auth: {
            token: "init",
            refresh_token: "init",
            expiry: "init"
        },
        mails: []
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
        setExpiry (state, { threadId, expiry }) {
            for (let mail of state.mails) {
                if (mail.threadId === threadId) {
                    mail.expiry = formatDate(expiry)
                }
            }
        }
    },
    actions: {
        setAuth: function(ctx, auth) {
            ctx.commit('setAuth', auth)
        },
        setMails: function(ctx, mails) {
            ctx.commit('setMails', mails)
        }
    },
    getters: {
        getMailById: (state) => (id) => {
            return state.mails.find(mail => mail.id === id)
        },
        getAuth: (state) => () => {
            return state.auth
        }
    }
})

export default store