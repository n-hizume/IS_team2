<template>
    <div class="allmail" >
          <div class="mt-3 ml-4 mr-2 text-start pl-4 font-bold text-primary-600">
            <p>通知</p>
          </div>  
          <div class="mailbox mt-1" style="overflow-y: auto;">
            <div class="mt-1.5 ml-6">
              <button
                v-for="mail in mailDatas"
                :key="mail.id"
                style="text-align: left;"
                class="mail my-0.5 rounded-2xl cursor-pointer px-4"
                @click="selectMail(mail)"
              >
                <div class="flex items-center mb-1">
                  <div class="mr-1">
                    <p style="font-size:15px">{{ mail.from }}</p>
                  </div>  
                  <div class="ml-5">
                    
                    <p style="font-size:10px">{{ mail.expiry }}</p>
                  
                    <p style="font-size:10px">{{ mail.date }}</p>
                      
                  </div>
                </div>  
                <div  style="font-size:14px" class="ml-2">
                  <p>{{ mail.subject }}</p>
                  <p>{{ mail.snipet }}</p>
                </div>  
              </button>
            </div>
          </div>  
        </div> 
</template>

<script setup>

import { useRouter } from "vue-router";
import store from '@/store/index';


const router = useRouter()

const selectMail = (mail) => {
  store.commit('setFocusMail', mail);
  router.push('/alarm/maildetail')
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
    "subject": "test: from isteam2 to hizumee228", //メールのタイトル
    "from": "Naoki Hizume <ku.is.team2@gmail.com>", //送信者
    "to": "hizumee228@gmail.com", //受信者(=自分)
    "date": formatDate(date),
    "expiry": formatDate(expiry),
  });
  
}

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