<template>
    <div @click="SettingInformationOpen = true" class="
    cursor-pointer">
        <Information :size="20"/>
    </div>

    <div v-if="SettingInformationOpen" id="SettingInformationSection" class="
        absolute 
        
        right-0 
        mr-9
        
        rounded-2xl
        shadow-2xl 
        bg-white"
    >
    <div class="flex items-center justify-between rounded-t-lg w-full text-sm px-3.5 py-2.5">
        <CloseIcon class="cursor-pointer ml-auto mb-1" @click="SettingInformationOpen = false" :size="19" />
    </div>
    </div>
        
</template>

<script setup>
import { ref } from "vue";
let SettingInformationOpen = ref(false)

SettingInformationOpen.value = false

import Information from "vue-material-design-icons/InformationOutline.vue";
import CloseIcon from "vue-material-design-icons/Close.vue";

</script>

<style>
#SettingInformationSection {
overflow: hidden;
width: 200px;
height: 250px;
}
</style>