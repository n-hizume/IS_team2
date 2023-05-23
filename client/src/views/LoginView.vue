<template>
    <div id="LoginView" class="grid h-screen place-items-center">
        <div>
            <img width="279" src="img/GmailLogin.png" alt="">
            <div class="flex justify-center">
                <GoogleLogin :callback="callback"/>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { onMounted } from '@vue/runtime-core'
    import { useRouter } from 'vue-router';

    const router = useRouter()

    onMounted(() => {
        setTimeout(() => { router.push('/email') }, 250)
    })

    const callback = async () => {
        setTimeout(() => { router.push('/email') }, 250)
    }
</script>
