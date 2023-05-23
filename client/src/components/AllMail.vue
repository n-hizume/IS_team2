<template>
  <div class="allmail" >
    <div class="mt-3 ml-4 mr-2 text-start pl-4 font-bold text-primary-600">
      <p><slot></slot></p>
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
  router.push('/email/maildetail')
};




const serverData = { 
    "mails":[
        {   
            "id":"abcdefg", //メールのID
            "threadId": "hijklmn", //メールのスレッドID
            "snipet": "これはテストです。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。", //メールのスニペット(本文の書式なしデータのようなもの)
            "body": "これはテストです。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n", //本文(書式や改行なども含む)
            "subject": "test: from isteam2 to hizumee228", //メールのタイトル
            "from": "Naoki Hizume <ku.is.team2@gmail.com>", //送信者
            "to": "hizumee228@gmail.com", //受信者(=自分)
            "date": "2023-05-23T10:10+09:00", //メールの受信日時
            "expiry": "" //我々のアプリで設定されたメールの締め切り日時(設定していなければnull)
        },
        {   
            "id":"opqrstu",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-23T10:10+09:00",
            "expiry": "2023-05-24T23:00+09:00"
        },
        {   
            "id":"agdhbfs",
            "threadId": "akfjs",
            "snipet": "これはテストです(ver3)。平山紗季のアカウントからhizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(ver3)。\r\n\r\n平山紗季のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 3",
            "from": "Saki Hirayama <hirayamasaki@kuhp.kyoto-u.ac.jp>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-22T10:10+09:00",
            "expiry": "2023-05-25T23:00+09:00"
        },
        {   
            "id":"ahfksjd",
            "threadId": "mvjdu",
            "snipet": "これはテストです(Ver4)。 ひらやまさきのアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver4)。\r\n\r\nひらやまさきのアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Saki Hirayama <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-20T10:10+09:00",
            "expiry": "2023-05-26T23:00+09:00"
        },
        {   
            "id":"aaaaaaa",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-19T10:10+09:00",
            "expiry": "2023-05-20T23:00+09:00"
        },
        {   
            "id":"aaaaaaa",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-19T10:10+09:00",
            "expiry": "2023-05-21T23:00+09:00"
        },
        {   
            "id":"aaaaaaa",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-18T10:10+09:00",
            "expiry": "2023-05-19T23:00+09:00"
        },
        {   
            "id":"aaaaaaa",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-17T10:10+09:00",
            "expiry": "2023-05-17T23:00+09:00"
        },
        {   
            "id":"aaaaaaa",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-16T10:10+09:00",
            "expiry": "2023-05-17T23:00+09:00"
        },
        {   
            "id":"aaaaaaa",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-15T10:10+09:00",
            "expiry": "2023-05-16T23:00+09:00"
        },
        {   
            "id":"aaaaaaa",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-14T10:10+09:00",
            "expiry": "2023-05-15T23:00+09:00"
        },
        {   
            "id":"aaaaaaa",
            "threadId": "vwxyz",
            "snipet": "これはテストです(Ver2)。 isteam2のアカウントから hizumee228のアカウントにメールを送ります。",
            "body": "これはテストです(Ver2)。\r\n\r\nisteam2のアカウントから\r\nhizumee228のアカウントにメールを送ります。\r\n",
            "subject": "test ver 2",
            "from": "Naoki Hizume <ku.is.team2@gmail.com>",
            "to": "hizumee228@gmail.com",
            "date": "2023-05-12T10:10+09:00",
            "expiry": "2023-05-13T23:00+09:00"
        },
        
    ]
}

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

for(const mail of serverData.mails){
  
    
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