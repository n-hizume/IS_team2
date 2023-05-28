<template>
    <div id="LoginView" class="grid h-screen place-items-center">
        <div class="container">
            <div class="image-container">
                <img class="login-image" src="img/GmailLogin.png" alt="">
            </div>
            <div class="font-semibold text-primary-600 login-btn m-5 mx-auto" @click="login">
                Google ログイン
            </div>
        </div>
    </div>
</template>


<script setup>
import { googleSdkLoaded } from "vue3-google-login";
import { storeToken } from '@/apis/mail'
import { storeMails } from '@/utils/index'
import { useRouter } from "vue-router";

const router = useRouter();

const login = () => {
    googleSdkLoaded((google) => {
        google.accounts.oauth2.initCodeClient({
            client_id: '290280505278-jr662shaa29lke42ckon55fumjp8dn4b.apps.googleusercontent.com',
            scope: 'https://www.googleapis.com/auth/gmail.modify',
            callback: async (response) => {
                await storeToken(response.code);
                await storeMails()
                router.push({name:'email'})
            }
        }).requestCode();

    })
}



</script>

<style lang="scss">
#LoginView {
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    text-align: center;
}

.image-container {
    display: flex;
    justify-content: center;
}

.login-image {
    width: 350px;
}

.login-btn {
    border-radius: 20px;
    padding: 10px;
    box-shadow: 0 0px 20px 0 rgba(0, 0, 0, .1);
    width: 200px; 
}

.login-btn:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.25);
}
</style>
