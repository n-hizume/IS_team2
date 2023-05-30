<template>
  <div class="allmail" >
    <div class="mt-3 mb-1 ml-4 mr-2 text-start pl-4 font-bold text-primary-600">
      <p>{{ isAlarm?"通知":"受信箱" }}</p>
    </div>  
    <div class="mailbox" style="overflow-y:scroll;">
      <div class="ml-6">
        <button
          v-for="mail in mailDatas"
          :key="mail.id"
          style="text-align: left; overflow:hidden;"
          class="mail my-0.5 rounded-2xl cursor-pointer px-4 py-0.5 hover:bg-primary-1000"
          @click="selectMail(mail)"
        >
          <div class="flex items-center justify-between mb-1">
            <div class="from mr-1 text-zinc-800">
              <p style="font-size:15px">{{ mail.from }}</p>
            </div>  
            <div class="ml-5">
              
              <div v-bind:class="{'notexist': mail.expiry==''}" style="color: crimson;" class="flex expiry">
                <ClockOutlineIcon :size="14" />
                <div class="ml-1.5">
                  <p style="font-size:10px">{{ mail.expiry }}</p>
                </div>
              </div>
              <div class="ml-5 mr-1 text-zinc-700">
                <p style="font-size:10px">{{ mail.date }}</p>
              </div>
                
            </div>
          </div>  
          <div  style="font-size:14px" class="ml-2">
            <div class="subject text-zinc-500 font-bold" style="overflow: hidden; ">
              <p>{{ mail.subject }}</p>
            </div>  
            <div class="snipet text-zinc-700" style="overflow:hidden">
              <p>{{ mail.snipet }}</p>
            </div>
          </div>  
        </button>
      </div>
    </div>  
  </div>
</template>

<script setup>

import ClockOutlineIcon from "vue-material-design-icons/ClockOutline.vue";
import { useRouter } from "vue-router";
import { getAllMails, getAllMailsForAlarm } from '@/utils/index'
import { defineProps, toRefs, ref, watch } from 'vue'
import store from '@/store/index'

const router = useRouter()
const props = defineProps({
  isAlarm: Boolean
});

const isAlarm = toRefs(props).isAlarm.value;

var selectMail = (mail) => {
  if(isAlarm) router.push({ name: "maildetailforalarm", query: { id: mail.id }});
  else router.push({ name: "maildetail", query: { id: mail.id }});
};

const mailDatas = ref(isAlarm?getAllMailsForAlarm():getAllMails());

if(mailDatas.value.length>0) selectMail(mailDatas.value[0]);
console.log(mailDatas.value.length)

watch(
  store.state.mails,
  () => {
    mailDatas.value = isAlarm?getAllMailsForAlarm():getAllMails();
  }
)

</script>


<style lang="scss">

  .mail-box {
    width: 90%;
    height: 799px;
    background: #F4F4F3;
  }

  .flexbox {
    display: flex;
    flex-direction: column;
    text-align: center;
    width: 300px;
    height: 100px;
  }

  .mail {
    width: 400px;
    height: 116px;
    background: #FDFDFD;
  }

  .mailbox{
    height: 739px;
    background: #F4F4F3;
  }

  .subject{
    height:20px;
  }

  .snipet{
    height:40px;
  }

  .from{
    width: 264px;
  }

  .expiry.notexist {
    display: none !important;
  }

 
</style>