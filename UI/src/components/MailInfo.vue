<template>
    <button @click="SettingOpen = true" class="mt-1 ml-auto mr-3">
        <InformationIcon :size="20" />
    </button>    

    <div v-if="SettingOpen" id="SettingOpenSection">
    </div>
</template>

<script setup>
import { ref } from "vue";

import InformationIcon from "vue-material-design-icons/InformationOutline.vue";


let SettingOpen = ref(false)
</script>

<style lang="scss">
#SettingOpenSection {
overflow: hidden;
width: 560px;
height: 570px;
}
</style>