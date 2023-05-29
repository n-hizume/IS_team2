<template>
    <div @click="showSettingInformation"> 
        <div class="cursor-pointer text-primary-600">
            <Information :size="20"/>
        </div>
    </div>

    <div v-if="SettingInformationOpen" id="SettingInformationSection" class="
        absolute 
        right-0 
        mr-9
        rounded-2xl
        shadow-2xl 
        bg-white"
    >
        <div class="px-4 py-4">
            <div class="flex text-zinc-600">
                <ClockOutlineIcon :size="18" />
                <h3 class="ml-2 text-sm font-semibold">通知設定</h3>
            </div> 
            <div class="ml-5 text-zinc-600" style="text-align: left;">   
                <div class="date mt-3 cursor-pointer">
                        <label for="alarm-date" class="custom block text-sm font-semibold"></label>
                        <input type="date" id="alarm-date" v-model="alarmDate" class="rounded-full px-2 py-1">
                </div>
                <div class="flex items-center">
                    <div class="time mt-3">
                            <label for="alarm-time" class="block"></label>
                            <input type="time" id="alarm-time" v-model="alarmTime" class="border rounded-full px-2 py-1">
                    </div>
                    <div class="mt-3 ml-2">
                            <button @click="saveAlarm" class="text-sm bg-zinc-600 hover:bg-primary-400 text-white font-bold py-1.5 px-2 rounded-full">
                            保存
                            </button>
                    </div>
                </div>    
            </div>  
            <div class="mt-5 flex text-zinc-600 cursor-pointer">
                <TrashCanOutline :size="18" class="mt-1" />
                <button class="hover:bg-primary-400 py-1 px-2 rounded-full">
                    <h3 class="text-sm font-semibold">メールを削除する</h3>
                </button>    
            </div>
        </div>
    </div>
    

        
</template>

<script setup>
import ClockOutlineIcon from "vue-material-design-icons/ClockOutline.vue";
import { ref, defineProps, toRefs, watch } from "vue";
import Information from "vue-material-design-icons/InformationOutline.vue";
import TrashCanOutline from "vue-material-design-icons/TrashCanOutline.vue";
import { setExpiry } from "@/apis/mail";
import store from '@/store/index';

const props = defineProps({
  threadId: String
});

const threadId = ref(toRefs(props).threadId.value);
watch(props,
    () => {
        threadId.value = toRefs(props).threadId.value;
    }
)

const SettingInformationOpen = ref(false);
const showSettingInformation = () => {
    SettingInformationOpen.value = !SettingInformationOpen.value;
}

const options = {
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  timeZone: 'Asia/Tokyo' // 日本のタイムゾーン
};
var japanTime = new Intl.DateTimeFormat('ja-JP', options).format(new Date());
japanTime = japanTime.split(" ");
const alarmDate = ref(japanTime[0].replaceAll("/", "-"));
const alarmTime = ref(japanTime[1]);

const saveAlarm = async () => {
    const expiry = alarmDate.value + "T" + alarmTime.value + "+09:00";
    await setExpiry(threadId.value, expiry);
    store.commit("setExpiry", { threadId: threadId.value, expiry: expiry });
    SettingInformationOpen.value = false;
}


</script>

<style>
#SettingInformationSection {
overflow: hidden;
width: 200px;
height: 196px;

}

.custom{
   -webkit-tap-highlight-color:rgba(0,0,0,0);
}

*:focus {
outline: none;
}





</style>