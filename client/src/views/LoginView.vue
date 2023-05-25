<template>
    <div id="LoginView" class="grid h-screen place-items-center">
        <div>
            <div class="login-btn" @click="login">
                <img width="279" src="img/GmailLogin.png" alt="">
                <div class="flex justify-center">
                    Googleログイン
                </div>
            </div>
            <!-- <a href="" @click="useGoogleAuth" >Google でログイン</a> -->
        </div>
    </div>
</template>

<script setup>
import { googleSdkLoaded } from "vue3-google-login";
import axios from 'axios'
import { useRouter } from "vue-router";

const router = useRouter();

const getToken = async (code) => {
    axios.post('http://kuisteam2.pythonanywhere.com/mail/auth/', {
        "code": code,
        "redirect_url": "http://localhost:8082"
    }).then((res) => {
        console.log(res)
    }).catch((err) => {
        console.log(err)
    })

}

const login = () => {
    googleSdkLoaded((google) => {
        google.accounts.oauth2.initCodeClient({
            client_id: '290280505278-jr662shaa29lke42ckon55fumjp8dn4b.apps.googleusercontent.com',
            scope: 'https://www.googleapis.com/auth/gmail.modify',
            callback: (response) => {
                getToken(response.code);
                router.push('email')
            }
        }).requestCode()

    })

}



</script>

<style lang="scss">

.login-btn {
    border-radius: 10px;
    padding: 20px;
    box-shadow: 1px 1px 10px 1px #888888;
}

.login-btn:hover {
    cursor: pointer;
    box-shadow: 1px 1px 10px 1px #555555;
}

</style>
