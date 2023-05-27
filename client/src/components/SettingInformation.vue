<template>
    <div @click="showSettingInformation"> 
        <div class="cursor-pointer text-zinc-600">
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
                <button class="ml-0.5 hover:bg-primary-400 py-1 px-1 rounded-full">
                    <h3 class="text-sm font-semibold">メールを削除する</h3>
                </button>    
            </div>
        </div>
    </div>
    

        
</template>

<script setup>
import ClockOutlineIcon from "vue-material-design-icons/ClockOutline.vue";

import { ref } from "vue";
const SettingInformationOpen = ref(false);
const showSettingInformation = () => {
    SettingInformationOpen.value = !SettingInformationOpen.value;
}

import Information from "vue-material-design-icons/InformationOutline.vue";
import TrashCanOutline from "vue-material-design-icons/TrashCanOutline.vue";

const alarmDate = ref("");
const alarmTime = ref("");

const saveAlarm = () => {
  const dateParts = alarmDate.value.split("-");
  const year = parseInt(dateParts[0]);
  const month = parseInt(dateParts[1]) - 1;
  const day = parseInt(dateParts[2]);
  const date = new Date(year, month, day);

  const timeParts = alarmTime.value.split(":");
  const hours = parseInt(timeParts[0]);
  const minutes = parseInt(timeParts[1]);

  const time = new Date();
  time.setFullYear(date.getFullYear());
  time.setMonth(date.getMonth());
  time.setDate(date.getDate());
  time.setHours(hours);
  time.setMinutes(minutes);
  time.setSeconds(0);

  const timezoneOffset = time.getTimezoneOffset() * 60000;
  const localTime = new Date(time.getTime() - timezoneOffset);
  const isoDateTime = localTime.toISOString().replace(/\:\d+\.\d+Z$/, "+09:00");

  console.log(isoDateTime);
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