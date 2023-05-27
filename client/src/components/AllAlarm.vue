<template>
    <div class="allmail" >
          <div class="mt-3 mb-1 ml-4 mr-2 text-start pl-4 font-bold text-primary-600">
            <p>通知</p>
          </div>  
          <div class="mailbox" style="overflow-y: auto;">
            <div class="ml-6">
              <button
                v-for="mail in mailDatas"
                :key="mail.id"
                style="text-align: left; overflow:hidden;"
                class="mail my-0.5 rounded-2xl cursor-pointer px-4 py-0.5"
                @click="selectMail(mail)"
              >
                <div class="flex items-center justify-between mb-1">
                  <div class="mr-1 text-zinc-800">
                    <p style="font-size:15px">{{ mail.from }}</p>
                  </div>  
                  <div class="ml-5">
                    
                 
                    <div style="color: crimson;" class="flex">
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
                  <div class="subject text-zinc-700" style="overflow: hidden;">
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
import store from '@/store/index';


const router = useRouter()

var selectMail = (mail) => {
  router.push({ name: "maildetailforalarm", query: { id: mail.id }});
};


function formatDate(date) {
  const today = new Date(); // 今日の日付を取得
  const yesterday = new Date(today); // 今日の日付をコピーして昨日の日付を作成
  yesterday.setDate(yesterday.getDate() - 1); // 昨日の日付に変更

  const month = date.getMonth() + 1;
  const day = date.getDate();

  if (
    date.getDate() === today.getDate() &&
    date.getMonth() === today.getMonth() &&
    date.getFullYear() === today.getFullYear()
  ) {
    return "今日";
  } else if (
    date.getDate() === yesterday.getDate() &&
    date.getMonth() === yesterday.getMonth() &&
    date.getFullYear() === yesterday.getFullYear()
  ) {
    return "昨日";
  } else {
    return month + "月" + day + "日";
  }
}

const mailDatas = [];

for(const mail of store.state.mails){
  
    if (!mail.expiry){
        continue;
    }
  var date = new Date(mail.date);
  var expiry = new Date(mail.expiry);
  
  mailDatas.push({
    "id": mail.id, //メールのID
    "threadId": mail.threadId, //メールのスレッドID
    "snipet": mail.snipet, //メールのスニペット(本文の書式なしデータのようなもの)
    "body": mail.body, //本文(書式や改行なども含む)
    "subject": mail.subject, //メールのタイトル
    "from": mail.from, //送信者
    "to": mail.to, //受信者(=自分)
    "date": formatDate(date),
    "expiry": formatDate(expiry),
  });
  
}

const sortedmails = mailDatas.sort((a, b) => {
  if (a.expiry === "今日" && b.expiry !== "今日") {
    return -1; 
  } else if (a.expiry !== "今日" && b.expiry === "今日") {
    return 1; 
  } else {
    return 0; 
  }
});

console.log(sortedmails);

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

  

  .date.expirynotempty {
    display: none
  }


</style>