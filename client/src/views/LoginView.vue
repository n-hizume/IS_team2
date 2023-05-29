<template>
    <div>
      <el-progress v-if="isGetMail"
        :percentage="100"
        status="success"
        :indeterminate="true"
        :duration="5"
      />
    </div>
    <div id="LoginView" class="grid h-screen place-items-center">
        <div class="video-container">
            <video src="img/LoginMovie.mp4" autoplay loop muted playsinline ></video>
        </div>
        <div class="container">
            <div class="content ">
                <div class="image-container">
                    <img class="login-image" src="img/GmailLogin.png" alt="">
                </div>
                <div class="font-semibold text-primary-600 bg-white login-btn m-5" @click="login">
                    Google ログイン
                </div>
            </div>
            
        </div>
    </div>
    
</template>

<script setup>
import { googleSdkLoaded } from "vue3-google-login";
import { storeToken } from '@/apis/mail'
import { storeMails } from '@/utils/index'
import { useRouter } from "vue-router";
import { ref } from 'vue'

const router = useRouter();

var isGetMail = ref(false)

const login = () => {
    googleSdkLoaded((google) => {
        google.accounts.oauth2.initCodeClient({
            client_id: '290280505278-jr662shaa29lke42ckon55fumjp8dn4b.apps.googleusercontent.com',
            scope: 'https://www.googleapis.com/auth/gmail.modify',
            callback: async (response) => {
                isGetMail.value = true;
                await storeToken(response.code);
                await storeMails()
                // isGetMail.value = false;
                
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

.video-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
}

.video-container video {
    width: 100%;
    height: 100%;
    object-fit: cover;

    background-color: white;
    opacity: 0.3;
    z-index: 2;
}

.container {
    
    position: relative;
    text-align: center;
    z-index: 3;
}

.content {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
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
    display: inline-block;
    
    
}

.login-btn:hover {
    cursor: pointer;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.25);
}



</style>